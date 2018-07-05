from flask import jsonify, send_file
from app import app
from app.dao.agencia_dao import Agencia_dao
from app.models import Serializer


@app.route('/')
def index():
    return "API de Agências"

@app.route('/swagger')
def swagger_api():
    return send_file('static/swagger.yml', mimetype='yml', as_attachment=False, cache_timeout=0)

@app.route('/health')
def health():
    status = {
        "status": "UP"
    }
    return jsonify(status)


@app.route('/agencias/', methods=['GET'])
def lista_agencia():
    agencias = Agencia_dao().lista_agencia()

    if agencias:
        return jsonify(Serializer.serialize_list(agencias)), 200
    else:
        return "Not Found", 404

@app.route('/agencias/<codigo>', methods=['GET'])
def agencia_codigo(codigo):
    agencia = Agencia_dao().agencia_codigo(codigo)

    if agencia:
        return jsonify(agencia.serialize()), 200
    else:
        return "Not Found", 404

@app.route('/agencias/banco/<codigo>', methods=['GET'])
def agencia_codigo_banco(codigo):
    agencias = Agencia_dao().agencia_codigo_banco(codigo)

    if agencias:
        return jsonify(Serializer.serialize_list(agencias)), 200
    else:
        return "Not Found", 404
