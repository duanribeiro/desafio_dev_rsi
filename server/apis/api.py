from flask import Blueprint, jsonify, request, session
from pymongo import MongoClient
from bson import ObjectId

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

    # session['cpf'] = usuario["cpf"]
    user = db.usuarios.find_one({"cpf": usuario["cpf"], "password": usuario["cpf"]})

    if user:
        if not db.conta.find_one({"cpf": usuario["cpf"]}):
            conta = db.conta.insert_one({"cpf": usuario["cpf"],
                                         "saldo": 0})

            return jsonify({'message': 'success',
                            'data': {"id": str(conta.inserted_id)}
                            }), 200

        else:
            conta = db.conta.find_one({"cpf": usuario["cpf"]})
            return jsonify({'message': 'success',
                            'data': {"id": str(conta['_id'])}
                            }), 200
    else:
        return jsonify({'message':'success'}), 401



# @app.route("/usuario/logout", methods=["GET"])
# def usuario_logout():
#     return jsonify({'message':'success'}), 200
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
        adicionarSaldo = request.get_json()
        adicionarSaldo['conta'] = ObjectId(adicionarSaldo["conta"])
        adicionarSaldo['valor'] = float(adicionarSaldo["novosaldo"])

        conta = db.conta.find_one({"_id": adicionarSaldo["conta"]}, {'_id': 0})
        if not conta :
            return jsonify({'error': "Conta não localizada", 'message': "Conta " + adicionarSaldo["conta"] + "não localizada"}), 404

        else:
            db.conta.update({"_id": adicionarSaldo["conta"]}, {"$set": {"saldo": adicionarSaldo['valor'] + conta['saldo']}})

        return jsonify({'message': 'success'}), 200


@api.route("/conta/<id>", methods=["DELETE", "GET"])
def conta_id(id):
    if request.method == "GET":
        id = ObjectId(id)
        conta = db.conta.find_one({"_id": id}, {'_id': 0})

    return jsonify({'message':'success',
                    'data': {'saldo': conta['saldo']}
                    }), 200


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

