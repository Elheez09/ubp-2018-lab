'use strict';

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
    const homeParams = {
        title: 'titulo',
        identified: true,
        items: [1,2,3],
        helpers: {
            bar: function() {return "bar";}
        }
    }
    res.redirect('login'),
    res.render('home', homeParams);
});

// login..
app.get('/login', function(req, res){
    res.render('login');
});

app.post('/login', function(req, res){
    console.log('POST /login');
    console.log('username:' + req.body.username);
    console.log('password:' + req.body.password);
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
        if(data.status == "OK") {
            const homeParams = {
                title: 'titulo',
                identified: true,
                items: [1,2,3],
                helpers: {
                    bar: function() {return "bar";}
                }
            }
            res.render('home', homeParams);    
        } else {
            const loginParams = {
                error: true,
                errorMsg: data.message
            }
            res.render('login', loginParams);
        }
    });
});

var server = app.listen(8080, '127.0.0.1', function()   {
    var host = server.address().address;
    var port = server.address().port;
    console.log("listening at http://%s:%s", host, port);
});

// npm install express-handlebars --save