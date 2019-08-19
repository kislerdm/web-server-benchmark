from flask import Flask, Response
import json
app = Flask(__name__)


@app.route("/")
def handler():
    return Response(response=json.dumps({"data": "Hello World!"}),
                    content_type='application/json',
                    status=200)

if __name__ == "__main__":
    app.run()
