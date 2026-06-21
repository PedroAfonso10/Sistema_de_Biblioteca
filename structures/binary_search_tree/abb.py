from structures.binary_search_tree.node import Node

class ArvoreBinariaBusca:
    def __init__(self):
        self.raiz = None

    def inserir(self, dado):
        if self.raiz is None:
            self.raiz = Node(dado)
        else:
            self._inserir_recursivo(dado, self.raiz)
    
    def _inserir_recursivo(self, dado, no):
        # Ordem alfabética: Letra posterior -> Direita
        if dado.get_nome().lower() >= no.dado.get_nome().lower():
            if no.direita is None:
                no.direita = Node(dado)
            else:
                self._inserir_recursivo(dado, no.direita)
        # Ordem alfabética: Letra anterior -> esquerda 
        else:
            if no.esquerda is None:
                no.esquerda = Node(dado)
            else:
                self._inserir_recursivo(dado, no.esquerda) 

    def remover(self, nome, alvo):    
        self._dado_removido = None

        if self.raiz != None:
            self.raiz = self._remover_recursivo(nome.lower(), alvo, self.raiz)
        
        return self._dado_removido

    def _remover_recursivo(self, nome, alvo, no):
        if no is None:
            return None

        # Encontra ALVO e remove
        if nome == no.dado.get_nome().lower() and alvo == no.dado.get_id():
            # Guarda o dado que vai ser removido
            if self._dado_removido is None:
                self._dado_removido = no.dado

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
            no.dado = substituto.dado
            # Remove o nó original
            no.direita = self._remover_recursivo(substituto.dado.get_nome().lower(), substituto.dado.get_id(), no.direita)
        else:
            if nome < no.dado.get_nome().lower():
                no.esquerda = self._remover_recursivo(nome, alvo, no.esquerda)
            else:
                no.direita = self._remover_recursivo(nome, alvo, no.direita)

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
        
        nomes_ordenados = []
        self._mostrar_em_ordem_recursivo(self.raiz, nomes_ordenados)
        return nomes_ordenados
        
    def _mostrar_em_ordem_recursivo(self, no, lista):
        if no is not None:
            self._mostrar_em_ordem_recursivo(no.esquerda, lista)
            lista.append(no.dado)
            self._mostrar_em_ordem_recursivo(no.direita, lista)