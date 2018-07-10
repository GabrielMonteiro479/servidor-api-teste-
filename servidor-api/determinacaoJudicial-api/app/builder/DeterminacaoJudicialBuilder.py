from datetime import datetime
from app.models.DeterminacaoJudicial import DeterminacaoJudicial


class DeterminacaoJudicialBuilder(object):

    @staticmethod
    def build(dados):
        determinacao = DeterminacaoJudicial()

        determinacao.codigo = dados.get('codigo')
        determinacao.descricao = dados['descricao']
        determinacao.data = datetime.strptime(dados['data'], '%Y-%m-%d')
        if dados.get('data_validade'):
            determinacao.data_validade = datetime.strptime(dados.get('data_validade'), '%Y-%m-%d')
        determinacao.tipo = dados['tipo']
        determinacao.folhas_incidencia = dados['folhas_incidencia']
        determinacao.numero_mandado = dados.get('numero_mandado')
        determinacao.numero_folha = dados.get('numero_folha')
        determinacao.mes_ano_folha = dados.get('mes_ano_folha')
        determinacao.percentual = dados.get('percentual')

        return determinacao
