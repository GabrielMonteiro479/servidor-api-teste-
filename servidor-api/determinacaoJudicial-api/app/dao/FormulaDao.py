from app import db
from app.models.Formula import Formula


class FormulaDao(object):

	def buscar_formula(formula):
		return Formula.query.filter(Formula.codigo == formula.codigo, Formula.codigo_liminar == formula.codigo_liminar).first()

	@staticmethod
	def incluir_relacao(formula):
		exists = FormulaDao.buscar_formula(formula)
		
		if not exists:
			db.session.add(formula)
			db.session.commit()

		return exists

