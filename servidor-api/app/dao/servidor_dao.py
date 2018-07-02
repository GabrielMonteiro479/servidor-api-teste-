from app.models.servidor import Servidor


class Servidor_dao(object):

    
    def lista_servidor(self):
        return Servidor.query.order_by(Servidor.nome).all()

    def servidor_matricula(self, matricula):
        return Servidor.query.get(matricula)

    def servidor_matricula_siape(self, matriculaSiape):
        return Servidor.query.filter(Servidor.matriculaSiape == matriculaSiape).first()
        #return Servidor.query.filter(Servidor.matriculaSiape == matriculaSiape).first()

    def servidor_cpf(self, cpf):	
    	return Servidor.query.filter(Servidor.cpf == cpf).first()
    	#return Servidor.query.filter_by(cpf = cpf).first()
    