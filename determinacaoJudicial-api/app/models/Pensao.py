from sqlalchemy.orm import foreign
from sqlalchemy import func
from sqlalchemy.schema import Sequence
from app import db
from app.models.Serializer import Serializer


class Pensao(db.Model, Serializer):
    __tablename__ = 'FL_PENS_X_LIMINAR'
    __table_args__ = {"schema": "FOLHA"}

    codigo_dependente = db.Column('COD_DEPEND', db.Integer, primary_key=True)
    codigo_liminar = db.Column('COD_LIM_JUDICIAL', db.Integer, primary_key=True)
    matricula_servidor = db.Column('MAT_SERVIDOR', db.String(8), primary_key=True)

    def __repr__(self):
        return '<Pensao %d - %d>' % (self.codigo_dependente, self.codigo_liminar)
