# pip install flask
# pip list

from flask import Flask

app = Flask(__name__)  # create server

@app.route("/")
def home():
    return "Welcome to flask"

@app.route("/us")
def about():
    return "about route"

app.run()  # start server