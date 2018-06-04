'use strict';
var session = require('express-session');
var express = require('express');
var hb = require("express-handlebars");
var bodyparser = require('body-parser');
var request = require('request');
var app = express();

const hbsOpts = {
    defaultLayout: 'main',
    extname: 'handlebars',
    layoutsDir: __dirname + '/views/layouts/',
    helpers: {                                  // helpers globales
        foo: function() {return 'FOO!';},
        bar: function() {return 'BAR!'}
    }
};
var hbs = hb.create({defaultLayout: 'main', extname: 'handlebars'})

app.engine('handlebars', hbs.engine)
app.set('view engine', 'handlebars')
app.use(bodyparser.urlencoded({extended: true}));

app.use(session({
    secret: 'mys3cr3t',
    resave: 'false',
    saveUnitialized: true,
    cookie: {secure: false}
}
))

app.get('/home',function(req, res){
    var sess = req.session
    if(!sess.token){
        res.redirect('login');
        return;
    }
    res.render('home');
})

var login = async function(credentials){
    console.log('credentials:');
    console.dir(credentials);
    
    const options = {
        headers: {'content-type' : 'application/json'},
        url: 'http://localhost:8081/login',
        body: JSON.stringify(credentials)
    };
    await request.post(options, doLogin);
}

var doLogin = function(err, resp, body) {
    console.log(body);
    let data = JSON.parse(body);
    console.log(data);
    if(data.status == "OK") {
        return true;
    }
    return false;
}

// root..
app.get('/', function(req, res) {
    const sess = req.session
    if(!sess.token) {
        res.redirect('login');
    } else {
        res.redirect('home');        
    }
});

// login..
app.get('/login', function(req, res){
    res.render('login');
});

app.post('/login', function(req, res){
    console.log('POST /login');
    console.log('username:' + req.body.username);
    console.log('password:' + req.body.password);
    const sess = req.session;
    const credentials = {
        username: req.body.username,
        password: req.body.password
    }    
    const options = {
        headers: {'content-type' : 'application/json'},
        url: 'http://localhost:8081/login',
        body: JSON.stringify(credentials)
    };
    request.post(options, function(error, response, body) {
        let data = JSON.parse(body);
        console.dir(data);
        if(!error && response.statusCode == 200){
            if(data.status == "OK") {
                sess.token = 'token1'; 
                const homeParams = {
                    title: 'titulo',
                    identified: true,
                    items: [1,2,3],
                    helpers: {
                        bar: function() {return "bar";}
                    },
                    username: credentials.username,
                    password: credentials.password
                }
                res.redirect('home');   
            } else {
                const loginParams = {
                    error: true,
                    errorMsg: data.message
                }
                res.render('login', loginParams);
            }
        }
    });
});

app.get('/register', function(req, res){
    res.render('register');
});

app.post('/register', function(req, res){
    console.log('POST /register');
    console.log('username:' + req.body.username);
    console.log('password:' + req.body.password);
    console.log('ggwp');
    const credentials = {
        username: req.body.username,
        password: req.body.password
    }    
    const options = {
        headers: {'content-type' : 'application/json'},
        url: 'http://localhost:8081/register',
        body: JSON.stringify(credentials)
    };
    request.post(options, function(error, response, body) {
        let data = JSON.parse(body);
        console.dir(data);
        if(data.status == "OK") {
            const homeParams = {
                title: 'titulo',
                identified: true,
                items: [1,2,3],
                helpers: {
                    bar: function() {return "bar";}
                }
            }
            res.render('login', homeParams);    
        } 
        else {
            const registerParams = {
                error: true,
                errorMsg: data.message
            }
            res.render('register', registerParams);
        }
    });
});

app.post('/logout', function(req, res){
    console.log('POST /logout');
    console.log('username:' + req.body.username);
    const sess = req.session
    const body = {
        username: req.body.username,
        password: req.body.password
    }
    const options = {
        headers: {'content-type' : 'application/json'},
        url: 'http://localhost:8081/logout',
        body: JSON.stringify(body)
    };
    request.post(options, function(error, response, body) {
        let data = JSON.parse(body);
        console.dir(data);
        if(data.status == "OK") {
            sess.token = null
            res.redirect('login')
        } else {
            const homeParams = {
                title: 'titulo',
                identified: true,
                items: [1,2,3],
                helpers: {
                    bar: function() {return "bar";}
                },
                username: credentials.username,
                password: credentials.password,
                logouterror: true,
                errorMsg: data.message
            }
            res.redirect('home')
        }
    });
});

var server = app.listen(8080, '127.0.0.1', function()   {
    var host = server.address().address;
    var port = server.address().port;
    console.log("listening at http://%s:%s", host, port);
});
// npm install express-handlebars --save
// npm run live
