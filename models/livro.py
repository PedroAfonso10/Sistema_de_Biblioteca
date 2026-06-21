class Livro:
    def __init__(self, isbn, titulo, autor, ano_publicacao, qtd_exemplares):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.qtd_exemplares = qtd_exemplares

    def get_id(self):
        return self.isbn
    
    def get_nome(self):
        return self.titulo