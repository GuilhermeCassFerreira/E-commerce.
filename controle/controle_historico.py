from itertools import count
from this import d
from limite.tela_historico import TelaHistorico
from entidade.historico import Historico
from entidade.usuario import Usuario
from entidade.cor import Cor
from entidade.tamanho import Tamanho
from entidade.categoria import Categoria
from entidade.produto import Produto

class ControladorHistorico():
    
    def __init__(self, controlador_sistema):
        self.__historico = []
        self.__controlador_sistema = controlador_sistema
        self.__tela_historico = TelaHistorico()
    
    @property
    def historico(self):
        return self.__historico

    def confere_output(self, adm, output):
        if output == "Sair":
            self.__controlador_sistema.encerra_sistema()
        elif output == "Voltar":
            self.abre_tela(adm)
        else:
            return output

    # def incluir_historico(self, pessoa):
    #     usuario = self.__controlador_sistema.controlador_pessoas.confere_usuario_cpf_historico()
    #     produto = self.__controlador_sistema.controlador_produtos.confere_produto_codigo(pessoa)
    #     self.recebe_dados_venda(usuario, produto)

    def recebe_dados_venda(self, usuario, produto):
        venda = Historico(usuario, produto)
        self.__historico.append(venda)
        self.__tela_historico.mostra_mensagem("ATENÇÃO: A venda foi adicionada ao histórico!")

    def confere_venda_historico(self, pessoa):
        usuario = self.__controlador_sistema.controle_pessoas.confere_usuario_cpf_historico()
        produto = self.__controlador_sistema.controlador_produtos.confere_produto_codigo(pessoa)
        venda_para_validar = Historico(usuario, produto)

        for venda in self.__historico:
            if venda == venda_para_validar:
                return venda
            else:
                self.__tela_historico.mostra_mensagem("ATENÇÃO: A venda informada não consta no histórico, tente novamente!")
                self.confere_venda_historico(pessoa)

    # def excluir_historico(self, pessoa):
    #     venda_excluir = self.confere_venda_historico(pessoa)
    #     self.__historico.remove(venda_excluir)

    def listar_historico_usuario(self, usuario):
        historico_usuario = []
        for venda in self.__historico:
            if venda.usuario == usuario:
                historico_usuario.append(venda.produto)

        relatorio = self.relatorio_produtos_iguais(historico_usuario)
        self.__tela_historico.imprime_historico(relatorio)

    def relatorio_produtos_iguais(self, lista_historico):
        relatorio = {}
        lista_produtos = self.__controlador_sistema.controlador_produtos.retorna_lista_produtos()

        i = 0
        for produto in lista_produtos:
            vezes = self.conta_objetos(produto, lista_historico)
            relatorio[i] = (produto, vezes)
            i = i + 1
        return relatorio

    def conta_objetos(self, produto, lista_produtos_comprados):
        vezes = 0
        for compra in lista_produtos_comprados:
            if compra.cor.nome == produto.cor.nome and compra.tamanho.descricao == produto.tamanho.descricao and compra.categoria.tipo == produto.categoria.tipo:
                vezes = vezes + 1

        return vezes
        
    def listar_historico_simples(self):
        lista_historico_produto = []

        for venda in self.__historico:
            produto_vendido = venda.produto
            lista_historico_produto.append(produto_vendido)

        relatorio = self.relatorio_produtos_iguais(lista_historico_produto)
        self.__tela_historico.imprime_historico(relatorio)

    def listar_historico_por_pessoa(self, adm):
        historico_pessoa = []
        opcao_pessoa = self.__tela_historico.filtro_cliente()
        opcao_pessoa = self.confere_output(adm, opcao_pessoa)

        if opcao_pessoa == 1:
            return self.__historico

        elif opcao_pessoa == 2:
            objeto_usuario = self.valida_usuario(adm)
            
            for venda in self.__historico:
                if venda.usuario == objeto_usuario:
                    historico_pessoa.append(venda)
            return historico_pessoa

        else:
            self.__tela_historico.mostra_mensagem("ATENÇÃO: A digite uma opção válida!")
            self.listar_historico_por_pessoa(adm)

    def lista_somente_produtos(self, lista, adm):
        lista_historico_produto = []

        for venda in lista:
            produto_vendido = venda.produto
            lista_historico_produto.append(produto_vendido)

        return lista_historico_produto
                
    def filtra_lista_por_cor(self, lista, adm):
        lista_filtrada_cor = []
        opcao_cor = self.__tela_historico.filtro_cor()
        opcao_cor = self.confere_output(adm, opcao_cor)

        if opcao_cor == 1:
            return lista

        elif opcao_cor == 2:
            cor = self.valida_cor(adm)
            for venda in lista:
                if venda.cor.nome == cor.nome:
                    lista_filtrada_cor.append(venda)
            return lista_filtrada_cor
        else:
            self.__tela_historico.mostra_mensagem("ATENÇÃO: Digite uma opção valida!")
            self.filtra_lista_por_cor(lista, adm)

    def filtrar_lista_por_tamanho(self, lista, adm):
        lista_filtrada_tamanho = []
        opcao_tamanho = self.__tela_historico.filtro_tamanho()
        opcao_tamanho = self.confere_output(adm, opcao_tamanho)

        if opcao_tamanho == 1:
            return lista

        elif opcao_tamanho == 2:
            tamanho = self.valida_tamanho(adm)
            for venda in lista:
                if venda.tamanho.descricao == tamanho.descricao:
                    lista_filtrada_tamanho.append(venda)
            return lista_filtrada_tamanho

        else:
            self.__tela_historico.mostra_mensagem("ATENÇÃO: Digite uma opção valida!")
            self.filtrar_lista_por_tamanho(adm)

    def filtrar_lista_por_categoria(self, lista, adm):
        lista_filtrada_categoria = []
        opcao_categoria = self.__tela_historico.filtro_categoria()
        opcao_categoria = self.confere_output(adm, opcao_categoria)

        if opcao_categoria == 1:
            return lista

        elif opcao_categoria == 2:
            categoria = self.valida_categoria(adm)
            for venda in lista:
                if venda.categoria.tipo == categoria.tipo:
                    lista_filtrada_categoria.append(venda)
            return lista_filtrada_categoria

        else:
            self.__tela_historico.mostra_mensagem("ATENÇÃO: Digite uma opção valida!")
            self.filtrar_lista_por_categoria(adm)

    def valida_usuario(self, adm):
        usuario = self.__tela_historico.escolha_cliente()
        objeto_usuario = self.__controlador_sistema.controlador_pessoas.confere_usuario_cpf(usuario)

        if isinstance(objeto_usuario, Usuario):
            return objeto_usuario

        else: 
            lista_opcoes = {1: self.valida_usuario, 2: self.abrir_menu_filtro_adm}
            opcao_escolhida = self.__tela_historico.entrada_incorreta()
            return lista_opcoes[opcao_escolhida](adm)

    def valida_cor(self, adm):
        cor = self.__tela_historico.escolha_cor()
        cor = self.__controlador_sistema.controlador_cores.confere_cor_nome(cor)

        if isinstance(cor, Cor):
            return cor

        else: 
            lista_opcoes = {1: self.valida_cor, 2: self.abrir_menu_filtro_adm}
            opcao_escolhida = self.__tela_historico.entrada_incorreta()
            return lista_opcoes[opcao_escolhida](adm)

    def valida_tamanho(self, adm):
        tamanho = self.__tela_historico.escolha_tamanho()
        tamanho = self.__controlador_sistema.controlador_tamanhos.confere_tamanho_descricao(tamanho)

        if isinstance(tamanho, Tamanho):
            return tamanho
        else: 
            lista_opcoes = {1: self.valida_tamanho, 2: self.abrir_menu_filtro_adm}
            opcao_escolhida = self.__tela_historico.entrada_incorreta()
            return lista_opcoes[opcao_escolhida](adm)
    
    def valida_categoria(self, adm):
        categoria = self.__tela_historico.escolha_categoria()
        categoria = self.__controlador_sistema.controlador_categorias.confere_categoria_tipo(categoria)

        if isinstance(categoria, Categoria):
            return categoria

        else: 
            lista_opcoes = {1: self.valida_categoria, 2: self.abrir_menu_filtro_adm}
            opcao_escolhida = self.__tela_historico.entrada_incorreta()
            return lista_opcoes[opcao_escolhida](adm)

    def listar_historico_personalizado(self, adm):
        lista_pessoa = self.listar_historico_por_pessoa(adm)
        lista_produtos = self.lista_somente_produtos(lista_pessoa, adm)
        lista_cor = self.filtra_lista_por_cor(lista_produtos, adm)
        lista_tamanho = self.filtrar_lista_por_tamanho(lista_cor, adm)
        lista_categoria = self.filtrar_lista_por_categoria(lista_tamanho, adm)
        relatorio_sem_nulos = {}
        relatorio = self.relatorio_produtos_iguais(lista_categoria)
        i = 0
        for codigo in relatorio:
            if relatorio[codigo][1] != 0:

                relatorio_sem_nulos[i] = relatorio[codigo]
                i = i + 1        
        self.__tela_historico.imprime_historico(relatorio_sem_nulos)
        
        
    def voltar_menu_principal_adm(self, adm):
        self.__controlador_sistema.controla_menu_principal_adm(adm)

    def abrir_menu_filtro_adm(self, adm):

        lista_opcoes = {1: self.listar_historico_simples, 2: self.listar_historico_personalizado, 3: self.__controlador_sistema.controla_menu_principal_adm, 4: self.__controlador_sistema.encerra_sistema}
        
        continua = True
        while continua:
            opcao_escolhida = self.__tela_historico.menu_opcao_filtro()
            if opcao_escolhida == 1 or opcao_escolhida == 4:
                lista_opcoes[opcao_escolhida]()
            else:
                lista_opcoes[opcao_escolhida](adm)

    # def abrir_menu_historico_adm(self, adm):
         
    #     lista_opcoes = {1: self.abrir_menu_filtro_adm, 2: self.incluir_historico, 3: self.excluir_historico, 4: self.__controlador_sistema.controla_menu_principal_adm, 5: self.__controlador_sistema.encerra_sistema}
        
    #     continua = True
    #     while continua:
    #         opcao_escolhida = self.__tela_historico.menu_principal_adm()
    #         if opcao_escolhida == 5:
    #             lista_opcoes[opcao_escolhida]()
    #         else:
    #             lista_opcoes[opcao_escolhida](adm)
    
    def instancia_historico(self):
        usuario1 = self.__controlador_sistema.controlador_pessoas.confere_usuario_cpf('09641787969')
        usuario2 = self.__controlador_sistema.controlador_pessoas.confere_usuario_cpf('99900011199')
        produto1 = self.__controlador_sistema.controlador_produtos.pega_produto_por_codigo(1)
        produto2 = self.__controlador_sistema.controlador_produtos.pega_produto_por_codigo(2)
        produto3 = self.__controlador_sistema.controlador_produtos.pega_produto_por_codigo(3)

        venda1 = Historico(usuario1, produto1)
        venda2 = Historico(usuario1, produto2)
        venda3 = Historico(usuario1, produto2)
        venda4 = Historico(usuario1, produto3)
        venda5 = Historico(usuario1, produto3)
        venda6 = Historico(usuario1, produto3)

        #Coloca venda na lista de Historicos
        self.__historico.append(venda1)
        self.__historico.append(venda2)
        self.__historico.append(venda3)
        self.__historico.append(venda4)
        self.__historico.append(venda5)
        self.__historico.append(venda6)


