from datetime import datetime
from tests import UnitTestCase
from app.builder.DeterminacaoJudicialBuilder import DeterminacaoJudicialBuilder


class DeterminacaoJudicialBuilderTestes(UnitTestCase):
    def test_builder_completo(self):
        dados = dict(codigo=1, descricao='Determinacao Judicial', data='2018-01-30', 
                     data_validade='2019-12-31', tipo='J', folhas_incidencia='T',
                     numero_mandado='123', numero_folha='1', mes_ano_folha='122018', percentual=3.14)

        model = DeterminacaoJudicialBuilder.build(dados)

        self.assertEqual(model.codigo, dados['codigo'])
        self.assertEqual(model.data, datetime.strptime(dados['data'], '%Y-%m-%d'))
        self.assertEqual(model.data_validade, datetime.strptime(dados['data_validade'], '%Y-%m-%d'))
        self.assertEqual(model.tipo, dados['tipo'])
        self.assertEqual(model.folhas_incidencia, dados['folhas_incidencia'])
        self.assertEqual(model.numero_mandado, dados['numero_mandado'])
        self.assertEqual(model.numero_folha, dados['numero_folha'])
        self.assertEqual(model.mes_ano_folha, dados['mes_ano_folha'])
        self.assertEqual(model.percentual, dados['percentual'])

    def test_builder_obrigatorios(self):
        obrigatorios = ['descricao', 'data', 'tipo', 'folhas_incidencia']
        dados = dict(descricao='desc', data='2018-01-30', tipo='J', folhas_incidencia='T')

        for o in obrigatorios:
            dados_test = dados.copy()  # copia dict original
            dados_test.pop(o)          # remove um campo obrigatório
            try:
                DeterminacaoJudicialBuilder.build(dados_test)
            except KeyError as e:
                causa = str(e).replace('\'', '')
                if causa == o:        # verifica se o erro é por causa do campo removido
                    pass
                else: 
                    self.fail("%s é obrigatório" % o)
