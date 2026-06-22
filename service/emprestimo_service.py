from repository.emprestimo_repository import emprestimo_repository_global
from repository.usuario_repository import usuario_repository_global
from repository.livros_repository import livro_repository_global
from exceptions.validator import Validator
from exceptions.exceptions import UsuarioNaoEncontradoError, LivroNaoEncontradoError, LivroIndisponivelError
from models.emprestimo import Emprestimo

class EmprestimoService:
    def __init__(self):
        self.emprestimo_repository = emprestimo_repository_global
        self.usuario_repository = usuario_repository_global
        self.livro_repository = livro_repository_global
        self.validator_emprestimo = Validator()

    def emprestar(self, matricula: str, isbn: str):
        matricula = self.validator_emprestimo.validar_matricula(matricula)
        isbn = self.validator_emprestimo.validar_isbn(isbn)

        usuario = self.usuario_repository.buscar_usuario(matricula)
        if not usuario:
            raise UsuarioNaoEncontradoError("Usuário não cadastrado. Cadastra-se para realizar empréstimos de livros")
        
        livro = self.livro_repository.buscar_isbn(isbn)
        if not livro:
            raise LivroNaoEncontradoError("ISBN do livro não cadastrado")

        if livro.qtd_exemplares <= 0:
            raise LivroIndisponivelError("Livro indisponível no momento.")
        
        livro.qtd_exemplares -= 1

        emprestimo = Emprestimo(matricula, isbn)
        return self.emprestimo_repository.emprestar(emprestimo)
