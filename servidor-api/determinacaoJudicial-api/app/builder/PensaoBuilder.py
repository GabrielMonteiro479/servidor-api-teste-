from app.models.Pensao import Pensao


class PensaoBuilder(object):

    @staticmethod
    def build(dados):
        pensao = Pensao()

        pensao.codigo_dependente = dados['codigo_dependente']
        pensao.codigo_liminar = dados['codigo_liminar']
        pensao.matricula_servidor = dados['matricula_servidor']

        return pensao
