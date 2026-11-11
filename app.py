import os
import socket

from flask import Flask, jsonify

app = Flask(__name__)

APP_VERSION = os.getenv("APP_VERSION", "dev")


@app.route("/")
def index():
    return jsonify(
        message="Hello from the Harness demo app!",
        version=APP_VERSION,
        host=socket.gethostname(),
    )


@app.route("/health")
def health():
    return jsonify(status="ok"), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", "8080")))
