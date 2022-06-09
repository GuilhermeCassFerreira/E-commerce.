from entidade.pessoa import Pessoa

class Usuario(Pessoa):

    def __init__(self, nome:str, cpf: str, telefone: str, endereco: str, email: str, senha: str):
        super().__init__(nome, cpf, telefone, endereco, email, senha)
        self.__historico_compra = list

    @property
    def historico_compra(self):
        return  self.__historico_compra

    @historico_compra.setter
    def historico_compra(self, historico_compra: list):
        self.__historico_compra = list