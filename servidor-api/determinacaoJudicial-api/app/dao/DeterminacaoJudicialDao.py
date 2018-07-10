from app.models.DeterminacaoJudicial import DeterminacaoJudicial
from app.models.Pensao import Pensao
from app import db


class DeterminacaoJudicialDao(object):

    @staticmethod
    def listar_todos():
        return DeterminacaoJudicial.query.all()

    @staticmethod
    def get_por_codigo(codigo):
        return DeterminacaoJudicial.query.get(codigo)

    @staticmethod
    def get_por_servidor(matricula):
        return DeterminacaoJudicial.query.join(Pensao,
                                               Pensao.codigo_liminar == DeterminacaoJudicial.codigo)\
            .filter(Pensao.matricula_servidor == matricula).first()
    
    @staticmethod
    def get_por_dependente(codigo):
        return DeterminacaoJudicial.query.join(Pensao,
                                               Pensao.codigo_liminar == DeterminacaoJudicial.codigo)\
            .filter(Pensao.codigo_dependente == codigo).first()

    @staticmethod
    def incluir(determinacao):
        db.session.add(determinacao)
        db.session.commit()

        return determinacao

    @staticmethod
    def alterar(determinacao):
        det = DeterminacaoJudicialDao.get_por_codigo(determinacao.codigo)

        if not det:  # Prevenindo que o registro seja inserido caso não exista
            raise Exception('Não foi possível encontrar a determinação de código %d' % determinacao.codigo)
        
        determinacao = db.session.merge(determinacao)
        db.session.commit()

        return determinacao
