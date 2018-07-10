from sqlalchemy.orm import foreign
from sqlalchemy.schema import Sequence
from app import db
from app.models.Serializer import Serializer
from app.models.Pensao import Pensao
from app.models.Formula import Formula


class DeterminacaoJudicial(db.Model, Serializer):
    __tablename__ = 'FL_LIMINAR'
    __table_args__ = {"schema": "FOLHA"}

    codigo = db.Column('cod_lim_judicial', db.Integer, Sequence('SQ_CD_LIMINAR', schema='FOLHA'), primary_key=True)
    descricao = db.Column('desc_lim_judicial', db.String(100))
    data = db.Column('dt_lim_judicial', db.Date)
    data_validade = db.Column('dt_validade', db.Date)
    numero_mandado = db.Column('nr_mandado', db.String(30))
    tipo = db.Column('tipo_liminar', db.String(1))
    folhas_incidencia = db.Column('folhas_incidencia', db.String(1))
    numero_folha = db.Column('num_folha', db.String(1))
    mes_ano_folha = db.Column('mes_ano_folha', db.String(6))
    percentual = db.Column('perc_pa', db.Float)

    pensoes = db.relationship(Pensao, primaryjoin=codigo == foreign(Pensao.codigo_liminar), lazy=False)
    formulas = db.relationship(Formula, primaryjoin=codigo == foreign(Formula.codigo_liminar), lazy=False,
                                cascade="all, delete-orphan")

    def __repr__(self):
        return '<DeterminacaoJudicial %s>' % self.descricao
