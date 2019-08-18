import falcon

app = falcon.API()


class Handler(object):

    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.body = "Hello world!"
        

handler = Handler()

app.add_route('/', handler)
