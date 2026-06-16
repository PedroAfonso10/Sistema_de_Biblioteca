from structures.linked_list.linkedlist import LinkedList
from structures.binary_search_tree.abb import ArvoreBinariaBusca
from structures.hash_table.hashtable import HashTable

class LivroRepository: 
    def __init__(self):
        self.linked_list = LinkedList()
        self.abb = ArvoreBinariaBusca()
        self.ht = HashTable()

    def create_livro(self, livro):
        self.linked_list.inserir(livro)
        self.abb.inserir(livro)
        self.ht.inserir(livro)
        return livro

    def buscar_isbn(self, isbn):
        return self.ht.buscar(isbn)