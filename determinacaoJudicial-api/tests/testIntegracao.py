from tests import DBTestCase, FlaskTestCase

from app.models.Formula import Formula


class TestesIntegracao(FlaskTestCase):

    other_schemas = ['FOLHA']
    fixtures = ['pensao.yaml', 'formula.yaml', 'determinacao_judicial.yaml']
    
    def test_health(self):
        resp = self.client.get("/health")
        self.assert200(resp)
        self.assertEqual(resp.json, dict(status="UP"))

    def test_list_all(self):
        resp = self.client.get("/determinacaoJudicial/")
        self.assert200(resp)
        self.assertEqual(len(resp.json), 2)

    def test_get_one(self):
        resp = self.client.get("/determinacaoJudicial/2")
        self.assert200(resp)
        self.assertEqual(resp.json['codigo'], 2)
        self.assertEqual(resp.json['descricao'], "Decisão Liminar Dois")

    def test_get_by_dependente(self):
        resp = self.client.get("/determinacaoJudicial/dependente/1865")
        self.assert200(resp)
        self.assertEqual(resp.json['codigo'], 1)
        self.assertEqual(resp.json['descricao'], "Decisão Liminar Um")
        deps = []
        for p in resp.json['pensoes']:
            deps.append(p['codigo_dependente'])
        self.assertTrue(deps.index(1865) != 0)

    def test_get_by_servidor(self):
        resp = self.client.get("/determinacaoJudicial/servidor/2366")
        self.assert200(resp)
        self.assertEqual(resp.json['codigo'], 1)
        self.assertEqual(resp.json['descricao'], "Decisão Liminar Um")
        for p in resp.json['pensoes']:
            self.assertEqual(p['matricula_servidor'], "2366")
    
    def test_incluir(self):
        pass

    def test_alterar(self):
        pass


class TestFormula(DBTestCase):

    other_schemas = ['FOLHA']
    fixtures = ['pensao.yaml', 'formula.yaml', 'determinacao_judicial.yaml']

    def test_list_all(self):
        formulas = Formula.query.all()
        self.assertEqual(len(formulas), 2)

    def test_get_one(self):
        formula = Formula.query.get((1866, 1))
        self.assertEqual(formula.codigo, 1866)
        self.assertEqual(formula.codigo_liminar, 1)
