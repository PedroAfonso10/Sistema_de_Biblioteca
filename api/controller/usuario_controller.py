from service.usuario_service import UsuarioService
from exceptions.exceptions import CampoVazioError, FormatoInvalidoError, TipoDadoIncorretoError, UsuarioDuplicadoError, UsuarioNaoEncontradoError
from flask import request, jsonify

class UsuarioController:
    def __init__(self):
        self.usuario_service = UsuarioService()

    def cadastrar_usuario(self):
        dados_usuario = request.get_json()

        try:
            usuario = self.usuario_service.cadastrar_usuario(
                nome=dados_usuario["nome"],
                curso=dados_usuario["curso"],
                matricula=dados_usuario["matricula"]
            )

            return jsonify(self._to_response(usuario)), 201
        
        except (CampoVazioError, FormatoInvalidoError, TipoDadoIncorretoError, ValueError) as e:
            return jsonify({"erro": str(e)}), 422
        
        except UsuarioNaoEncontradoError as e:
            return jsonify({"erro": str(e)}), 404
        
        except UsuarioDuplicadoError as e:
            return jsonify({"erro": str(e)}), 409
    
    def _to_response(self, usuario):
        return {
            "nome": usuario.nome,
            "curso": usuario.curso,
            "matricula": usuario.matricula,
        }