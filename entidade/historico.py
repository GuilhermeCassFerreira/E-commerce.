from entidade.produto import Produto
from entidade.usuario import Usuario


class Historico:
    def __init__(self, usuario, produto):
        if isinstance(usuario, Usuario):
            self.__usuario =  usuario
        if isinstance(produto, Produto):
            self.__produto = produto

    @property
    def usuario(self):
        return self.__usuario

    @property
    def produto(self):
        return self.__produto

    @usuario.setter
    def usuario(self, usuario):
        if isinstance(usuario, Usuario):
            self.__usuario =  usuario

    @produto.setter
    def produto(self, produto):
        if isinstance(produto, Produto):
            self.__produto = produto

    def __eq__(self, other):
        if self.__produto == other.produto:
            return True
        else:
            return