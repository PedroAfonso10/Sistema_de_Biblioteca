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
        # Ordem alfabética: Letra posterior -> Direita
        if livro.titulo.lower().lower() >= no.livro.titulo.lower().lower():
            if no.direita is None:
                no.direita = Node(livro)
            else:
                self._inserir_recursivo(livro, no.direita)
        # Ordem alfabética: Letra anterior -> esquerda 
        else:
            if no.esquerda is None:
                no.esquerda = Node(livro)
            else:
                self._inserir_recursivo(livro, no.esquerda) 

    def remover(self, titulo, isbn):    
        self._livro_removido = None

        if self.raiz != None:
            self.raiz = self._remover_recursivo(titulo.lower(), isbn, self.raiz)
        
        return self._livro_removido

    def _remover_recursivo(self, titulo, isbn, no):
        if no is None:
            return None

        # Encontra ALVO e remove
        if titulo == no.livro.titulo.lower() and isbn == no.livro.isbn:
            # Guarda o livro que vai ser removido
            if self._livro_removido is None:
                self._livro_removido = no.livro

            # FOLHA
            if no.direita is None and no.esquerda is None:
                return None
            # Somente filho(s) a esquerda
            elif no.direita is None:
                return no.esquerda
            # Somente filho(s) a direita
            elif no.esquerda is None:
                return no.direita
            
            # Dois filhos: Escolhe o menor entre os maiores
            substituto = self._menor_elemento(no.direita)
            # Copia para o nó atual
            no.livro = substituto.livro
            # Remove o nó original
            no.direita = self._remover_recursivo(substituto.livro.titulo.lower(), substituto.livro.isbn, no.direita)
        else:
            if titulo < no.livro.titulo.lower():
                no.esquerda = self._remover_recursivo(titulo,isbn, no.esquerda)
            else:
                no.direita = self._remover_recursivo(titulo, isbn, no.direita)

        return no

    def _menor_elemento(self, no):
        if no is None:
            return None
        if no.esquerda is None:
            return no
        return self._menor_elemento(no.esquerda)
    
    def mostrar_em_ordem(self):
        if self.raiz is None:
            return []   
        
        livros_ordenados = []
        self._mostrar_em_ordem_recursivo(self.raiz, livros_ordenados)
        return livros_ordenados
        
    def _mostrar_em_ordem_recursivo(self, no, lista):
        if no is not None:
            self._mostrar_em_ordem_recursivo(no.esquerda, lista)
            lista.append(no.livro)
            self._mostrar_em_ordem_recursivo(no.direita, lista)