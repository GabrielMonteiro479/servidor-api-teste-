from tests import DBTestCase, FlaskTestCase

from app.dao.agencia_dao import Agencia_dao


class TestesIntegracao(FlaskTestCase):

    fixtures = ['agencia.yaml']
    
    def test_health(self):
        resp = self.client.get("/health")
        self.assert200(resp)
        self.assertEqual(resp.json, dict(status="UP"))

    def test_list_all(self):
        resp = self.client.get("/agencias/")
        self.assert200(resp)
        self.assertEqual(len(resp.json), 4)

    def test_get_one(self):
        resp = self.client.get("/agencias/2")
        self.assert200(resp)
        self.assertEqual(resp.json['codigo'], '2')
        self.assertEqual(resp.json['descricao'], "Agencia Dois")

    def test_get_by_banco(self):
        resp = self.client.get("/agencias/banco/2")
        self.assert200(resp)
        self.assertEqual(len(resp.json), 2)
        for p in resp.json:
            self.assertTrue(p['cod_banco'], '2')

    def test_incluir(self):
        pass

    def test_alterar(self):
        pass


class TestAgenciaDao(DBTestCase):

    fixtures = ['agencia.yaml']

    def test_list_all(self):
        agencias = Agencia_dao().lista_agencia()
        self.assertEqual(len(agencias), 4)

    def test_get_one(self):
        agencia = Agencia_dao().agencia_codigo(2)
        self.assertEqual(agencia.codigo, '2')
        self.assertEqual(agencia.descricao, 'Agencia Dois')
        self.assertEqual(agencia.cod_banco, '1')

    def test_get_por_banco(self):
        agencias = Agencia_dao().agencia_codigo_banco(2)
        self.assertEqual(len(agencias), 2)
        for a in agencias:
            self.assertEqual(a.cod_banco, '2')
