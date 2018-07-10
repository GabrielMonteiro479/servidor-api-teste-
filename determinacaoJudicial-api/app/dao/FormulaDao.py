from app import db


class FormulaDao(object):

    @staticmethod
    def incluir_relacao(formula):

    	exists = Servidor_dao.buscar_matricula(servidor.matricula)

    	if exits: #Caso ja existe
    		raise Exception('Não foi possível encontrar o servidor portador da matrícula %s' % (data.matricula))

        db.session.add(formula)
        db.session.commit()

        return formula