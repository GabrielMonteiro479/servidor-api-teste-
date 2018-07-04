from flask import jsonify, send_file, request
from app import app
from app.dao.servidor_dao import Servidor_dao
from app.models import Serializer
from app.builder.servidor_builder import servidor_builder


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


@app.route('/servidores/matricula/<matricula>', methods=['GET'])
def servidor_matricula(matricula):
    servidor = Servidor_dao().servidor_matricula(matricula)


    if servidor:
        return jsonify(servidor.serialize()), 200
    else:
        return "Not Found", 404

@app.route('/servidores/matriculaSiape/<matriculaSiape>', methods=['GET'])
def servidor_matricula_siape(matriculaSiape):
    servidor = Servidor_dao().servidor_matricula_siape(matriculaSiape)

    if servidor:
        return jsonify(servidor.serialize()), 200
    else:
        return "Not Found", 404

@app.route('/servidores/cpf/<cpf>', methods=['GET'])
def servidor_cpf(cpf):
    servidor = Servidor_dao().servidor_cpf(cpf)

    if servidor:
        return jsonify(servidor.serialize()), 200
    else:
        return "Not Found", 404

@app.route('/servidores/nome/<nome>', methods=['GET'])
def servidores_nome(nome):
    servidores = Servidor_dao().servidores_nome(nome)

    if servidores:
        return jsonify(Serializer.serialize_list(servidores)), 200
    else:
        return "Not Found", 404

@app.route('/servidores/atualizacao/<matricula>', methods = ['PUT'])
def atualiza (matricula):
    data = request.get_json() if request.is_json else request.form.to_dict()
    data.update({'matricula': matricula})

    servidor = servidor_builder.build(data)

    data_saved = Servidor_dao.atualiza(servidor)
    return jsonify(data_saved.serialize())



