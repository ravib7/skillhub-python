from flask import Flask

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return {"message":"welcome to flask"}


@app.route("/todo/create", methods=["POST"])
def createTodo():
    return {"message":"todo create success"}


@app.route("/todos", methods=["GET"])
def readTodo():
    return {"message":"todo read success"}


@app.route("/todo/update", methods=["PUT"])
def updateTodo():
    return {"message":"todo update success"}


@app.route("/todo/remove", methods=["DELETE"])
def deleteTodo():
    return {"message":"todo remove success"}
    

@app.route("/me", methods=["GET"])
def me():
    return {"message":"john doe", "role":"admin"}
    

if __name__== "__main__":
    app.run(debug=True)