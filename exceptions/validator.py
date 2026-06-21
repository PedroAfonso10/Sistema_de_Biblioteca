import re
from exceptions.exceptions import CampoVazioError, FormatoInvalidoError, TipoDadoIncorretoError

class Validator:
    def validar_entrada_numerica(self, valor):
        # Garante existência de valor no campo
        if valor is None:
            raise CampoVazioError('Campo não está preenchido')
        
        # Garante que o valor seja do tipo int
        if not isinstance(valor, int):
            raise TipoDadoIncorretoError('O campo deve ser preenchido com número inteiro')
    

    def validar_string(self, string):
        # Garante existência de string no campo
        if string is None:
            raise CampoVazioError('Campo não está preenchido')
        
        # Garante que a string seja do tipo str
        if not isinstance(string, str):
            raise TipoDadoIncorretoError('O campo deve ser preenchido com string')
        
        # Garante que o campo não seja preenchido com espaços 
        if string.strip() == "":
            raise CampoVazioError('O campo não está preenchido com caracteres válidos')
    

    def validar_isbn(self, string):
        self.validar_string(string)

        # Remove espaços extras no início, fim e espaços duplos
        string = " ".join(string.split())

        # Expressão Regular para o formato do ISBN
        # ISBN-10: Ex: 85-359-0277-5 ou 8535902775
        # ISBN-13: Ex: 978-85-359-0277-7 ou 9788535902777
        formato = r"^(?:97[89][- ]?)?(?:\d[- ]?){9}[\dxX]$"

        # Verifica se o ISBN é válido
        if not re.fullmatch(formato, string):
            raise FormatoInvalidoError("Formato de ISBN inválido. Use o padrão de 10 ou 13 dígitos.")

        return string


    def validar_autor(self, string):
        self.validar_string(string)

        string = " ".join(string.split()) 

        formato = r"^[A-Za-zÀ-ÿ]+(?:[ .'\-][A-Za-zÀ-ÿ]+)*$"

        if not re.fullmatch(formato, string):
            raise ValueError("Nome do autor inválido")
        
        return string
        

    def validar_titulo(self, string):
        self.validar_string(string)

        string = " ".join(string.split())

        formato = r"^[A-Za-zÀ-ÿ0-9\s\-\:\,\.'\"!\?]+$"

        if not re.fullmatch(formato, string):
            raise ValueError("Título inválido")

        return string
    
    def validar_matricula(self, string):
        self.validar_string(string)

        string = " ".join(string.split())

        # Expressão Regular para o formato da MATRICULA
        # Ano atual/recente (4 dígitos) + Sequencial (4 dígitos) -> 8 dígitos numéricos puros
        formato = r"^\d{4}\d{4}$"

        if not re.fullmatch(formato, string):
            raise FormatoInvalidoError(
                "Formato de matrícula inválido.")

        return string