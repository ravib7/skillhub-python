from flask import Flask, request, jsonify
import json

app = Flask(__name__)

def get_all_notes():
    with open("db.json", "r") as file:
        return json.load(file)
    

def create_note(single_note):
    with open("db.json", "w") as file:
        json.dump(single_note, file)


@app.route("/", methods=["GET"])
def home():
    return {"message":"app running"}


@app.route("/todo/create", methods=["POST"])
def createTodo():
    # step1 read body
    body = request.json
    # step2 write to db.json
    data = get_all_notes() # {notes:[]}
    data["notes"].append(body) # [notes:[{task:"learn python"}]]
    create_note(data)
    return {"message":"todo create success"}


@app.route("/todos", methods=["GET"])
def readTodo():
    data = get_all_notes()["notes"]
    return {"message":"todo read success", "data":data}


@app.route("/todo/modify", methods=["PATCH"])
def updateTodo():
    return {"message":"todo update success"}


@app.route("/todo/remove", methods=["DELETE"])
def deleteTodo():
    return {"message":"todo delete success"}


if __name__ == "__main__":
    app.run(debug=True)