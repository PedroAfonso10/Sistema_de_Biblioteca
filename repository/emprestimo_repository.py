from structures.linked_list.linkedlist import LinkedList
from structures.hash_table.hashtable import HashTable

class EmprestimoRepository:
    def __init__(self):
        self.linkedlist_emprestimo = LinkedList()
        self.ht_emprestimo = HashTable()

    def emprestar(self, emprestimo):
        self.linkedlist_emprestimo.inserir(emprestimo)
        self.ht_emprestimo.inserir(emprestimo)
        return emprestimo

emprestimo_repository_global = EmprestimoRepository()