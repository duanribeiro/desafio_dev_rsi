from flask import Flask, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb+srv://duanribeiro:BJ183r32@futebol-iwbwh.mongodb.net/test?retryWrites=true&w=majority")
db = client['desafio']

@app.route("/", methods=["GET"])
def test():
    return jsonify({'messager':'success'}), 200

#
# @app.route("/usuario/login", methods=["POST"])
# def usuario_login():
#     return jsonify({'messager':'success'}), 200
#
#
# @app.route("/usuario/logout", methods=["GET"])
# def usuario_logout():
#     return jsonify({'messager':'success'}), 200
#
#
# @app.route("/conta", methods=["POST"])
# def conta():
#     return jsonify({'messager':'success'}), 200
#
#
# @app.route("/conta/adicionarSaldo", methods=["POST"])
# def conta_adicionarSaldo():
#     return jsonify({'messager':'success'}), 200
#
#
# @app.route("/conta/<id>", methods=["DELETE", "GET"])
# def conta_id(id):
#     return jsonify({'messager':'success'}), 200
#
#
# @app.route("/extrato", methods=["POST"])
# def extrado():
#     return jsonify({'messager':'success'}), 200
#
#
# @app.route("/extrato/<conta>", methods=["DELETE", "GET"])
# def extrato_conta(conta):
#     return jsonify({'messager':'success'}), 200
#
#
# @app.route("/tranferir", methods=["POST"])
# def tranferir():
#     return jsonify({'messager':'success'}), 200
#
#
@app.route("/usuario", methods=["POST", "PUT"])
def usuario():
    if request.method == "POST":
        usuario = {
            "bairro": "Jabotiana"
            # "cidade": "Aracaju",
            # "complemento": "T2",
            # "cpf": 78771926909,
            # "dataNascimento": "2001-02-06",
            # "email": "jaquelinestefanyalmada_@compuativa.com.br",
            # "estado": "SE",
            # "nome": "Jaqueline Stefany",
            # "numero": 907,
            # "pais": "BRASIL",
            # "password": "CYtzI2uZis",
            # "rua": "Rua C",
            # "sobrenome": "Almada"
        }
        print(1)
        db.usuarios.insert(usuario)

    return jsonify({'messager':'success'}), 201

#
# @app.route("/usuario/<cpf>", methods=["DELETE", "GET"])
# def usuario_cpf(cpf):
#     return jsonify({'messager':'success'}), 200



if __name__ == "__main__":
    app.run(host="0.0.0.0", port='5000', debug=True)