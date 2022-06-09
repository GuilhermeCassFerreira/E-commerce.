from entidade.pessoa import Pessoa

class Adm(Pessoa):

    def __init__(self, nome:str, cpf: str, telefone: str, endereco: str, email: str, senha: str, salario: str):
        super().__init__(nome, cpf, telefone, endereco, email, senha)
        self.__salario = salario

    @property
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(self, salario: float):
        self.__salario = salario