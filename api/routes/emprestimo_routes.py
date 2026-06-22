from api.controller.emprestimo_controller import EmprestimoController
from flask import Blueprint

emprestimo_controller = EmprestimoController()

bp_emprestimo = Blueprint("emprestimos", __name__)

@bp_emprestimo.route("/emprestimos", methods=['GET'])
def listar_emprestimos():
    return emprestimo_controller.listar_emprestimos()

@bp_emprestimo.route("/emprestimos", methods=['POST'])
def emprestar():
    return emprestimo_controller.emprestar()

@bp_emprestimo.route("/emprestimos/<string:id_emprestimo>/devolucao", methods=['PUT'])
def devolucao(id_emprestimo):
    return emprestimo_controller.devolucao(id_emprestimo)