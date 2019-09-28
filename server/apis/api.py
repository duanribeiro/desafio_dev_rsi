from flask import Blueprint, jsonify, request
import pandas as pd
import json
from pymongo import MongoClient

api = Blueprint('blueprint', __name__)

client = MongoClient("mongodb+srv://duanribeiro:BJ183r32@futebol-iwbwh.mongodb.net/test?retryWrites=true&w=majority")
db = client.futebol

@api.route('/', methods=['GET', 'POST'])
def helathcheck():
    return "Funcionando", 200

@api.route('/1', methods=['GET', 'POST'])
def insert():
    db.usuarios.insert_one({"1":"1"})
    return "Funcionando", 201