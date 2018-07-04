from tests import DBTestCase, FlaskTestCase

from app.dao.servidor_dao import Servidor_dao


class TestesIntegracao(FlaskTestCase):

    fixtures = ['servidor.yaml']
    
    def test_health(self):
        resp = self.client.get("/health")
        self.assert200(resp)
        self.assertEqual(resp.json, dict(status="UP"))

    
    def test_list_all(self):
        resp = self.client.get("/servidores/")
        self.assert200(resp)
        self.assertEqual(len(resp.json), 4)

    #?
    def test_get_one(self):
        resp = self.client.get("/servidores/2")
        self.assert200(resp)
        self.assertEqual(resp.json['codigo'], '2')
        self.assertEqual(resp.json['descricao'], "Agencia Dois")

    #?
    def test_get_by_banco(self):
        resp = self.client.get("/servidores/banco/2")
        self.assert200(resp)
        self.assertEqual(len(resp.json), 2)
        for p in resp.json:
            self.assertTrue(p['cod_banco'], '2')

    def test_incluir(self):
        pass

    def test_alterar(self):
        pass


class TestServidorDao(DBTestCase):

    fixtures = ['servidor.yaml']

    def test_list_all(self):
        servidores = Servidor_dao().lista_servidor()
        self.assertEqual(len(servidores), 4)

    
    def test_get_one(self):
        servidor = Servidor_dao().servidor_matricula(2)
        self.assertEqual(servidor.matricula, 3)
        self.assertEqual(servidor.matriculaSiape, 33)
        self.assertEqual(servidor.nome, 'Nome Tres')
        self.assertEqual(servidor.nomeAnterior, 'Nome Dois')
        self.assertEqual(servidor.cpf, '33333333333')
        self.assertEqual(servidor.dataNascimento, '2018-06-26') #nao sei se ta correto
        self.assertEqual(servidor.sexo, 'F')
        self.assertEqual(servidor.eMail, 'nometres@email.com')
        self.assertEqual(servidor.telefone, '61333333333')
        self.assertEqual(servidor.naturalidade, 'Rio de Janeiro')
        self.assertEqual(servidor.nacionalidade, 1)
        self.assertEqual(servidor.cargo, 3)
        self.assertEqual(servidor.situacaoFuncional, 'Situacao Tres')

    
    def test_get_por_matricula_siape(self):
        servidores = Servidor_dao().servidor_matricula_siape(2)
        self.assertEqual(len(servidor), 2)
        for s in servidores:
            self.assertEqual(s.matriculaSiape, 33)

    def test_get_por_cpf(self):
        servidores = Servidor_dao().servidor_cpf(2)
        self.assertEqual(len(servidor), 2)
        for s in servidores:
            self.assertEqual(s.cpf, 3)
