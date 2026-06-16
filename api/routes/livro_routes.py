from api.controller.livro_controller import LivroController
from flask import Blueprint

livro_controller = LivroController()

bp = Blueprint("livros", __name__)

@bp.route("/livros", methods=['POST'])
def cadastrar_livro():
    return livro_controller.cadastrar_livro()