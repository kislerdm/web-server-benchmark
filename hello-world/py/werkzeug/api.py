from werkzeug.wrappers import Request, Response
from werkzeug.serving import run_simple

PORT = 4500


@Request.application
def handler(request):
    return Response('Hello, World!')


if __name__ == '__main__':
    run_simple(hostname='0.0.0.0', port=PORT, application=handler)
