library(RestRserve)

app = RestRserveApplication$new()

app$add_get(path = "/", 
  FUN = function(request, response) {
    response$body = '{"data": "Hello World!"}'
    forward()
  })

app$run(http_port = 4500)