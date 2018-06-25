from flask import jsonify, send_file
from app import app
from app.dao.servidor_dao import Servidor_dao
from app.models import Serializer


@app.route('/')
def index():
    return "API de Servidores"

@app.route('/swagger')
def swagger_api():
    return send_file('static/swagger.yml', mimetype='yml', as_attachment=False, cache_timeout=0)

@app.route('/health')
def health():
    status = {
        "status": "UP"
    }
    return jsonify(status)


@app.route('/servidores/', methods=['GET'])
def lista_servidor():
    servidores = Servidor_dao().lista_servidor()

    if servidores:
        return jsonify(Serializer.serialize_list(servidores)), 200
    else:
        return "Not Found", 404


@app.route('/servidores/<matricula>', methods=['GET'])
def servidor_matricula(matricula):
    servidor = Servidor_dao().servidor_matricula(matricula)

    if servidor:
        return jsonify(servidor.serialize()), 200
    else:
        return "Not Found", 404

@app.route('/servidores/<matriculaSiape>', methods=['GET'])
def servidor_matricula_siape(matriculaSiape):
    servidores = Servidor_dao().servidor_matricula_siape(matriculaSiape)

    if servidores:
        return jsonify(Serializer.serialize_list(servidores)), 200
    else:
        return "Not Found", 404

@app.route('/servidores/<cpf>', methods=['GET'])
def servidor_cpf(cpf):
    servidor = Servidor_dao().servidor_cpf(cpf)

    if servidor:
        return jsonify(servidor.serialize()), 200
    else:
        return "Not Found", 404
