from limite.tela_tamanho import TelaTamanho
from entidade.tamanho import Tamanho
from limite.cadrasto import Cadastrado
from limite.ja_cadastrado import JaCadastrado
from DAOs.tamanho_daos import TamanhoDAO


class ControladorTamanhos():
    # Fazer lançamento e tratamento de exceções, ao invés de apenas mostrar mensagem na tela.
    def __init__(self, controlador_sistema):
        #self.__tamanhos = []
        self.__tamanhos_DAO = TamanhoDAO()
        self.__controlador_sistema = controlador_sistema
        self.__tela_tamanho = TelaTamanho()

    def confere_tamanho_descricao(self, descricao: str):
        for tamanho in self.__tamanhos_DAO.get_all():
            if (tamanho.descricao == descricao):
                return tamanho
        return None

    def incluir_tamanho(self):
        dados_tamanho = self.__tela_tamanho.pega_dados_tamanho()
        nova_tamanho = self.confere_tamanho_descricao(dados_tamanho)

        try:
            if nova_tamanho == None:
                categoria = Tamanho(dados_tamanho)
                self.__tamanhos_DAO.add(categoria)
                raise Cadastrado
            else:
                raise JaCadastrado
        except JaCadastrado as j:
            self.__tela_tamanho.mostra_mensagem("Categoria" + str(j))
        except Cadastrado as i:
            self.__tela_tamanho.mostra_mensagem("A categoria foi" + str(i))

    def alterar_tamanho(self):
        self.__tela_tamanho.mostra_mensagem(
            "ATENÇÃO: Digite a descrição do tamanho que você deseja alterar")
        tamanhoAntigo = self.__tela_tamanho.alterar_dados_tamanho()
        self.__tela_tamanho.mostra_mensagem(
            "ATENÇÃO: Digite a descrição do tamanho pelo qual você deseja substituir")
        tamanhoNovo = self.__tela_tamanho.alterar_dados_tamanho()
        verefica1 = False
        verefica = False
        for tamanho in self.__tamanhos_DAO.get_all():
            if tamanho.descricao == tamanhoAntigo:
                verefica = True
            if tamanho.descricao == tamanhoNovo:
                verefica1 = True
                self.__tela_tamanho.mostra_mensagem(
                    "ATENÇÃO: O tamanho que você deseja alterar já se encontra na lista")
        if verefica == True and verefica1 != True:
            for tamanho in self.__tamanhos_DAO.get_all():
                if tamanho.descricao == tamanhoAntigo:
                    self.__tela_tamanho.mostra_mensagem(
                        "ATENÇÃO: Tamanho alterado com suesso")
                    tamanho.descricao = tamanhoNovo
        if verefica == False:
            self.__tela_tamanho.mostra_mensagem(
                "ATENÇÃO: O trabalho que deseja alterar não se encontra na lista de cores")

    # Sugestão: se a lista estiver vazia, mostrar a mensagem de lista vazia
    def lista_tamanho(self):
        
        self.__tela_tamanho.mostra_tamanho(self.__tamanhos_DAO.get_all())

    def excluir_tamanho(self):
        descricao_tamanho = self.__tela_tamanho.seleciona_tamanho()
        tamanho = self.confere_tamanho_descricao(descricao_tamanho)
        if(tamanho is not None):
        #self.__amigos.remove(amigo)
            self.__tamanhos_DAO.remove(tamanho.descricao)
            self.lista_tamanho()
        else:
            self.__tela_tamanho.mostra_mensagem("ATENCAO: Tamanho não existente")

    def retornar_menu__produto(self, adm):
        self.__controlador_sistema.controlador_produtos.menu_incluir_produto(
            adm)

    def abre_tela(self, adm):
        lista_opcoes = {1: self.incluir_tamanho, 2: self.alterar_tamanho, 3: self.lista_tamanho,
                        4: self.excluir_tamanho, 5: self.retornar_menu__produto, 6: self.__controlador_sistema.abre_tela_inicial}

        continua = True
        while continua:
            opcao_escolhida = self.__tela_tamanho.tela_opcoes()
            if opcao_escolhida == 5:
                lista_opcoes[opcao_escolhida](adm)
            else:
                lista_opcoes[opcao_escolhida]()

            '''    def instancia_tamanho(self):
        tamanho1 = Tamanho('P')
        tamanho2 = Tamanho('M')
        tamanho3 = Tamanho('G')
        self.__tamanhos.append(tamanho1)
        self.__tamanhos.append(tamanho2)
        self.__tamanhos.append(tamanho3)'''

    def imprime_cabecalho_tamanhos_cadastrados(self):
        self.__tela_tamanho.cabecalho_tamanhos_cadastrados()