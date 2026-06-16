class HashTable:

    def __init__(self, tamanho=10):
        self.tamanho = tamanho
        # Cria um vetor de listas vazias para o encadeamento (chaining)
        self.tabela = [[] for _ in range(tamanho)]

    def _hash_func(self, isbn):
        # Converte para int se for uma string númerica
        isbn_num = int(str(isbn).replace('-', ''))
        return isbn_num % self.tamanho

    def inserir(self, livro):
        indice = self._hash_func(livro.isbn)
        self.tabela[indice].append((livro.isbn, livro))
    
    def buscar(self, isbn):
        # Calcula o índice baseado no ISBN
        indice = self._hash_func(isbn)
        
        # Percorre a lista de colisões neste índice
        for item_isbn, item_livro in self.tabela[indice]:
            if item_isbn == isbn:
                return item_livro  # Retorna o objeto se achar