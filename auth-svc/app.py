from bottle import Bottle, route, run, get, template, post, request, response
import pymysql
# import json


def createUser(user,password):
	mysql_config = {
		'host':'localhost',
		'db': 'users',
		'user':'root',
		'passwd':'root'
	}
	cnx = None
	try: 
		cnx = pymysql.connect(**mysql_config)
		insertStr = "INSERT INTO credentials (username,password) VALUES(%s,%s)"
		data = (user,password)
		cursor = cnx.cursor()
		cursor.execute(insertStr,data)
		cnx.commit()
		cursor.close()
		cnx.close()
	except pymysql.MySQLError as err:
		print "MySQLError: {0}".format(err)
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
		'passwd':'root'
	}
	cnx = None
	try: 
		cnx = pymysql.connect(**mysql_config)

		selectStr = "select id , count(*) from credentials where username='{0}' and password='{1}'".format(user, password)
		cursor = cnx.cursor()
		cursor.execute(selectStr)
		row = cursor.fetchone()
		cursor.close()
		cnx.close()
		if row[1] > 0:
			return True, row[0] 
		else:
			return False, False	
	except pymysql.MySQLError as err:
		print "Failed to select.....{0}".format(err)
		return False, False

def auditEvent(event, userid):
	mysql_config = {
		'host':'localhost',
		'db': 'users',
		'user':'root',
		'passwd':'root'
	}
	cnx = None
	try: 
		cnx = pymysql.connect(**mysql_config)
		insertStr = "INSERT INTO audit_event (event,userid) VALUES('{0}',{1})".format(event,userid)
		print insertStr
		cursor = cnx.cursor()
		cursor.execute(insertStr)
		cnx.commit()
		cursor.close()
		cnx.close()
	except pymysql.MySQLError as err:
		print "MySQLError: {0}".format(err)
		return False

	return True

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
	a,userid = searchUser(data["username"], data["password"])
	if a:
		auditEvent("Correct Login",userid)
		return { "status": "OK", "message": "Bienvenido"}
	auditEvent("Wrong Login", "NULL")
	return {"status": "ERROR", "message": "se ingreso mal el usuario"}

@app.post('/register')
def register_json():
	data = request.json
	print data
	a, userid = createUser(data["username"], data["password"])
	if a:
		auditEvent("Correct Register",userid)
		return {"status": "OK", "message": "se registro correctamente el usuario"}
	else:
		auditEvent("Wrong Register", "NULL")
		return {"status": "ERROR", "message": "No se pudo registrar"}

@app.post('/logout')
def logout_json():
	print "POST: logout..."
	data = request.json
	print data
	a, userid = searchUser(data["username"], data["password"])
	if a:
		auditEvent("Correct Logout",userid)
		return { "status": "OK", "message": "ADIOS"}
	else:
		auditEvent("Correct Logout","NULL")
		return { "status": "OK", "message": "ADIOS"}
	
run(app,host='127.0.0.1',port=8081)
