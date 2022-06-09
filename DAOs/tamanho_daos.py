from DAOs.dao import DAO
from entidade.tamanho import Tamanho

#cada entidade terá uma classe dessa, implementação bem simples.
class TamanhoDAO(DAO):
    def __init__(self):
        super().__init__('tamanhos.pkl')

    def add(self, tamanho: Tamanho):
        if((tamanho is not None) and isinstance(tamanho, Tamanho) and isinstance(tamanho.descricao, str)):
            super().add(tamanho.descricao, tamanho)

    def update(self, tamanho: Tamanho):
        if((tamanho is not None) and isinstance(tamanho, Tamanho) and isinstance(tamanho.descricao, str)):
            super().update(tamanho.descricao, tamanho)

    def get(self, key:str):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key:str):
        if(isinstance(key, str)):
            return super().remove(key)