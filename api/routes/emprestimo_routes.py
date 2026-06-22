from api.controller.emprestimo_controller import EmprestimoController
from flask import Blueprint

emprestimo_controller = EmprestimoController()

bp_emprestimo = Blueprint("emprestimos", __name__)

@bp_emprestimo.route("/emprestimos", methods=['POST'])
def emprestar():
    return emprestimo_controller.emprestar()