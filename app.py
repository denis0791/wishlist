import json

from flask import request

from . import create_app, database
from .models import Produto

app = create_app()


@app.route('/')
def principal():
    return "Lista de Desejos"


@app.route('/listar', methods=['GET'])
def listar():
    produtos = database.get_all(Produto)
    todos_produtos = []
    for produto in produtos:
        novo_produto = {
            "id": produto.id,
            "titulo": produto.titulo_do_produto,
            "descricao": produto.descricao,
            "link": produto.link,
            "foto": produto.foto,
            "ganhou": produto.ganhou,
            "comprou": produto.comprou
        }
        todos_produtos.append(novo_produto)

    return json.dumps(todos_produtos, indent=4), 200


@app.route('/item_aleatorio', methods=['GET'])
def item_aleatorio():
    produtos = database.get_random_item(Produto)
    for produto in produtos:
        novo_produto = {
            "id": produto.id,
            "titulo": produto.titulo_do_produto,
            "descricao": produto.descricao,
            "link": produto.link,
            "foto": produto.foto,
            "ganhou": produto.ganhou,
            "comprou": produto.comprou
        }

    return json.dumps(novo_produto, indent=4), 200


@app.route('/adicionar', methods=['POST'])
def adicionar():
    data = request.get_json()
    titulo_do_produto = data.get('titulo')

    if not titulo_do_produto:
        return json.dumps("titulo do produto não informado"), 400

    descricao = data.get('descricao')
    link = data.get('link')
    foto = data.get('foto')

    database.add_instance(Produto, titulo_do_produto=titulo_do_produto, descricao=descricao,
                          link=link, foto=foto)
    return json.dumps("Item adicionado"), 200


@app.route('/remover/<produto_id>', methods=['DELETE'])
def remover(produto_id):
    database.delete_instance(Produto, id=produto_id)
    return json.dumps("Item removido"), 200


@app.route('/editar/<produto_id>', methods=['PATCH'])
def editar(produto_id):
    data = request.get_json()
    ganhou = data.get('ganhou')
    comprou = data.get('comprou')
    database.edit_instance(Produto, id=produto_id, ganhou=ganhou, comprou=comprou)
    return json.dumps("Item editado"), 200
