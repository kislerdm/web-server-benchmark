import tornado.ioloop
import tornado.web


HOST = "0.0.0.0"
PORT = 4500


class Handler(tornado.web.RequestHandler):
    def get(self):
        self.write({"data": "Hello World!"})


def make_app():
    return tornado.web.Application([
        (r"/", Handler),
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(PORT, address=HOST)
    tornado.ioloop.IOLoop.current().start()
