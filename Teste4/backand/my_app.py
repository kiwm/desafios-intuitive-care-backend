"""app"""
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

HOST = 'localhost'
USER_NAME = 'root'
PASSWORD = 'HYGy8xNh3#a$We'
DATABASE = 'appdb_intuitive_care'

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+mysqldb://{USER_NAME}:{PASSWORD}@{HOST}/{DATABASE}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)


if __name__ == "__main__":
    app.run(debug=True)

class Report(db.Model):
    id = db.Column(db.BIGINT, primary_key=True)
    Registro_ANS = db.Column(db.BIGINT) 
    CNPJ = db.Column(db.Text) 
    Razão_Social = db.Column(db.Text)
    Nome_Fantasia = db.Column(db.Text)
    Modalidade = db.Column(db.Text) 
    Logradouro = db.Column(db.Text) 
    Número = db.Column(db.Text) 
    Complemento = db.Column(db.Text) 
    Bairro = db.Column(db.Text) 
    Cidade = db.Column(db.Text) 
    UF = db.Column(db.Text) 
    CEP = db.Column(db.BIGINT)
    DDD = db.Column(db.Float)
    Telefone = db.Column(db.Text)
    Fax = db.Column(db.Float)
    Endereço_eletrônico = db.Column(db.Text) 
    Representante = db.Column(db.Text) 
    Cargo_Representante = db.Column(db.Text) 
    Data_Registro_ANS = db.Column(db.Text)

    def __init__(self, registro_ANS, cnpj, razao_social, nome_fantasia, modalidade, logradouro, numero, complemento, bairro, cidade, uf, cep, ddd, telefone, fax, endereço_eletronico, representante, cargo_representante, data_registro_ans):
        self.registro_ANS = registro_ANS
        self.cnpj = cnpj
        self.razao_social = razao_social
        self.nome_fantasia = nome_fantasia
        self.modalidade = modalidade
        self.logradouro = logradouro
        self.numero = numero
        self.complemento = complemento
        self.bairro = bairro
        self.cidade = cidade
        self.uf = uf
        self.cep = cep
        self.ddd = ddd
        self.telefone = telefone
        self.fax = fax
        self.endereço_eletronico = endereço_eletronico
        self.representante = representante
        self.cargo_representante = cargo_representante
        self.data_registro_ans = data_registro_ans

db.create_all()   
