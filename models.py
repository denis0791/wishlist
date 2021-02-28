import flask_sqlalchemy

db = flask_sqlalchemy.SQLAlchemy()


class Produto(db.Model):
    __tablename__ = 'produto'
    id = db.Column(db.Integer, primary_key=True)
    titulo_do_produto = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.String(100), nullable=True)
    link = db.Column(db.String(500), nullable=True)
    foto = db.Column(db.LargeBinary, nullable=True)
    ganhou = db.Column(db.String(3), nullable=True)
    comprou = db.Column(db.String(3), nullable=True)
