from app.models.servidor import Servidor


class Servidor_dao(object):

    #modificar de acordo com a db
    def lista_servidor(self):
        return Servidor.query.order_by(Servidor.nome).all()

    def servidor_matricula(self, matricula):
        return Servidor.query.get(Servidor.matricula)

    def servidor_matricula_siape(self, matriculaSiape):
        return Servidor.query.get(Servidor.matriculaSiape)

    def servidor_cpf(self, cpf):
        return Servidor.query.get(Servidor.cpf)
