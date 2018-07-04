from app.models.servidor import Servidor
from datetime import datetime

class servidor_builder(object):

	DATE_FORMAT = '%Y-%m-%d'
	@staticmethod

	def build(data):
		servidor = Servidor()
		servidor.matricula = data.get('matricula')
		servidor.matriculaSiape = data.get('matriculaSiape')
		servidor.nome  = data.get('nome')
		servidor.nomeAnterior = data.get('nomeAnterior')
		servidor.cpf = data.get('cpf')
		servidor.dataNascimento = data.get('dataNascimento')
		servidor.sexo = data.get('sexo')
		servidor.eMail = data.get('eMail')
		servidor.telefone = data.get('telefone')
		servidor.naturalidade = data.get('naturalidade')
		servidor.nacionalidade = data.get('nacionalidade')
		servidor.cargo = data.get('cargo')
		servidor.situacaoFuncional = data.get('situacaoFuncional')

		if data.get('dataNascimento'):
			dataNascimento = datetime.strptime(data.get('dataNascimento'), servidor_builder.DATE_FORMAT)
			servidor.dataNascimento = dataNascimento

		return servidor
