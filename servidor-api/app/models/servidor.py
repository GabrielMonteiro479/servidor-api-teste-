from app import db
from app.models.Serializer import Serializer

#talvez tenha que acrescentar algo
class Servidor(db.Model, Serializer):
  
   __tablename__ =  'SERVIDOR' #Ou 'SER', tem que olhar no codigo java
   
   matricula = db.Column('MAT_SERVIDOR', db.Integer, primary_key=True)
   matriculaSiape = db.Column('MAT_SIAPE', db.Integer)
   nome = db.Column('NOME', db.String(60))
   nomeAnterior= db.Column('NOME_ANTERIOR', db.String(60))
   cpf = db.Column('CPF', db.String(11))
   dataNascimento = db.Column('DT_NASC', db.Date)
   sexo = db.Column('SEXO', db.String(1))
   eMail = db.Column('E_MAIL', db.String(50))
   telefone = db.Column('TELEFONE', db.String(25))
   naturalidade = db.Column('NATURALIDADE', db.String(35))
   nacionalidade = db.Column('NACIONALIDADE', db.Integer)
   cargo = db.Column('CARGO', db.Integer)
   situacaoFuncional = db.Column('SITUACAO_FUNC', db.String(20))

def __repr__(self):
        return '<Servidor %s>' % self.nome
