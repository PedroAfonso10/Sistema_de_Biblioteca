from repository.emprestimo_repository import emprestimo_repository_global
from repository.usuario_repository import usuario_repository_global
from repository.livros_repository import livro_repository_global
from exceptions.validator import Validator
from exceptions.exceptions import UsuarioNaoEncontradoError, LivroNaoEncontradoError, LivroIndisponivelError, EmprestimosNaoRealizados, EmprestimoNaoEncontradoError, DevolucaoIndisponivelError
from models.emprestimo import Emprestimo

class EmprestimoService:
    def __init__(self):
        self.emprestimo_repository = emprestimo_repository_global
        self.usuario_repository = usuario_repository_global
        self.livro_repository = livro_repository_global
        self.validator_emprestimo = Validator()

    def listar_emprestimos(self):
        emprestimos_realizados = self.emprestimo_repository.listar_emprestimos()
        if not emprestimos_realizados:
            raise EmprestimosNaoRealizados("Não há empréstimos cadastrados no sistema.")
        
        return emprestimos_realizados

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
            self.emprestimo_repository.enfileirar_fila_de_espera(matricula, isbn)
            raise LivroIndisponivelError("Livro indisponível no momento. Inserido na fila de espera")
        
        livro.qtd_exemplares -= 1

        emprestimo = Emprestimo(matricula, isbn)
        return self.emprestimo_repository.emprestar(emprestimo)
    
    def devolucao(self, id_emprestimo):
        emprestimo = self.emprestimo_repository.devolucao(id_emprestimo)

        if not emprestimo:
            raise EmprestimoNaoEncontradoError("Empréstimo não localizado.")
        
        if emprestimo.data_devolucao is not None:
            raise DevolucaoIndisponivelError("Devolução já realizada.") 
        
        # Registra o momento da devolução
        emprestimo.registrar_devolucao()

        # Busca o livro guardado no empréstimo
        livro = self.livro_repository.buscar_isbn(emprestimo.isbn_livro)
        if livro:
            novo_emprestimo = self.emprestimo_repository.desenfileirar_espera(livro.isbn)       
            
            if novo_emprestimo:
                # Se tem alguém na fila, repassa o livro
                novo_emprestimo = Emprestimo(novo_emprestimo, livro.isbn)
                self.emprestimo_repository.emprestar(novo_emprestimo)
            else:
                # Volta para 'qtd_exemplares' se não tiver ninguém na fila
                livro.qtd_exemplares += 1
        
        return emprestimo

    def desfazer_ultimo_emprestimo(self):
        ultimo_emprestimo = self.emprestimo_repository.desfazer_ultimo_emprestimo()
        
        if not ultimo_emprestimo:
            raise Exception("Não há empréstimos recentes para desfazer.")
            
        # Desenvolve o livro
        livro = self.livro_repository.buscar_isbn(ultimo_emprestimo.isbn_livro)
        if livro:
            livro.qtd_exemplares += 1
            
        return ultimo_emprestimo
    
    def relatorio_acervo(self):
        todos_livros = self.livro_repository.listar_livros()
        if not todos_livros:
            raise LivroNaoEncontradoError("Livros não encontrados no sistema.")
        
        relatorio = []
        for livro in todos_livros:
            # Busca a fila do livro atual na fila de espera
            fila = self.emprestimo_repository.ht_filas_espera.buscar(livro.isbn)

            usuarios_fila = fila.dados if fila else []
            tamanho_fila = len(usuarios_fila)
            
            relatorio.append({
                "titulo": livro.titulo,
                "autor": livro.autor,
                "ano_publicacao": livro.ano_publicacao,
                "isbn": livro.isbn,
                "exemplares_disponiveis": livro.qtd_exemplares,
                "total_na_fila": tamanho_fila,
                "matriculas_na_fila": usuarios_fila,
                "status": "Disponível" if livro.qtd_exemplares > 0 else "Esgotado"
            })
            
        return relatorio