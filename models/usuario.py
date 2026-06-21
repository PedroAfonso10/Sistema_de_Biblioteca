from structures.linked_list.linkedlist import LinkedList

class Usuario:
    def __init__(self, nome: str, curso: str, matricula: str):
        self.nome = nome
        self.curso = curso
        self.matricula = matricula
        self.livros_emprestados = LinkedList()  
    
    def get_id(self):
        return self.matricula
    
    def get_nome(self):
        return self.nome