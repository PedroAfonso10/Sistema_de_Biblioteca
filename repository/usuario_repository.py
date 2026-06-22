from structures.linked_list.linkedlist import LinkedList
from structures.binary_search_tree.abb import ArvoreBinariaBusca
from structures.hash_table.hashtable import HashTable

class UsuarioRepository:
    def __init__(self):
        self.linkedlist_usuario = LinkedList()
        self.abb_usuario = ArvoreBinariaBusca()
        self.ht_usuario = HashTable()

    def listar_usuarios(self):
        return self.abb_usuario.mostrar_em_ordem()

    def buscar_usuario(self, matricula):
        return self.ht_usuario.buscar(matricula)

    def cadastrar_usuario(self, usuario):
        self.linkedlist_usuario.inserir(usuario)
        self.abb_usuario.inserir(usuario)
        self.ht_usuario.inserir(usuario)
        return usuario
    
    def deletar_usuario(self, usuario):
        usuario_removido = self.linkedlist_usuario.remover(usuario.matricula)
        self.abb_usuario.remover(usuario.nome, usuario.matricula)
        self.ht_usuario.remover(usuario.matricula)
        return usuario_removido

usuario_repository_global = UsuarioRepository()