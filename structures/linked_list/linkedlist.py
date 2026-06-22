from structures.linked_list.node import Node

class LinkedList:
    """
    Armazena qualquer objeto (Livros, Usuários, etc.). Utiliza o polimorfismo através do método 'get_id()' dos objetos contidos
    para realizar operações de busca e remoção. 
    """
    def __init__(self):
        self.head = None

    def inserir(self, dado):
        novo_dado = Node(dado)

        if self.head is None:
            self.head = novo_dado
            return

        dado_atual = self.head

        # Percorre até o último nó
        while dado_atual.next is not None:
            dado_atual = dado_atual.next

        # Insere o dado no fim
        dado_atual.next = novo_dado

    def remover(self, alvo):
        if self.head is None:
            return None
        
        # Remove se estiver na primeira posição
        if self.head.dado.get_id() == alvo:
            # Guarda o dado que vai ser removido 
            dado_removido = self.head.dado

            # A cabeça aponta para o próximo nó
            self.head = self.head.next
            return dado_removido 
        
        dado_anterior = self.head
        dado_atual = self.head.next

        # Percorre até encontrar o ISBN
        while dado_atual is not None:
            if dado_atual.dado.get_id() == alvo:
                dado_removido = dado_atual.dado

                # Pula o atual e referencia o próximo
                dado_anterior.next = dado_atual.next
                return dado_removido

            dado_anterior = dado_atual
            dado_atual = dado_atual.next
    
        return None
    
    def listar(self):
        if self.head is None:
            return []
            
        elementos = [] 
        dado_atual = self.head
        
        # Percorre todos os nós até o fim da lista encadeada
        while dado_atual is not None:
            elementos.append(dado_atual.dado)
            dado_atual = dado_atual.next     
            
        return elementos