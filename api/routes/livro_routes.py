from api.controller.livro_controller import LivroController
from flask import Blueprint

livro_controller = LivroController()

bp = Blueprint("livros", __name__)

@bp.route("/livros", methods=['GET'])
def listar_livros():
    return livro_controller.listar_livros()

@bp.route("/livros/<string:isbn>", methods=['GET'])
def obter_livro(isbn: str):
    return livro_controller.buscar_livro(isbn)

@bp.route("/livros", methods=['POST'])
def cadastrar_livro():
    return livro_controller.cadastrar_livro()

@bp.route("/livros/<string:isbn>", methods=['DELETE'])
def deletar_livro(isbn: str):
    return livro_controller.deletar_livro(isbn)