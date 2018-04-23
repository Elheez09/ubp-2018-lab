from bottle import Bottle, route, run, get, template, post, request
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
	users.append(data)
	return {"status": "OK", "Description": "se registro correctamente el usuario"}


run(app,host='127.0.0.1',port=8081)


