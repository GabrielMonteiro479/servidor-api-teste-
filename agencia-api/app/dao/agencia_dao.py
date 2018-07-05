from app.models.agencia import Agencia


class Agencia_dao(object):

    def lista_agencia(self):
        return Agencia.query.order_by(Agencia.codigo).all()

    def agencia_codigo(self, codigo):
        return Agencia.query.get(codigo)

    def agencia_codigo_banco(self, codigo):
        return Agencia.query.filter(Agencia.cod_banco==codigo).all()
