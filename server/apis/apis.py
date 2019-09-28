from flask import Flask


app = Flask(__name__)

@app.route("/usuario/login", methods="POST")
def usuario_login():

@app.route("/usuario/logout", methods="GET")
def usuario_logout():

@app.route("/conta", methods="POST")
def conta():

@app.route("/conta/adicionarSaldo", methods="POST")
def conta_adicionarSaldo():

@app.route("/conta/{id}", methods=["DELETE", "GET"])
def conta_id():

@app.route("/extrato", methods="POST")
def