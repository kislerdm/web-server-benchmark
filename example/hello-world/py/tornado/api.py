import tornado.ioloop
import tornado.web


class Handler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello World!")


def make_app():
    return tornado.web.Application([
        (r"/", Handler),
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(4500, address='0.0.0.0')
    tornado.ioloop.IOLoop.current().start()
