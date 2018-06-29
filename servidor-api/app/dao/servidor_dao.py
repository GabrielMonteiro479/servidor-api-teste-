from app.models.servidor import Servidor


class Servidor_dao(object):

    
    def lista_servidor(self):
        return Servidor.query.order_by(Servidor.nome).all()

    def servidor_matricula(self, matricula):
        return Servidor.query.get(matricula) #get funciona apenas para primary key

    def servidor_matricula_siape(self, matriculaSiape):
        return Servidor.query.get(matriculaSiape)

    def servidor_cpf(self, cpf):
    	return Servidor.query.having(Servidor.cpf==cpf) #ver na documentacao http://docs.sqlalchemy.org/en/latest/orm/query.html qual metodo usar
        #return Servidor.query.get(cpf)
