from bottle import Bottle, route, run, get, template, post, request
import pymysql

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
		return -1

	return 1


app = Bottle()

users = [{"username": "pepe", "password": "pepe123"},\
         {"username": "pepe4", "password": "pepe1234"}]

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
	if data in users:
		return { "status": "OK", "Description": "Bienvenido"}

	return {"status": "ERROR", "Description": "se ingreso mal el usuario"}

@app.post('/register')
def register_json():
	data = request.json
	print data
	#users.append(data)
	a = createUser(data["username"], data["password"])
	if a:
		return {"status": "OK", "Description": "se registro correctamente el usuario"}
	else:
		return {"status": "ERROR", "Description": "No se pudo registrar"}
run(app,host='127.0.0.1',port=8081)


