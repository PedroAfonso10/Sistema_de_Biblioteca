from repository.livros_repository import livro_repository_global
from exceptions.validator import Validator
from exceptions.exceptions import FormatoInvalidoError, LivroNaoEncontradoError, LivroDuplicadoError, ArvoreVazia
from models.livro import Livro
from datetime import datetime

class LivroService:
    def __init__(self):
        self.livro_repository = livro_repository_global
        self.validator_service = Validator()

    def buscar_livro_isbn(self, isbn: str):
        self.validator_service.validar_isbn(isbn)
        livro  = self.livro_repository.buscar_isbn(isbn)
        if not livro:
            raise LivroNaoEncontradoError('ISBN não cadastrado')
        
        return livro

    def listar_livros(self):
        livros_ordenados = self.livro_repository.listar_livros()
        
        if not livros_ordenados:
            raise ArvoreVazia("Não há nenhum livro cadastrado na árvore")
        
        return livros_ordenados

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

        return self.livro_repository.cadastrar_livro(livro)
    
    def deletar_livro(self, isbn: str):
        self.validator_service.validar_isbn(isbn)
        livro = self.buscar_livro_isbn(isbn)
        
        # Remove o livro e o retorna, ou retorna None se não existir
        livro_removido = self.livro_repository.deletar_livro(livro)

        return livro_removido   