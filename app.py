import os
import socket

from flask import Flask, render_template

app = Flask(__name__)

APP_MESSAGE = os.environ.get("APP_MESSAGE", "Fallback message.<br><br>Override with:<br> <code>-e APP_MESSAGE=...</code>")
PORT = int(os.environ.get("PORT", 5000))


@app.route("/")
def hello_world():
    return render_template(
        "index.html",
        message = APP_MESSAGE,
        hostname=socket.gethostname(),
        port=PORT
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)