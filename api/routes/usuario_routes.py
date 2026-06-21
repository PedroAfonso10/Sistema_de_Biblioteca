from api.controller.usuario_controller import UsuarioController
from flask import Blueprint

usuario_controller = UsuarioController()

bp_usuario = Blueprint("usuarios", __name__)

@bp_usuario.route("/usuarios", methods=['GET'])
def listar_usuarios():
    return usuario_controller.listar_usuarios()

@bp_usuario.route("/usuarios/<string:matricula>", methods=['GET'])
def obter_usuario(matricula: str):
    return usuario_controller.buscar_usuario(matricula)

@bp_usuario.route("/usuarios", methods=['POST']) 
def cadastrar_usuario():
    return usuario_controller.cadastrar_usuario()

@bp_usuario.route("/usuarios/<string:matricula>", methods=['DELETE'])
def deletar_usuario(matricula: str):
    return usuario_controller.deletar_usuario(matricula)