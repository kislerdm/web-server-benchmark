local cjson = require('cjson')
                
ngx.header.content_type = 'application/json'  
ngx.status = ngx.HTTP_OK  
ngx.say(cjson.encode({ data = 'Hello World!' }))  