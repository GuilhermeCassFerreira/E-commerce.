from DAOs.produto_DAO import ProdutoDAO
from controle.controlador_categorias import ControladorCategorias
from controle.controlador_cores import ControladorCores
from controle.controlador_tamanhos import ControladorTamanhos
from entidade.produto import Produto
from entidade.tamanho import Tamanho
from entidade.cor import Cor
from entidade.categoria import Categoria
from limite.tela_produto import TelaProduto
from limite.tela_abstrata import cabecalho
from limite.cadrasto import Cadastrado
from limite.ja_cadastrado import JaCadastrado
# Fazer lançamento e tratamento de exceções, ao invés de apenas mostrar mensagem na tela.


class ControladorProdutos():

    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__produtos = []
        self.__tela_produtos = TelaProduto()

    def retorna_lista_produtos(self):
        return self.__produtos

    def pega_produto_por_codigo(self, codigo: int):
        for produto in self.__produtos:
            if(produto.codigo == codigo):
                return produto
        return None

    def incluir_produto(self, adm):
        try:
            self.__controlador_sistema.controlador_cores.lista_cor()
            self.__controlador_sistema.controlador_tamanhos.lista_tamanho()
            self.__controlador_sistema.controlador_categorias.lista_categoria()
            dados_produto = self.__tela_produtos.pega_dados_produto()
            print(dados_produto)

            cor1 = self.valida_cor(dados_produto)
            tamanho1 = self.valida_tamanho(dados_produto)
            categoria1 = self.valida_categoria(dados_produto)
            
            if dados_produto == "Sair":
                self.__controlador_sistema.encerra_sistema()

            elif dados_produto == "Voltar":
                self.abre_tela_produtos_adm(adm)
            
            else:
                cor1 = self.valida_cor(dados_produto)
                tamanho1 = self.valida_tamanho(dados_produto)
                categoria1 = self.valida_categoria(dados_produto)

                for produto in self.__produtos:
                    if produto.cor == cor1 and produto.tamanho == tamanho1 and produto.categoria == categoria1:
                        self.__tela_produtos.mostra_mensagem(
                            "ATENCAO:O produto que você está tentando incluir já está na lista de produtos!")
                        return None
                self.__tela_produtos.mostra_mensagem(
                    "ATENCAO:O produto foi adicionado a lista de produtos!")
                codigo = len(self.__produtos) + 1
                novo_produto = Produto(cor1, tamanho1, categoria1, codigo)
                self.__produtos.append(novo_produto)
                return None

        except JaCadastrado as j:
            self.__tela_produtos.mostra_mensagem("Produto não foi" + str(j))
        except Cadastrado as i:
            self.__tela_produtos.mostra_mensagem("O produto foi" + str(i))

    def valida_cor(self, dados_produto):
        cor = self.__controlador_sistema.controlador_cores.confere_cor_nome(dados_produto["cor"])
        if isinstance(cor, Cor):
            return cor
        else:
            self.__tela_produtos.mostra_mensagem(
                "ATENCAO:A cor digitada não está cadastrada na lista de cores, digite um cor válida!")
            self.valida_cor(dados_produto)

    def valida_tamanho(self, dados_produto):
        tamanho = self.__controlador_sistema.controlador_tamanhos.confere_tamanho_descricao(
            dados_produto["tamanho"])
        if isinstance(tamanho, Tamanho):
            return tamanho
        else:
            self.__tela_produtos.mostra_mensagem(
                "ATENCAO: A cor digitada não está cadastrada na lista de tamanhos, digite um cor válida!")
            self.valida_tamanho(dados_produto)

    def valida_categoria(self, dados_produto):
        categoria = self.__controlador_sistema.controlador_categorias.confere_categoria_tipo(
            dados_produto["categoria"])
        if isinstance(categoria, Categoria):
            return categoria
        else:
            self.__tela_produtos.mostra_mensagem(
                "ATENCAO:A cor digitada não está cadastrada na lista de categorias, digite um cor válida!")
            self.valida_categoria(dados_produto)

    def lista_produto(self):
        self.__tela_produtos.mostra_produto(self.__produtos)

    def lista_produto_historico(self, produto):
        self.__tela_produtos.mostra_produto({"codigo": produto.codigo, "nome_cor": produto.cor.nome,
                                            "descricao_tamanho": produto.tamanho.descricao, "tipo_categoria": produto.categoria.tipo})

    def excluir_produto(self):
        self.__controlador_sistema.controlador_cores.lista_cor()
        self.__controlador_sistema.controlador_tamanhos.lista_tamanho()
        self.__controlador_sistema.controlador_categorias.lista_categoria()

        codigo = self.__tela_produtos.seleciona_produto()
        for produto in self.__produtos.get_all():
            if produto.codigo == codigo:
                self.__produtos.remove(produto.codigo)
                self.__tela_produtos.mostra_mensagem(
                    "ATENÇÃO: Produto removido com sucesso")
                return None
            else:
                self.__tela_produtos.mostra_mensagem(
                    "ATENCAO: Produto não existente")

    def confere_produto_cor(self, cor):
        for produto in self.__produtos.get_all():
            if (produto.cor == cor):
                return produto
        return None

    def confere_produto_tamanho(self, tamanho):
        for produto in self.__produtos.get_all():
            if (produto.tamanho == tamanho):
                return produto
        return None

    def confere_produto_categoria(self, categoria):
        for produto in self.__produtos.get_all():
            if (produto.categoria == categoria):
                return produto
        return None

    def confere_produto_codigo(self,pessoa):
        codigo = self.__tela_produtos.seleciona_produto()
        print(codigo)
        if codigo == "Sair":
            self.__controlador_sistema.encerra_sistema()
        
        elif codigo == "Voltar":
            self.abre_menu_usuario(pessoa)
        else:  
            codigo = int(self.__tela_produtos.seleciona_produto())
            for produto in self.__produtos.get_all():
                if produto.codigo == codigo:
                    return produto

            self.__tela_produtos.mostra_mensagem(
                "ATENÇÃO: O código digitado não corresponde a nenhum produto cadastrado, digite um código válido!")
            self.confere_produto_codigo(pessoa)

    def alterar_produto(self):
        codigo1 = input('Digite o codigo do produto')
        dados_produto = self.__tela_produtos.pega_dados_produto()
        self.__tela_produtos.mostra_mensagem(
            "ATENCAO: Digite a descricao do produto pelo qual você deseja substituir!")
        cor2 = self.valida_cor(dados_produto)
        tamanho2 = self.valida_tamanho(dados_produto)
        categoria2 = self.valida_categoria(dados_produto)
        verefica = False
        verefica1 = False
        for produto in self.__produtos.get_all():
            if produto.cor == cor2:
                verefica1 = True
                self.__tela_produtos.mostra_mensagem(
                    "ATENCAO: O produto que você deseja alterar já se encontra na lista!")
        for produto in self.__produtos.get_all():
            if produto.codigo == codigo1:
                if produto.cor != cor2 or produto.tamanho != tamanho2 or produto.categoria != categoria2:
                    verefica = True
                    self.__tela_produtos.mostra_mensagem(
                        "ATENCAO: O produto que você deseja alterar já se encontra na lista!")
        if verefica1 == True and verefica != True:
            for produto in self.__produtos.get_all():
                if produto.codigo == codigo1:
                    produto.cor = cor2
                    produto.tamanho = tamanho2
                    produto.categoria = categoria2
                    produto.codigo = codigo1
                    self.__tela_produtos.mostra_mensagem(
                        "ATENCAO: Produto alterada com sucesso")
        else:
            self.__tela_produtos.mostra_mensagem(
                "ATENCAO: O produto que deseja alterar não se encontra na lista de cores")

    def retornar_tela_adm_principal(self, adm):
        self.__controlador_sistema.controla_menu_principal_adm(adm)

    def abre_tela_produtos_adm(self, adm):
        lista_opcoes = {1: self.menu_incluir_produto, 2: self.lista_produto, 3: self.alterar_produto,
                        4: self.excluir_produto, 5: self.__controlador_sistema.controla_menu_principal_adm, 6: self.__controlador_sistema.encerra_sistema}

        continua = True
        while continua:
            opcao_escolhida = self.__tela_produtos.tela_produtos_inicial_adm()
            if opcao_escolhida == 5 or opcao_escolhida == 1:
                lista_opcoes[opcao_escolhida](adm)
            else:
                lista_opcoes[opcao_escolhida]()

    def abre_menu_cor(self, adm):
        self.__controlador_sistema.controlador_cores.abre_tela(adm)

    def abre_menu_tamanho(self, adm):
        self.__controlador_sistema.controlador_tamanhos.abre_tela(adm)

    def abre_menu_categoria(self, adm):
        self.__controlador_sistema.controlador_categorias.abre_tela(adm)

    def retornar_tela_adm_produto(self, adm):
        self.abre_tela_produtos_adm(adm)

    def menu_incluir_produto(self, adm):

        lista_opcoes = {1: self.incluir_produto, 2: self.abre_menu_cor, 3: self.abre_menu_tamanho,
                        4: self.abre_menu_categoria, 5: self.retornar_tela_adm_produto, 6: self.__controlador_sistema.encerra_sistema}

        continua = True
        while continua:
            opcao_escolhida = self.__tela_produtos.tela_produtos__adm()
            if opcao_escolhida == 6:
                lista_opcoes[opcao_escolhida]()
            else:
                lista_opcoes[opcao_escolhida](adm)

    def usuario_compra_produto(self, usuario):
        produto = self.confere_produto_codigo(usuario)
        self.__controlador_sistema.controlador_historico.recebe_dados_venda(
            usuario, produto)

    def retorna_menu_principal_usuario(self, usuario):
        self.__controlador_sistema.controla_menu_principal_usuario(usuario)

    def abre_menu_usuario(self, usuario):
        lista_opcoes = {1: self.lista_produto, 2: self.usuario_compra_produto,
                        3: self.__controlador_sistema.controla_menu_principal_usuario, 4: self.__controlador_sistema.encerra_sistema}

        continua = True
        while continua:
            opcao_escolhida = self.__tela_produtos.tela_produto_usuario()
            if opcao_escolhida == 1 or opcao_escolhida == 4:
                lista_opcoes[opcao_escolhida]()
            else:
                lista_opcoes[opcao_escolhida](usuario)

    def instancia_produtos(self):
        cor1 = self.__controlador_sistema.controlador_cores.confere_cor_nome(
            'VERMELHO')
        cor2 = self.__controlador_sistema.controlador_cores.confere_cor_nome(
            'VERDE')
        cor3 = self.__controlador_sistema.controlador_cores.confere_cor_nome(
            'AMARELO')
        tamanho1 = self.__controlador_sistema.controlador_tamanhos.confere_tamanho_descricao(
            'P')
        tamanho2 = self.__controlador_sistema.controlador_tamanhos.confere_tamanho_descricao(
            'M')
        tamanho3 = self.__controlador_sistema.controlador_tamanhos.confere_tamanho_descricao(
            'G')
        categoria1 = self.__controlador_sistema.controlador_categorias.confere_categoria_tipo(
            'CAMISETA')
        categoria2 = self.__controlador_sistema.controlador_categorias.confere_categoria_tipo(
            'MOLETON')
        categoria3 = self.__controlador_sistema.controlador_categorias.confere_categoria_tipo(
            'SHORT')
        produto1 = Produto(cor1, tamanho2, categoria3, 1)
        produto2 = Produto(cor3, tamanho2, categoria1, 2)
        produto3 = Produto(cor3, tamanho1, categoria1, 3)
        self.__produtos.append(produto1)
        self.__produtos.append(produto2)
        self.__produtos.append(produto3)


