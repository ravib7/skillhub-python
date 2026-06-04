from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return {"message":"welcome to flask"}

@app.route("/about", methods=["POST"])
def about():
    return {"message":"welcome to about"}

@app.route("/us", methods=["PATCH"])
def contact():
    return {"message":"welcome to contact"}

app.run(debug=True)