from flask import jsonify, request, render_template, send_file
from app.builder.DeterminacaoJudicialBuilder import DeterminacaoJudicialBuilder
from app.builder.PensaoBuilder import PensaoBuilder
from app.builder.FormulaBuilder import FormulaBuilder
from app.dao.DeterminacaoJudicialDao import DeterminacaoJudicialDao
from app.dao.PensaoDao import PensaoDao
from app.dao.FormulaDao import FormulaDao
from app.models import Serializer
from app import app


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/swagger')
def swagger_api():
    return send_file('static/swagger.yml', mimetype='yml', as_attachment=False, cache_timeout=0)


@app.route('/health')
def health():
    status = {
        "status": "UP"
    }
    return jsonify(status)


@app.route('/determinacaoJudicial/', methods=['GET'])
def listar_todos():
    determinacoes = DeterminacaoJudicialDao.listar_todos()

    return jsonify(Serializer.serialize_list(determinacoes))


@app.route('/determinacaoJudicial/<int:codigo>', methods=['GET'])
def recuperar_por_cd(codigo):
    determinacao = DeterminacaoJudicialDao.get_por_codigo(codigo)

    if determinacao:
        return jsonify(determinacao.serialize())
    else:
        return "Not Found", 404


@app.route('/determinacaoJudicial/<int:codigo>/dependente', methods=['POST'])
def vincular_dependente(codigo):
    dados = request.json if request.is_json else request.form.to_dict()
    dados.update({'codigo_liminar': codigo})

    pensao = PensaoBuilder.build(dados)

    salvo = PensaoDao.incluir(pensao)

    return jsonify(salvo.serialize())


@app.route('/determinacaoJudicial/dependente/<int:codigo>', methods=['GET'])
def recuperar_por_dependente(codigo):
    determinacao = DeterminacaoJudicialDao.get_por_dependente(codigo)

    if determinacao:
        return jsonify(determinacao.serialize())
    else:
        return "Not Found", 404


@app.route('/determinacaoJudicial/servidor/<matricula>', methods=['GET'])
def recuperar_por_servidor(matricula):
    determinacao = DeterminacaoJudicialDao.get_por_servidor(matricula)

    if determinacao:
        return jsonify(determinacao.serialize())
    else:
        return "Not Found", 404


@app.route('/determinacaoJudicial/', methods=['POST'])
def incluir_determinacao():
    dados = request.json if request.is_json else request.form.to_dict()
    dados.update({'codigo': None})

    determinacao = DeterminacaoJudicialBuilder.build(dados)
    
    determinacao = DeterminacaoJudicialDao.incluir(determinacao)

    return jsonify(determinacao.serialize()) if determinacao.codigo else None


@app.route('/determinacaoJudicial/<int:codigo>', methods=['PUT'])
def alterar(codigo):
    dados = request.json if request.is_json else request.form.to_dict()
    dados.update({'codigo': codigo})

    determinacao = DeterminacaoJudicialBuilder.build(dados)
    
    determinacao = DeterminacaoJudicialDao.alterar(determinacao)

    return jsonify(determinacao.serialize())

@app.route('/formulaxLiminar/', methods=['POST'])
def incluir_relacao():
    dados = request.json if request.is_json else request.form.to_dict()

    formula = FormulaBuilder.build(dados)

    if formula.codigo == '' or formula.codigo_liminar == '':
        return "Bad Request", 400

    else:
        exists = FormulaDao.incluir_relacao(formula)

        if not exists: #ja existe o dado na tabela
            return jsonify(formula.serialize())
        else:
            return "Conflict", 409

