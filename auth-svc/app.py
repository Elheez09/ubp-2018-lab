from bottle import Bottle, route, run, get, template, post, request, response
import pymysql
#import json


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
	except pymysql.err as err:
		print "Failed to connect.....{0}".format(err)
		return False

	return True

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

		selectStr = "select count(*) from credentials where username='{0}' and password='{1}'".format(user, password)
		#data = (user,password)
		cursor = cnx.cursor()
		cursor.execute(selectStr)
		row = cursor.fetchone()
		print "count:{0}".format(row[0])
		cursor.close()
		cnx.close()
		if row[0] > 0:
			return True
		else:
			return False		
	except pymysql.err as err:
		print "Failed to select.....{0}".format(err)
		return False


app = Bottle()

#users = [{"username": "pepe", "password": "pepe123"},\
#         {"username": "pepe4", "password": "pepe1234"}]

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
	#response.content_type = 'application/json'
	#response.status = 200
	#return json.dumps({ "status": "OK", "message": "Bienvenido"})

	a = searchUser(data["username"], data["password"])
	if a:
		return { "status": "OK", "message": "Bienvenido"}

	return {"status": "ERROR", "message": "se ingreso mal el usuario"}

@app.post('/register')
def register_json():
	data = request.json
	print data
	#users.append(data)
	a = createUser(data["username"], data["password"])
	if a:
		return {"status": "OK", "message": "se registro correctamente el usuario"}
	else:
		return {"status": "ERROR", "message": "No se pudo registrar"}
run(app,host='127.0.0.1',port=8081)


