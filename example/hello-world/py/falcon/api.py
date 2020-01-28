import json
import falcon


app = falcon.API()


class Handler(object):

    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.content_type = "application/json"
        resp.body = json.dumps({"data": "Hello world!"})
        

handler = Handler()

app.add_route('/', handler)
