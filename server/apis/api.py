from flask import Blueprint, jsonify, request
from pymongo import MongoClient

api = Blueprint('blueprint', __name__)

client = MongoClient('mongodb://localhost:27017/')
db = client.desafio

@api.route("/", methods=["GET"])
def test():
    return jsonify({'message':'success'}), 200

#
# @app.route("/usuario/login", methods=["POST"])
# def usuario_login():
#     return jsonify({'message':'success'}), 200
#
#
# @app.route("/usuario/logout", methods=["GET"])
# def usuario_logout():
#     return jsonify({'message':'success'}), 200
#
#
# @app.route("/conta", methods=["POST"])
# def conta():
#     return jsonify({'message':'success'}), 200
#
#
# @app.route("/conta/adicionarSaldo", methods=["POST"])
# def conta_adicionarSaldo():
#     return jsonify({'message':'success'}), 200
#
#
# @app.route("/conta/<id>", methods=["DELETE", "GET"])
# def conta_id(id):
#     return jsonify({'message':'success'}), 200
#
#
# @app.route("/extrato", methods=["POST"])
# def extrado():
#     return jsonify({'message':'success'}), 200
#
#
# @app.route("/extrato/<conta>", methods=["DELETE", "GET"])
# def extrato_conta(conta):
#     return jsonify({'message':'success'}), 200
#
#
# @app.route("/tranferir", methods=["POST"])
# def tranferir():
#     return jsonify({'message':'success'}), 200
#
#
@api.route("/usuario", methods=["POST", "PUT"])
def usuario():
    if request.method == "POST":
        usuario = {
            "bairro": "sei la",
            "cidade": "Aracaju",
            "complemento": "T2",
            "cpf": "05087897478",
            "dataNascimento": "2001-02-06",
            "email": "jaquelinestefanyalmada_@compuativa.com.br",
            "estado": "SE",
            "nome": "Jaqueline Stefany",
            "numero": 907,
            "pais": "BRASIL",
            "password": "CYtzI2uZis",
            "rua": "Rua C",
            "sobrenome": "Almada"
        }

        if ['bairro', 'cidade', 'complemento', 'cpf', 'dataNascimento',
            'email', 'estado', 'nome', 'numero', 'pais', 'password',
            'rua', 'sobrenome'] != list(usuario.keys()):
            return jsonify({'message': 'Valor não informado, favor verificar o todos o campos do formulario'}), 405

        for key, value in usuario.items():
            if not value:
                return jsonify({'message': 'Valor ' + key + ' não informado'}), 405

        db.usuarios.insert_one(usuario)

    return jsonify({'message': 'success'}), 201


@api.route("/usuario/<cpf>", methods=["DELETE", "GET"])
def usuario_cpf(cpf):
    if request.method == "GET":
        usuario = db.usuarios.find_one({"cpf": cpf}, {'_id': 0})

        if not usuario:
            return jsonify({'message': 'Usuario não localizado'}), 404

        return jsonify({'message': 'success', 'data': usuario}), 200

    # if request.method == "DELETE":
    #
    #
    #     return jsonify({'message': 'success'}), 200

