from tkinter import Button
from controle.controle_historico import ControladorHistorico
from limite.tela_abstrata import *
from limite.tela_sistema  import TelaSistema
from controle.controlador_cores import ControladorCores
from controle.controlador_tamanhos import ControladorTamanhos
from controle.controlador_categorias import ControladorCategorias
from controle.controlador_produtos import ControladorProdutos
from controle.controle_pessoas import ControladorPessoa

class ControladorSistema:

    def __init__(self):
        self.__controlador_cores = ControladorCores(self)
        self.__controlador_tamanhos = ControladorTamanhos(self)
        self.__controlador_categorias = ControladorCategorias(self)
        self.__controlador_produtos = ControladorProdutos(self)
        self.__controle_pessoas = ControladorPessoa(self)
        self.__controlador_historico = ControladorHistorico(self)
        self.__tela_sistema = TelaSistema()

    @property
    def controlador_cores(self):
        return self.__controlador_cores

    @property
    def controlador_tamanhos(self):
        return self.__controlador_tamanhos

    @property
    def controlador_categorias(self):
        return self.__controlador_categorias

    @property
    def controlador_produtos(self):
        return self.__controlador_produtos

    @property
    def controlador_pessoas(self):
        return self.__controle_pessoas
    
    @property
    def controlador_historico(self):
        return self.__controlador_historico

    def inicializa_sistema(self):
        self.__controle_pessoas.instancia_pessoas()
        #self.__controlador_cores.instancia_cor()
        #self.__controlador_tamanhos.instancia_tamanho()
        #self.__controlador_categorias.instancia_categorias()
        #self.__controlador_produtos.instancia_produtos()
        self.__controlador_historico.instancia_historico()
        self.abre_tela_inicial()

    def encerra_sistema(self):
        exit(0)

    def controla_menu_principal_adm(self, adm):
        lista_opcoes = {1: self.controla_pessoas_adm, 2: self.controla_produto_adm, 3: self.controla_historico_adm, 4: self.inicializa_sistema}
        opcao_escolhida = self.__tela_sistema.tela_opcoes_adm()
        if opcao_escolhida == 4:
            lista_opcoes[opcao_escolhida]()
        else:
            lista_opcoes[opcao_escolhida](adm)
    
    def controla_pessoas_adm(self, adm):
        self.__controle_pessoas.abre_tela_adm(adm)

    def controla_produto_adm(self, adm):
        self.__controlador_produtos.abre_tela_produtos_adm(adm)

    def controla_historico_adm(self, adm):
        self.__controlador_historico.abrir_menu_filtro_adm(adm)

    def controla_menu_principal_usuario(self, usuario):
        lista_opcoes = {1: self.controla_produto_usuario, 2: self.controla_historico_usuario, 3: self.controla_pessoas_usuario, 4: self.inicializa_sistema}
        opcao_escolhida = self.__tela_sistema.tela_opcoes_usuario()
        if opcao_escolhida == 4:
            lista_opcoes[opcao_escolhida]()
        else:
            lista_opcoes[opcao_escolhida](usuario)

    def controla_produto_usuario(self, usuario):
        self.__controlador_produtos.abre_menu_usuario(usuario)

    def controla_historico_usuario(self, usuario):
        self.__controlador_historico.listar_historico_usuario(usuario)
        self.controla_menu_principal_usuario(usuario)

    def controla_pessoas_usuario(self, usuario):
        self.__controle_pessoas.abre_tela_usuario(usuario)

    def confere_login_adm(self):
        adm = self.__controle_pessoas.confere_login(1)
        if adm is not None:
            self.controla_menu_principal_adm(adm)

        else:
            self.falha_login_adm()

    def confere_login_usuario(self):
        usuario = self.__controle_pessoas.confere_login(2)
        if usuario is not None:
            self.controla_menu_principal_usuario(usuario)

        else:
            self.falha_login_usuario()

    def falha_login_adm(self):
        lista_opcoes = {1: self.confere_login_adm, 2: self.controla_tela_login, 3: self.encerra_sistema}
        opcao_escolhida = self.__tela_sistema.falha()
        lista_opcoes[opcao_escolhida]()

    def falha_login_usuario(self):
        lista_opcoes = {1: self.confere_login_usuario, 2: self.controla_tela_login, 3: self.encerra_sistema}
        opcao_escolhida = self.__tela_sistema.falha()
        lista_opcoes[opcao_escolhida]()

    def controla_tela_login(self):
        lista_opcoes = {1:self.confere_login_adm, 2:self.confere_login_usuario, 3:self.abre_tela_inicial, 4:self.encerra_sistema}
        opcao_escolhida = self.__tela_sistema.tela_login()
        lista_opcoes[opcao_escolhida]()

    def incluir_usuario(self):
        novo_usuario = None
        usuario = self.__controle_pessoas.incluir_usuario(novo_usuario)
        if usuario is not None:
            self.abre_tela_inicial()
        else: 
            self.falha_cpf_ja_cadastrado()

    def falha_cpf_ja_cadastrado(self):
        lista_opcoes = {1: self.incluir_usuario, 2: self.abre_tela_inicial, 3: self.encerra_sistema}
        opcao_escolhida = self.__tela_sistema.falha()
        lista_opcoes[opcao_escolhida]()

    def abre_tela_inicial(self):
        lista_opcoes = {1: self.controla_tela_login, 2: self.incluir_usuario, 3: self.encerra_sistema}
        opcao_escolhida = self.__tela_sistema.tela_inicial()
        lista_opcoes[opcao_escolhida]()

            
