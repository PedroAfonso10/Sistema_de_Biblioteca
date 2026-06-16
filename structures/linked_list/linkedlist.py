from structures.linked_list.node import Node

class LinkedList:
    def __init__(self):
        self.head = None

    def inserir(self, valor):
        novo = Node(valor)
        
        if self.head is None:
            self.head = novo
            return

        atual = self.head
        # Percorre até o último nó
        while atual.next is not None:
            atual = atual.next

        # Insere o elemento no fim
        atual.next = novo
