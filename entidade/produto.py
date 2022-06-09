from entidade.cor import Cor
from entidade.tamanho import Tamanho
from entidade.categoria import Categoria


class Produto:
  def __init__(self, cor: Cor, tamanho: Tamanho,categoria:Categoria, codigo: int):
    if (isinstance(cor, Cor)):
        self.__cor = cor
    if (isinstance(tamanho, Tamanho)):
        self.__tamanho = tamanho
    if (isinstance(categoria, Categoria)):
        self.__categoria = categoria
    self.__codigo = codigo

  @property
  def cor(self):
    return self.__cor

  @property
  def tamanho(self):
    return self.__tamanho

  @property
  def categoria(self):
    return self.__categoria

  @property
  def codigo(self):
    return self.__codigo

  @cor.setter
  def cor(self, cor: Cor):
    if (isinstance(cor, Cor)):
        self.__cor = cor

  @tamanho.setter
  def tamanho(self, tamanho: Tamanho):
    if (isinstance(tamanho, Tamanho)):
        self.__tamanho = tamanho

  @categoria.setter
  def categoria(self, categoria: Categoria):
    if (isinstance(categoria, Categoria)):
        self.__categoria = categoria


  @codigo.setter
  def codigo(self, codigo: int):
    self.__codigo = codigo

  def __eq__(self, other):
    if self.__cor == other.cor and self.__tamanho == other.tamanho and self.__categoria == other.categoria:
      return True
    else:
      return False
