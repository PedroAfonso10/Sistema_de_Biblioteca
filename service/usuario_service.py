from repository.usuario_repository import UsuarioRepository
from models.usuario import Usuario
from exceptions.validator import Validator
from exceptions.exceptions import CampoVazioError, FormatoInvalidoError, TipoDadoIncorretoError, UsuarioDuplicadoError, UsuarioNaoEncontradoError

class UsuarioService:
    def __init__(self):
        self.usuario_repository = UsuarioRepository()
        self.validator_service_usuario = Validator()

    def cadastrar_usuario(self, nome: str, curso: str, matricula: str):
        self.validator_service_usuario.validar_autor(nome)
        self.validator_service_usuario.validar_string(curso) 

        matricula = self.validator_service_usuario.validar_matricula(matricula)
        if self.usuario_repository.buscar_usuario(matricula):
            raise UsuarioDuplicadoError("Usuário já cadastrado")
        
        usuario = Usuario(nome, curso, matricula)

        return self.usuario_repository.cadastrar_usuario(usuario)