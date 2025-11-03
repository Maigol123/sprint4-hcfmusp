from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Consulta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    paciente = db.Column(db.String(100))
    data = db.Column(db.String(10))
    medico = db.Column(db.String(100))
    especialidade = db.Column(db.String(100))
    link = db.Column(db.String(255))
    horario = db.Column(db.String(10))
    local = db.Column(db.String(200))
    observacoes = db.Column(db.String(500))
    data_cadastro = db.Column(db.String(20))

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class Parente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    telefone = db.Column(db.String(20))
    parentesco = db.Column(db.String(50))
    email = db.Column(db.String(100))

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class Lembrete(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100))
    mensagem = db.Column(db.String(500))
    data = db.Column(db.String(10))
    horario = db.Column(db.String(10))
    enviado = db.Column(db.Boolean, default=False)

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
