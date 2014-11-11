import flask

app = flask.Flask(__name__)


@app.route("/")
def hello():
    return flask.jsonify({
        "hello": "world"
    })


@app.route("/health")
def health():
    return flask.jsonify({
        "status": "ok"
    })


if __name__ == '__main__':
    app.run(host="0.0.0.0")
