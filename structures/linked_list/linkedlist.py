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

        # Insere o elemento no fim
        livro_atual.next = novo_livro