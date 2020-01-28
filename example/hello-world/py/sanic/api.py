from sanic import Sanic, response


HOST = "0.0.0.0"
PORT = 4500

app = Sanic(__name__)


@app.route("/")
async def handler(request):
    return response.json(body={"data": "Hello world!"},
                         content_type='application/json',
                         status=200)


if __name__ == "__main__":
    app.run(host=HOST, port=PORT, debug=False)


