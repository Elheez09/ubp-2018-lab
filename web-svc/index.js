'use strict';

var express = require('express');
var hb = require("express-handlebars");
var bodyparser = require('body-parser');
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

var login = function(credentials){
    return true;
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
    if(login(credentials)) {
        const homeParams = {
            title: 'titulo',
            identified: true,
            items: [1,2,3],
            helpers: {
                bar: function() {return "bar";}
            }
        }
        res.render('home', homeParams);    
    }
    else {
        const loginParams = {
            error: true,
            errorMsg: 'invalid credentials'
        }
        res.render('login', loginParams);
    }
});

var server = app.listen(8080, '127.0.0.1', function()   {
    var host = server.address().address;
    var port = server.address().port;
    console.log("listening at http://%s:%s", host, port);
});

// npm install express-handlebars --save