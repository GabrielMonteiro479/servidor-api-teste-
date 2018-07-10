from app import db
from app.models.Serializer import Serializer


class Formula(db.Model, Serializer):
    __tablename__ = 'FL_FORM_ESP_X_LIMINAR'
    __table_args__ = {"schema": "FOLHA"}

    codigo = db.Column('COD_FORMULA', db.Integer, primary_key=True, autoincrement=False)
    codigo_liminar = db.Column('COD_LIM_JUDICIAL', db.Integer, primary_key=True, autoincrement=False)

    def __repr__(self):
        return '<Formula %d - %d>' % (self.codigo, self.codigo_liminar)