from app import db
from app.models.Serializer import Serializer

class Agencia(db.Model, Serializer):
   __tablename__ =  'TAB_AGE'
   codigo = db.Column('CD', db.String(5), primary_key=True)
   descricao = db.Column('DS', db.String(50))
   cod_banco = db.Column('CD_BCO', db.String(3))

def __repr__(self):
        return '<Agencia %s>' % self.descricao
