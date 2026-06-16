from service.livros_service import LivroService
from flask import request, jsonify

class LivroController:
    def __init__(self):
        self.livro_service = LivroService()

    
    def cadastrar_livro(self):
        dados = request.get_json()

        try:
            livro = self.livro_service.cadastrar_livro(
                isbn=dados["isbn"],
                titulo=dados["titulo"],
                autor=dados["autor"],
                ano_publicacao=int(dados["ano_publicacao"]),
                qtd_exemplares=int(dados["qtd_exemplares"])
            )
            return jsonify(self._to_response(livro)), 201

        except ValueError as e:
            return jsonify({"erro": str(e)}), 400


    def _to_response(self, livro):
        return {
            "isbn": livro.isbn,
            "titulo": livro.titulo,
            "autor": livro.autor,
            "ano_publicacao": livro.ano_publicacao,
            "qtd_exemplares": livro.qtd_exemplares
        }