var express = require('express'),
  app = express(),
  port = 4500;

app.get('/', function(req, res) {
  res.setHeader('Content-Type', 'application/json');
  res.end(JSON.stringify({ data: "Hello World!" }));
})

app.listen(port);
