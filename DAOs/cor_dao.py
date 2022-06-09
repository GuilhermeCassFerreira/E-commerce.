from DAOs.dao import DAO
from entidade.cor import Cor

#cada entidade terá uma classe dessa, implementação bem simples.
class CorDAO(DAO):
    def __init__(self):
        super().__init__('cores.pkl')

    def add(self, cor: Cor):
        if((cor is not None) and isinstance(cor, Cor) and isinstance(cor.nome, str)):
            super().add(cor.nome, cor)

    def update(self, cor: Cor):
        if((cor is not None) and isinstance(cor, Cor) and isinstance(cor.nome, str)):
            super().update(cor.nome, cor)

    def get(self, key:str):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key:str):
        if(isinstance(key, str)):
            return super().remove(key)