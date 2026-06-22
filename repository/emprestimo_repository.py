from structures.linked_list.linkedlist import LinkedList
from structures.hash_table.hashtable import HashTable
from structures.queue.queue import Fila
from structures.stack.stack import Pilha

class EmprestimoRepository:
    def __init__(self):
        self.linkedlist_emprestimo = LinkedList()
        self.ht_emprestimo = HashTable()
        self.ht_filas_espera = HashTable()
        self.pilha_desfazer = Pilha()

    def listar_emprestimos(self):
        return self.linkedlist_emprestimo.listar()
    
    def relatorio_acervo(self):
        return self.linkedlist_emprestimo.listar()

    def emprestar(self, emprestimo):
        self.linkedlist_emprestimo.inserir(emprestimo)
        self.ht_emprestimo.inserir(emprestimo)
        # Guarda histórico
        self.pilha_desfazer.empilhar(emprestimo)
        return emprestimo
    
    def devolucao(self, id_emprestimo):
        emprestimo = self.ht_emprestimo.buscar(id_emprestimo)
        return emprestimo
    
    def desfazer_ultimo_emprestimo(self): 
        # Remove o último empréstimo
        ultimo_emprestimo = self.pilha_desfazer.desempilhar()
        
        if ultimo_emprestimo is None:
            return None
            
        self.ht_emprestimo.remover(ultimo_emprestimo.id_emprestimo)
        self.linkedlist_emprestimo.remover(ultimo_emprestimo.id_emprestimo)
        
        return ultimo_emprestimo

    def enfileirar_fila_de_espera(self, matricula, isbn):
        # Busca a Fila correspondente
        fila = self.ht_filas_espera.buscar(isbn)

        if fila is None:
            fila = Fila(isbn)
            self.ht_filas_espera.inserir(fila)

        # Insere na fila
        fila.enfileirar(matricula)

    def desenfileirar_espera(self, isbn):
        # Busca a Fila do livro
        fila = self.ht_filas_espera.buscar(isbn)
        # Verifica se existe Fila
        if fila is None:
            return None 
        
        # Remove primeiro da fila
        return fila.desenfileirar()

emprestimo_repository_global = EmprestimoRepository()