from bottle import Bottle, route, run, get, template, post, request, response
import pymysql
import os
import datetime
import python_jwt as jwt
import Crypto.PublicKey.RSA as RSA
# import json


def createUser(user,password,rol):
	mysql_config = {
		'host':'localhost',
		'db': 'users',
		'user':'root',
		'passwd':'emauzumaki09'
	}
	cnx = None
	try: 
		cnx = pymysql.connect(**mysql_config)
		insertStr = "INSERT INTO credentials (username,password,rol) VALUES(%s,%s,%s)"
		data = (user,password,rol)
		cursor = cnx.cursor()
		cursor.execute(insertStr,data)
		cnx.commit()
		cursor.close()
		cnx.close()
	except pymysql.MySQLError as err:
		print ("MySQLError: {0}".format(err))
		return False, False
		
	cnx = pymysql.connect(**mysql_config)
	selectid = "select id from credentials where username='{0}' and password='{1}'".format(user, password)
	cursor = cnx.cursor()
	cursor.execute(selectid)
	row = cursor.fetchone()
	cursor.close()
	cnx.close()
	return True, row[0]

def searchUser(user,password):
	mysql_config = {
		'host':'localhost',
		'db': 'users',
		'user':'root',
		'passwd':'emauzumaki09'
	}
	cnx = None
	try: 
		cnx = pymysql.connect(**mysql_config)

		selectStr = "select id , count(*), rol from credentials where username='{0}' and password='{1}'".format(user, password)		
		cursor = cnx.cursor()
		cursor.execute(selectStr)
		row = cursor.fetchone()
		cursor.close()
		cnx.close()
		if row[1] > 0:
			return True, row[0], row[2] 
		else:
			return False, False, False	
	except pymysql.MySQLError as err:
		print ("Failed to select.....{0}".format(err))
		return False, False ,False

def auditEvent(event, userid):
	mysql_config = {
		'host':'localhost',
		'db': 'users',
		'user':'root',
		'passwd':'emauzumaki09'
	}
	cnx = None
	try: 
		cnx = pymysql.connect(**mysql_config)
		insertStr = "INSERT INTO audit_event (event,userid) VALUES('{0}',{1})".format(event,userid)
		print (insertStr)
		cursor = cnx.cursor()
		cursor.execute(insertStr)
		cnx.commit()
		cursor.close()
		cnx.close()
	except pymysql.MySQLError as err:
		print ("MySQLError: {0}".format(err))
		return False

	return True

def getEvents(userid, rol):
	mysql_config = {
		'host':'localhost',
		'db': 'users',
		'user':'root',
		'passwd':'emauzumaki09'
	}
	cnx = None
	try:
		cnx = pymysql.connect(**mysql_config)
		if rol == "admin":
			query = "select * from audit_event order by time desc"
		else:
			query = "select * from audit_event where userid={} order by time desc".format(userid)
		print(query)
		cursor = cnx.cursor()
		cursor.execute(query)
		events = dict()
		for res in cursor:
			dict_event = {"id":None, "datetime":None, "event":None}
			dict_event['id']=res[0]
			dict_event['userid'] = res[3]
			time = "{}/{}/{} - {}:{}:{}".format(res[1].day, res[1].month, res[1].year, res[1].hour, res[1].minute, res[1].second)
			dict_event['datetime']=time
			dict_event['event']=res[2]
			# idd= "id{}".format(res[0])
			events[res[0]]= dict_event 
		cnx.commit()
		cursor.close()
		cnx.close()
	except pymysql.MySQLError as err:
		print ("MySQLError: {0}".format(err))
		return None
	return events
		

app = Bottle()

@app.route('/hello', method="GET")
def hello():
	return "Hello World!"

@app.get('/')
@app.get('/hello/<name>', method="GET")
def greet(name='Stranger'):
	return template('Hello {{name}}',name=name)

@app.post('/param')
def hello_json():
	data = request.json
	param = data['param']
	ret = {"status": "OK", "param": param}
	return ret

@app.post('/login')
def login_json():
	data = request.json
	a,userid, rol= searchUser(data["username"], data["password"])
	if a:
		auditEvent("Correct Login",userid)
		payload = {'userid': userid, 'username': data["username"], 'rol': rol}
		token = generate_token(payload)
		return { "status": "OK","token": token ,"message": "Bienvenido"}
	
	auditEvent("Wrong Login", "NULL")
	return {"status": "ERROR", "message": "se ingreso mal el usuario"}

@app.post('/register')
def register_json():
	data = request.json
	if data["rol"]!='admin' and data["rol"]!='normal':
		auditEvent("Wrong Register", "NULL")
		return {"status": "ERROR", "message": "No se pudo registrar"}
	a, userid = createUser(data["username"], data["password"],data["rol"])
	if a:
		auditEvent("Correct Register",userid)
		return {"status": "OK", "message": "se registro correctamente el usuario"}
	else:
		auditEvent("Wrong Register", "NULL")
		return {"status": "ERROR", "message": "No se pudo registrar"}

@app.post('/logout')
def logout_json():
	data = request.json
	if data["userid"]:
		auditEvent("Correct Logout",data["userid"])
		return { "status": "OK", "message": "ADIOS"}
	auditEvent("Correct Logout","null")
	return { "status": "OK", "message": "ADIOS"}

@app.post('/home')
def events_json():
	data = request.json
	events = getEvents(data["userid"], data['rol'])
	return events

def generate_token(payload):
	private_key_file = os.path.join(os.path.dirname(__file__), 'keypair.priv')
	with open(private_key_file, 'r') as fd:
		private_key = RSA.importKey(fd.read())
	token = jwt.generate_jwt(payload,private_key,'RS256',datetime.timedelta(minutes=5))
	return token

def validate_token(token):
	public_key_file = os.path.join(os.path.dirname(__file__), 'keypair.pub')
	with open(public_key_file, 'r') as fd:
		public_key = RSA.importKey(fd.read())
	try:
		header, claims = jwt.verify_jwt(token,public_key,['RS256'])
	except jwt.exceptions.SignatureError:
		print ('invalid token signature')
		raise SystemExit()

#caca = generate_token()
#print(caca)
#validate_token(caca)


run(app,host='127.0.0.1',port=8081)
