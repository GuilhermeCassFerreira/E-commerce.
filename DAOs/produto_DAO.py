from DAOs.dao import DAO
from entidade.categoria import Categoria
from entidade.cor import Cor
from entidade.produto import Produto
from entidade.tamanho import Tamanho

#cada entidade terá uma classe dessa, implementação bem simples.
class ProdutoDAO(DAO):
    def __init__(self):
        super().__init__('produtos.pkl')

    def add(self, produto: Produto):
        if((produto is not None) and isinstance(produto, Produto) and isinstance(produto.cor, Cor) and isinstance(produto.categoria, Categoria) and isinstance(produto.tamanho, Tamanho) and isinstance(produto.codigo, int)):
            super().add(produto.codigo, produto)

    def update(self, produto: Produto):
        if((produto is not None) and isinstance(produto, Produto) and isinstance(produto.cor, Cor) and isinstance(produto.categoria, Categoria) and isinstance(produto.tamanho, Tamanho) and isinstance(produto.codigo, int)):
            super().update(produto.codigo, produto)

    def get(self, key:int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key:int):
        if(isinstance(key, int)):
            return super().remove(key)