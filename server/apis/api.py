from flask import Blueprint, jsonify, request
from pymongo import MongoClient

api = Blueprint('blueprint', __name__)

client = MongoClient('mongodb+srv://duanribeiro:BJ183r32@futebol-iwbwh.mongodb.net/test?retryWrites=true&w=majority')
db = client.desafio

@api.route("/", methods=["GET"])
def healthcheck():
    return jsonify({'message':'success'}), 200



@api.route("/usuario/login", methods=["POST"])
def usuario_login():
    usuario = request.get_json()
    usuario["cpf"] = usuario["cpf"].replace("-", "").replace("", "")

    user = db.usuarios.find_one({"cpf": usuario["cpf"], "password": usuario["cpf"]})

    if user:
        return jsonify({'message':'success'}), 200
    else:
        return jsonify({'message':'success'}), 401

#
#
# @app.route("/usuario/logout", methods=["GET"])
# def usuario_logout():
#     return jsonify({'message':'success'}), 200
#
#
@api.route("/conta", methods=["POST"])
def conta():
    if request.method == "POST":
        conta = {
          "cpf": "05087897478",
          "id": "4568"
        }

        if ['cpf', 'id'] != list(conta.keys()):
            return jsonify({'message': ''}), 405

        for key, value in conta.items():
            if not value:
                return jsonify({'message': 'Valor ' + key + ' não informado'}), 405

        db.conta.insert_one(conta)

        return jsonify({'message': 'success'}), 200


@api.route("/conta/adicionarSaldo", methods=["POST"])
def conta_adicionarSaldo():
    if request.method == "POST":
        adicionarSaldo = {
            'conta': "4567",
            'valor': 150.45
        }

        if db.conta.find_one({"conta": adicionarSaldo["conta"]}, {'_id': 0}):
            return jsonify({'error': "Conta não localizada", 'message': "Conta " + adicionarSaldo["conta"] + "não localizada"}), 404

        db.conta.insert_one()
        return jsonify({'message': 'success'}), 200


@api.route("/conta/<id>", methods=["DELETE", "GET"])
def conta_id(id):
    return jsonify({'message':'success'}), 200


@api.route("/extrato", methods=["POST"])
def extrado():
    if request.method == "POST":
        extrado = {
              "conta": "4567",
              "data": "2019-09-28",
              "descricao": "Saldo Inicial",
              "valor": 100.50
        }

        if ['conta', 'data', 'descricao', 'valor'] != list(extrado.keys()):
            return jsonify({'message': ''}), 405

        for key, value in extrado.items():
            if not value:
                return jsonify({'message': 'Valor ' + key + ' não informado'}), 405

        db.conta.insert_one(extrado)

        return jsonify({'message': 'success'}), 200


@api.route("/extrato/<conta>", methods=["DELETE", "GET"])
def extrato_conta(conta):

    if request.method == "GET":
        conta = db.conta.find_one({"conta": conta}, {'_id': 0})

        if not conta:
            return jsonify({'message': 'Conta não localizado'}), 404

        return jsonify({'message': 'success', 'data': conta}), 200

    if request.methd == "DELETE":
        return jsonify({'message': 'success'}), 200

# @api.route("/tranferir", methods=["POST"])
# def tranferir():
#     return jsonify({'message':'success'}), 200
#
#
@api.route("/usuario", methods=["POST", "PUT"])
def usuario():
    if request.method == "POST":
        usuario = request.get_json()

        if ['nome', 'cpf', 'password', 'email', 'bairro',
            'cidade', 'complemento', 'dataNascimento', 'pais', 'rua', 'sobrenome',
            'estado', 'numero'] != list(usuario.keys()):
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
    #     db.usuarios.delete_one()
    #
    #     return jsonify({'message': 'success'}), 200

