class Tamanho:
    def __init__(self,descricao:str):
        self.__descricao = descricao

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self,descricao:str):
        self.__descricao = descricao
