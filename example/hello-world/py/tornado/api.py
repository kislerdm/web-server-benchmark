import tornado.ioloop
import tornado.web
import logging

# turn off tornado logger
logs_tornado = logging.NullHandler()
logs_tornado.setLevel(logging.DEBUG)
logging.getLogger("tornado.access").addHandler(logs_tornado)
logging.getLogger("tornado.access").propagate = False


class Handler(tornado.web.RequestHandler):
    def get(self):
        self.write({"data": "Hello World!"})


def make_app():
    return tornado.web.Application([
        (r"/", Handler),
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(4500, address='0.0.0.0')
    tornado.ioloop.IOLoop.current().start()
