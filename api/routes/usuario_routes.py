from api.controller.usuario_controller import UsuarioController
from flask import Blueprint

usuario_controller = UsuarioController()

bp_usuario = Blueprint("usuarios", __name__)

@bp_usuario.route("/usuarios", methods=['POST']) 
def cadastrar_usuario():
    return usuario_controller.cadastrar_usuario()