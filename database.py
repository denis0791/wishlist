from .models import db
from sqlalchemy.sql.expression import func


def get_all(model):
    data = model.query.all()
    return data


def add_instance(model, **kwargs):
    instance = model(**kwargs)
    db.session.add(instance)
    commit_changes()


def delete_instance(model, id):
    model.query.filter_by(id=id).delete()
    commit_changes()


def edit_instance(model, id, **kwargs):
    instance = model.query.filter_by(id=id).all()[0]
    for attr, new_value in kwargs.items():
        setattr(instance, attr, new_value)
    commit_changes()


def get_random_item(model):
    data = model.query.order_by(func.random()).limit(1).all()
    return data


def commit_changes():
    db.session.commit()
