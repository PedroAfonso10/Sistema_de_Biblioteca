from service.emprestimo_service import EmprestimoService
from exceptions.exceptions import FormatoInvalidoError, CampoVazioError, TipoDadoIncorretoError, UsuarioNaoEncontradoError, LivroNaoEncontradoError, EmprestimosNaoRealizados
from flask import request, jsonify

class EmprestimoController:
    def __init__(self):
        self.emprestimo_service = EmprestimoService()

    def listar_emprestimos(self):
        try:
            emprestimos_realizados = self.emprestimo_service.listar_emprestimos()
            return jsonify([self._to_response(emprestimo) for emprestimo in emprestimos_realizados]), 200
        
        except EmprestimosNaoRealizados as e:
            return jsonify({"erro": str(e)}), 404
        
        except Exception as e:
            return jsonify({"erro": "Falha no servidor"}), 500

    def emprestar(self):
        dados = request.get_json()

        try:
            dados_emprestimo = self.emprestimo_service.emprestar(
                matricula=dados["matricula"],
                isbn=dados["isbn"]
            )
            return jsonify(self._to_response(dados_emprestimo)), 201    
        
        except (CampoVazioError, FormatoInvalidoError, TipoDadoIncorretoError) as e:
            return jsonify({"erro": str(e)}), 422
        
        except (UsuarioNaoEncontradoError, LivroNaoEncontradoError)  as e:
            return jsonify({"erro": str(e)}), 404
        

    def _to_response(self, dados_emprestimo):
        formato_data = "%d/%m/%Y %H:%M:%S"
        return {
            "matricula": dados_emprestimo.matricula_usuario,
            "isbn": dados_emprestimo.isbn_livro,
            "id_emprestimo": dados_emprestimo.id_emprestimo,
            "data_inicio": dados_emprestimo.data_inicio.strftime(formato_data),
            "data_limite_entrega": dados_emprestimo.data_limite_entrega.strftime(formato_data),
            "data_devolucao": dados_emprestimo.data_devolucao.strftime(formato_data) if dados_emprestimo.data_devolucao else None,
            "status": dados_emprestimo.status_atrasado
        }   