class Fila:
    def __init__(self, isbn: str):
        self.isbn = isbn 
        self.dados = []

    def enfileirar(self, dado:str):
        # Adiciona ao fim
        self.dados.append(dado)
    
    def desenfileirar(self):
        if len(self.dados) == 0:
            return None
            
        elemento_removido = self.dados[0]

        # Deslocamos todos os itens para a esquerda para "cobrir" o primeiro
        for i in range(len(self.dados) - 1):
            self.dados[i] = self.dados[i+1]
        # Remove a última posição que ficou duplicada após o deslocamento
        self.dados = self.dados[:-1]

        return elemento_removido
    
    # Hashtable usa o isbn para localizar
    def get_id(self):
        return self.isbn