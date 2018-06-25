from app import db
from app.models.Serializer import Serializer

#talvez tenha que acrescentar algo
class Servidor(db.Model, Serializer):
  
   __tablename__ =  'SERVIDOR' 
   
   matricula = db.Column('MAT_SERVIDOR', db.Integer, primary_key=True)
   matriculaSiape = db.Column('MAT_SIAPE', db.Integer)
   nome = db.Column('NOME', db.String(60))
   nomeAnterior= db.Column('NOME_ANTERIOR', db.String(60)) #FK?
   cpf = db.Column('CPF', db.String(11))
   dataNascimento = db.Column('DT_NASC', db.Date)
   sexo = db.Column('SEXO', db.String(1))
   eMail = db.Column('E_MAIL', db.String(50)) #FK?
   telefone = db.Column('TELEFONE', db.String(25)) #FK?
   naturalidade = db.Column('NATURALIDADE', db.String(35))
   nacionalidade = db.Column('NACIONALIDADE', db.Integer) #FK? MELHOR CANDIDATO PARA FK
   cargo = db.Column('CARGO', db.Integer) #MELHOR CANDIDATO PARA FK
   situacaoFuncional = db.Column('SITUACAO_FUNC', db.String(20)) #MELHOR CANDIDATO PARA FK

def __repr__(self):
        return '<Servidor %s>' % self.nome
