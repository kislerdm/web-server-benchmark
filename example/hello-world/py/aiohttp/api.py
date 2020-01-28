from aiohttp import web


PORT = 4500


async def handler(request):
    return web.json_response(data={"data": "Hello World!"})


if __name__ == "__main__":
    app = web.Application()
    app.router.add_get('/', handler)
    web.run_app(app, port=PORT)
