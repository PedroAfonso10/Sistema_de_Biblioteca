from structures.linked_list.linkedlist import LinkedList
from structures.hash_table.hashtable import HashTable
from structures.queue.queue import Fila

class EmprestimoRepository:
    def __init__(self):
        self.linkedlist_emprestimo = LinkedList()
        self.ht_emprestimo = HashTable()
        self.ht_filas_espera = HashTable()

    def listar_emprestimos(self):
        return self.linkedlist_emprestimo.listar()

    def emprestar(self, emprestimo):
        self.linkedlist_emprestimo.inserir(emprestimo)
        self.ht_emprestimo.inserir(emprestimo)
        return emprestimo
    
    def devolucao(self, id_emprestimo):
        emprestimo = self.ht_emprestimo.buscar(id_emprestimo)
        return emprestimo
    
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