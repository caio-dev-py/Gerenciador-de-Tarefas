from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

class Usuarios(db.Model, UserMixin):
    __tablename__ = "usuarios"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), nullable=False, unique=True)
    senha = db.Column(db.String(), nullable=False)
    status = db.Column(db.String(), default="ativo")
    role = db.Column(db.String(4), default="user")
    db.relationship("Tarefas", backref="usuario", lazy=True)
    
class Tarefas(db.Model, UserMixin):
    __tablename__ = "tarefas"
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey("usuarios.id"), nullable=False)
    titulo = db.Column(db.String(150), nullable=False)
    descricao = db.Column(db.String(1000), nullable=False)