#coding: utf-8
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hell. Ryoichi !  Try Flask."

if __name__ == "__main__":
    app.run()