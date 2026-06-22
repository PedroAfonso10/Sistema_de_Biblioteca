from datetime import datetime, timedelta
import random 

class Emprestimo:
    def __init__(self, matricula_usuario: str, isbn_livro: str):
        self.matricula_usuario = matricula_usuario
        self.isbn_livro = isbn_livro
        self.id_emprestimo = str(random.randint(1000000000, 9999999999))
        self.data_inicio = datetime.now()
        self.data_limite_entrega = self.data_inicio + timedelta(minutes=2)
        self.data_devolucao = None
    
    @property
    def status_atrasado(self) -> bool:
        # Calcula dinamicamente se o empréstimo está atrasado ou não
        data_fim = self.data_limite_entrega
        if self.data_devolucao:
            return self.data_devolucao > data_fim
        return datetime.now() > data_fim

    def registrar_devolucao(self):
        self.data_devolucao = datetime.now()
    
    def get_id(self):
        return self.id_emprestimo
