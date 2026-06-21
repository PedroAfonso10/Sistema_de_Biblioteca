from repository.usuario_repository import UsuarioRepository
from models.usuario import Usuario
from exceptions.validator import Validator
from exceptions.exceptions import  UsuarioDuplicadoError, UsuarioNaoEncontradoError, ArvoreVazia

class UsuarioService:
    def __init__(self):
        self.usuario_repository = UsuarioRepository()
        self.validator_service_usuario = Validator()
    
    def buscar_usuario(self, matricula: str):
        self.validator_service_usuario.validar_matricula(matricula)
        usuario  = self.usuario_repository.buscar_usuario(matricula)
        if not usuario:
            raise UsuarioNaoEncontradoError('Usuário não cadastrado')
            
        return usuario
    
    def listar_usuarios(self):
        usuarios_ordenados = self.usuario_repository.listar_usuarios()

        if not usuarios_ordenados:
            raise ArvoreVazia('Não há usuários na árvore')
        
        return usuarios_ordenados

    def cadastrar_usuario(self, nome: str, curso: str, matricula: str):
        self.validator_service_usuario.validar_autor(nome)
        self.validator_service_usuario.validar_string(curso) 

        matricula = self.validator_service_usuario.validar_matricula(matricula)
        if self.usuario_repository.buscar_usuario(matricula):
            raise UsuarioDuplicadoError("Usuário já cadastrado")
        
        usuario = Usuario(nome, curso, matricula)

        return self.usuario_repository.cadastrar_usuario(usuario)
    
    def deletar_usuario(self, matricula: str):
        self.validator_service_usuario.validar_matricula(matricula)
        usuario = self.usuario_repository.buscar_usuario(matricula)

        if not usuario:
            raise UsuarioNaoEncontradoError('Usuário não encontrado')
        
        usuario_removido = self.usuario_repository.deletar_usuario(usuario)
        
        return usuario_removido