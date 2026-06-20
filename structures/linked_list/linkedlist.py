from structures.linked_list.node import Node

class LinkedList:
    def __init__(self):
        self.head = None

    def inserir(self, livro):
        novo_livro = Node(livro)

        if self.head is None:
            self.head = novo_livro
            return

        livro_atual = self.head

        # Percorre até o último nó
        while livro_atual.next is not None:
            livro_atual = livro_atual.next

        # Insere o Livro no fim
        livro_atual.next = novo_livro

    def remover(self, isbn):
        if self.head is None:
            return None
        
        # Remove se estiver na primeira posição
        if self.head.livro.isbn == isbn:
            # Guarda o livro que vai ser removido 
            livro_removido = self.head.livro

            # A cabeça aponta para o próximo nó
            self.head = self.head.next
            return livro_removido 
        
        livro_anterior = self.head
        livro_atual = self.head.next
        
        # Percorre até encontrar o ISBN
        while livro_atual is not None:
            if livro_atual.livro.isbn == isbn:
                livro_removido = livro_atual.livro

                # Pula o atual e referencia o próximo
                livro_anterior.next = livro_atual.next
                return livro_removido

            livro_anterior = livro_atual
            livro_atual = livro_atual.next
    
        return None