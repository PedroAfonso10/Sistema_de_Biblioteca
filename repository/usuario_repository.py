from structures.linked_list.linkedlist import LinkedList
from structures.binary_search_tree.abb import ArvoreBinariaBusca
from structures.hash_table.hashtable import HashTable

class UsuarioRepository:
    def __init__(self):
        self.linkedlist_usuario = LinkedList()
        self.abb_usuario = ArvoreBinariaBusca()
        self.ht_usuario = HashTable()

    def cadastrar_usuario(self, usuario):
        self.linkedlist_usuario.inserir(usuario)
        self.abb_usuario.inserir(usuario)
        self.ht_usuario.inserir(usuario)
        return usuario
    
    def buscar_usuario(self, matricula):
        return self.ht_usuario.buscar(matricula)