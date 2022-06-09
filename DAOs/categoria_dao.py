from DAOs.dao import DAO
from entidade.categoria import Categoria

#cada entidade terá uma classe dessa, implementação bem simples.
class CategoriaDAO(DAO):
    def __init__(self):
        super().__init__('categorias.pkl')

    def add(self, categoria: Categoria):
        if((categoria is not None) and isinstance(categoria, Categoria) and isinstance(categoria.tipo, str)):
            super().add(categoria.tipo, categoria)

    def update(self, categoria: Categoria):
        if((categoria is not None) and isinstance(categoria, Categoria) and isinstance(categoria.tipo, str)):
            super().update(categoria.tipo, categoria)

    def get(self, key:str):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key:str):
        if(isinstance(key, str)):
            return super().remove(key)