
class Pessoa():
    
    def __init__(self, nome:str, cpf: str, telefone:str, endereco: str, email: str, senha: str):
        self.__nome = nome
        self.__cpf = cpf
        self.__telefone = telefone
        self.__endereco = endereco
        self.__email = email
        self.__senha = senha
    
    @property
    def nome(self):
        return self.__nome

    @property
    def cpf(self):
        return self.__cpf
    
    @property
    def telefone(self):
        return self.__telefone

    @property
    def endereco(self):
        return self.__endereco

    @property
    def email(self):
        return self.__email

    @property
    def senha(self):
        return self.__senha
    
    @nome.setter
    def nome(self, nome:str):
        self.__nome = nome

    @cpf.setter
    def cpf(self, cpf:str):
        self.__cpf = cpf

    @telefone.setter
    def telefone(self, telefone:str):
        self.__telefone = telefone

    @endereco.setter
    def endereco(self, endereco:str):
        self.__endereco = endereco

    @email.setter
    def email(self, email:str):
        self.__email = email
    
    @senha.setter
    def senha(self, senha: str):
        self.__senha = senha



