from flask import Flask, Response
import json


HOST = "0.0.0.0"
PORT = 4500

app = Flask(__name__)


@app.route("/")
def handler():
    return Response(response=json.dumps({"data": "Hello World!"}),
                    content_type='application/json',
                    status=200)


if __name__ == "__main__":
    app.run(host=HOST, port=PORT, debug=False)
