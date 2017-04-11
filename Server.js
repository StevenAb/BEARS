const express = require('express');
const bodyParser = require('body-parser');
var db = require('mongodb');
const MongoClient = require('mongodb').MongoClient;
const app = express();

//actually retrieve data inputted
app.set('view engine', 'ejs');
app.use(express.static('c:\\Users\\almei\\Desktop\\Node\\TestServer' + '/views'));
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({extended: true}));



MongoClient.connect('mongodb://stephanie_almeida:Saggi1212@ds163377.mlab.com:63377/bears-senior-project', (err, database) => {
	if (err)
		return console.log(err);
	app.locals.db = database;
	app.locals.id = 1;
	//listening to certain port
	app.listen(3000, function() {
	console.log('listening on 3000')
	});
});

//callback function --> what to do when path is matched
app.get('/', (req, res) => {
	name = String(app.locals.id);
	//res.sendFile('c:\\Users\\almei\\Desktop\\Node\\TestServer\\index.html');
	app.locals.db.collection(name).find().toArray((err, result) => {
		if (err)
			return console.log(err);
		res.render('index.ejs', {id: result});
	});
});


app.post('/addusers', (req, res) => {
	name = String(app.locals.id);
	/*app.locals.db.collection(name).save(req.body, (err, result) => {
		if (err)
			return console.log(err);
		console.log('saved to database');
		app.locals.id = app.locals.id + 1;
		res.redirect('/');
	});*/



/*	db.collection('usercollection').save(req.body, (err, result) => {
		if (err)
			return console.log(err);
		console.log('saved to database');
		id++;
		res.redirect('/');
	});*/

	app.locals.db.collection("usercollection").insert([{user: req.body.user, pass: req.body.pass, id: app.locals.id}], (err, result) => {
		if (err)
			return console.log(err);
		app.locals.id = app.locals.id + 1;
		res.redirect('/');
		app.locals.collection = app.locals.db.collection(name).save({}, (err, result) => {
			if (err)
				return console.log(err);
		});
	});
	console.log(req.body);
});

app.post('/checkusers', (req, res) => {

	var datab = app.locals.db;
	 app.locals.username = req.body.user;	
	app.locals.password = req.body.pass;
	var collection = app.locals.db.collection("usercollection");
	//console.log(collection);
	collection.findOne({user: app.locals.username, pass: app.locals.password}, function(err, user) {
		if (user == null) {
			console.log("no username/pass");
			res.redirect('back');
		}
		else if (err) {
			return console.log(err);
		}
		else {
			console.log(user.id);
			app.locals.id = parseInt(user.id);
			return res.redirect('/');
		}
	});

	/*datab.getCollectionNames().forEach(function(collname) {
		var user = db[collname].find({ user: {$gt: username}});
		var pass = db[collname].find({ user: {$get: password}});
		if (user == null && pass == null) {
			alert('Either username or password is incorrect!');
		}
		else {
			id = collname;
		}
	});*/

});

app.post('/delete', (req, res) => {
	name = String(app.locals.id);

	app.locals.db.collection(name).remove();
	return res.redirect('/');
});

app.post('/addtranscript', (req, res) => {
	console.log(req.body);

	name = String(req.body.id);

	if (req.body.transcript == "false") {

	}
	else {
		app.locals.db.collection(name).save(req.body, (err, result) => {
		if (err)
			return console.log(err);
		console.log('saved to db');
		res.redirect('/');
	});
	}

});