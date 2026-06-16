from repository.livros_repository import LivroRepository
from exceptions.validator import Validator
from exceptions.exceptions import FormatoInvalidoError, LivroNaoEncontradoError, LivroDuplicadoError
from models.livro import Livro
from datetime import datetime

class LivroService:
    def __init__(self):
        self.livro_repository = LivroRepository()
        self.validator_service = Validator()

    def buscar_livro_isbn(self, isbn: str):
        self.validator_service.validar_isbn(isbn)
        livro  = self.livro_repository.buscar_isbn(isbn)
        if not livro:
            raise LivroNaoEncontradoError('ISBN não encontrado cadastrado')
        
        return livro


    def cadastrar_livro(self, isbn: str, titulo: str, autor: str, ano_publicacao: int, qtd_exemplares: int):
        # Valida ISBN
        self.validator_service.validar_isbn(isbn)
        if self.livro_repository.buscar_isbn(isbn):
            raise LivroDuplicadoError('ISBN já cadastrado')

        # Valida e garante formato do titulo
        titulo = self.validator_service.validar_titulo(titulo)

        # Valida e garante formato do nome
        autor = self.validator_service.validar_autor(autor)

        # Valida Ano de publicação
        self.validator_service.validar_entrada_numerica(ano_publicacao)
        ano_atual = datetime.now().year
        if ano_publicacao < 0 or  ano_publicacao > ano_atual:
            raise FormatoInvalidoError('Ano de publicação inválido')
        
        # Valida Quantidade de exemplares
        self.validator_service.validar_entrada_numerica(qtd_exemplares)
        if qtd_exemplares <= 0:
            raise FormatoInvalidoError('Quantidade de exemplares inválida')
        
        # Cria entidade 
        livro = Livro(isbn, titulo, autor, ano_publicacao, qtd_exemplares)

        return self.livro_repository.create_livro(livro)