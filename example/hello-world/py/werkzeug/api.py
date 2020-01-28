from werkzeug.wrappers import Request, Response
from werkzeug.datastructures import Headers
from werkzeug.serving import run_simple
import json


HOST = "0.0.0.0"
PORT = 4500


@Request.application
def handler(request):
    headers = Headers()
    headers.add('Content-Type', 'application/json')
    return Response(response=json.dumps({"data": "Hello World!"}),
                    headers=headers)


if __name__ == '__main__':
    run_simple(hostname=HOST, port=PORT, application=handler, 
               use_debugger=False, 
               threaded=True)
