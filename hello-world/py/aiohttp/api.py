from aiohttp import web

PORT = 4500

async def handler(request):
    return web.Response(text="Hello World!",
                        status=200)


if __name__ == "__main__":
    app = web.Application()
    app.router.add_get('/', handler)
    web.run_app(app, port=PORT)
