class HashTable:
    def __init__(self, tamanho=10):
        self.tamanho = tamanho
        # Cria um vetor de listas vazias para o encadeamento (chaining)
        self.tabela = [[] for _ in range(tamanho)]

    def _hash_func(self, chave):
        # Converte para int se for uma string númerica
        dado_num = int(str(chave).replace('-', ''))
        return dado_num % self.tamanho

    def inserir(self, dado):
        chave = dado.get_id()
        indice = self._hash_func(chave)
        self.tabela[indice].append((chave, dado))
    
    def remover(self, chave):
        # Remove o item baseado na chave (ISBN ou MATRICULA)
        indice = self._hash_func(chave)
        # Percorre em busca da chave
        for i, (ch, valor) in enumerate(self.tabela[indice]):
            if ch == chave:
                # Remove o item encontrado da lista de colisões e o retorna
                return self.tabela[indice].pop(i)[1]

    def buscar(self, chave):
        # Calcula o índice baseado no ID(ISBN ou MATRICULA)
        indice = self._hash_func(chave)
        
        # Percorre a lista de colisões neste índice
        for ch, valor in self.tabela[indice]:
            if ch == chave:
                return valor  # Retorna o objeto se achar