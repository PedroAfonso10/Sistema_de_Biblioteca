from service.livros_service import LivroService
from exceptions.exceptions import CampoVazioError, TipoDadoIncorretoError, FormatoInvalidoError, LivroNaoEncontradoError, LivroDuplicadoError
from flask import request, jsonify

class LivroController:
    def __init__(self):
        self.livro_service = LivroService()

    def buscar_livro(self, isbn):
        try:
            livro = self.livro_service.buscar_livro_isbn(isbn)
            return jsonify(self._to_response(livro)), 200
            
        except (CampoVazioError, TipoDadoIncorretoError, FormatoInvalidoError) as e:
            return jsonify({"erro": str(e)}), 422

        except LivroNaoEncontradoError as e:
            return jsonify({"erro": str(e)}), 404

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

        except (CampoVazioError, TipoDadoIncorretoError, FormatoInvalidoError) as e:
            return jsonify({"erro": str(e)}), 422
        
        except LivroDuplicadoError as e:
            return jsonify({"erro": str(e)}), 409
        
    def deletar_livro(self, isbn):
        try:
            livro = self.livro_service.deletar_livro(isbn)
            return jsonify(self._to_response(livro)), 200
        
        except (CampoVazioError, FormatoInvalidoError, TipoDadoIncorretoError) as e:
            return jsonify({"erro": str(e)}), 422
        
        except LivroNaoEncontradoError as e:
            return jsonify({"erro": str(e)}), 404

    def _to_response(self, livro):
        return {
            "isbn": livro.isbn,
            "titulo": livro.titulo,
            "autor": livro.autor,
            "ano_publicacao": livro.ano_publicacao,
            "qtd_exemplares": livro.qtd_exemplares
        }