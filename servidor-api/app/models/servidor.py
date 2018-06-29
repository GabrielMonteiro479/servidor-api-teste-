from app import db
from app.models.Serializer import Serializer

#talvez tenha que acrescentar algo
class Servidor(db.Model, Serializer):
  
   __tablename__ =  'SERVIDOR' 
   
   matricula = db.Column('MAT_SERVIDOR', db.String(8), primary_key=True, nullable = False) #primary key
   matriculaSiape = db.Column('MAT_SIAPE', db.String(8)) 
   nome = db.Column('NOM', db.String(60), nullable = False)
   nomeAnterior= db.Column('NOM_ANT_SERV', db.String(60)) 
   cpf = db.Column('NUM_CPF', db.String(11), nullable = False)
   dataNascimento = db.Column('DT_NASC', db.Date, nullable = False)
   sexo = db.Column('SEXO', db.String(1), nullable = False)
   eMail = db.Column('E_MAIL', db.String(50)) 
   telefone = db.Column('TELEFONE', db.String(25)) 
   naturalidade = db.Column('NATURALIDADE', db.String(35), nullable = False)
   nacionalidade = db.Column('NACIONALIDADE', db.Integer)#, db.Foreignkey('SERVIDOR.NACIONALIDADE'))
   cargo = db.Column('CARGO', db.Integer)#, db.Foreignkey('SERVIDOR.CARGO'))
   situacaoFuncional = db.Column('CD_SI_FUNC', db.Integer)#, db.Foreignkey('SERVIDOR.CD_SI_FUNC')) 

def __repr__(self):
        return '<Servidor %s>' % self.nome
