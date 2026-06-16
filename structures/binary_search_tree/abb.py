from structures.binary_search_tree.node import Node

class ArvoreBinariaBusca:
    def __init__(self):
        self.raiz = None


    def inserir(self, livro):
        if self.raiz is None:
            self.raiz = Node(livro)
        else:
            self._inserir_recursivo(livro, self.raiz)
    

    def _inserir_recursivo(self, livro, no):
        # Valor maior -> Direita
        if livro.titulo.lower() >= no.livro.titulo.lower():
            if no.direita is None:
                no.direita = Node(livro)
            else:
                self._inserir_recursivo(livro, no.direita)
        # Valor menor -> esquerda 
        else:
            if no.esquerda is None:
                no.esquerda = Node(livro)
            else:
                self._inserir_recursivo(livro, no.esquerda)