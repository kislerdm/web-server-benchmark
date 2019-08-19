from sanic import Sanic, response

PORT = 4500

async def handler(request):
    return response.json(body={"data": "Hello world!"})

if __name__ == "__main__":
    app = Sanic()
    app.add_route(handler, '/')
    app.run(host="0.0.0.0", port=PORT, access_log=False)
