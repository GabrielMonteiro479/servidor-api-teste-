from app.models.servidor import Servidor
from app import db


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

    def servidores_nome(self, nome):
    	return Servidor.query.filter(Servidor.nome.like("%" + nome.upper() + "%")).order_by(Servidor.nome).all()


    def atualiza(servidor):
    	serv = Servidor_dao.buscar_matricula(servidor.matricula)

    	if not serv: #Caso não encontra
    		raise Exception('Não foi possível encontrar o servidor portador da matrícula %s' % (data.matricula))

    	servidor.matricula = serv.matricula
    	servidor = db.session.merge(servidor)
    	db.session.commit()

    	return servidor

    def buscar_matricula(matricula):
    	return Servidor.query.get(matricula)


