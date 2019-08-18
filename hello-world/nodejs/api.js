var express = require('express'),
  app = express(),
  port = 4500;

app.get('/', function(req, res) {
  res.end("Hello World!");
})

app.listen(port);
