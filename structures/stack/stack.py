class Pilha:
    def __init__(self):
        self.dados = []

    def empilhar(self, dado):
        # Adiciona no topo da pilha
        self.dados.append(dado)
    
    def desempilhar(self):
        if len(self.dados) == 0:
            return None
        
        # Guarda o último elemento
        topo = self.dados[-1]
        # Cria uma nova lista sem o último
        self.dados = self.dados[:-1]

        return topo