import os
from flask import Flask, request, json
from main import insertUsuario

app = Flask("teste")

@app.route("/olamundo", methods=["GET"])
def olaMundo(self):
    return {"ola": "mundo"}

#USANDO POSTMAN
#@app.route("/cadastra", methods=["POST", "GET"])
#def cadastraUsuario():
#    body = request.get_json()

#    print(body)

#    return body

@app.route("/cadastra", methods=["POST", "GET"])
def cadastraUsuarios(self):
    filename = os.path.join("", "body.json")
    with open(filename) as blog_file:
        data = json.load(blog_file)


    return data


app.run()