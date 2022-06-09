#from pyparsing import sgl_quoted_string
from limite.tela_abstrata import *
import PySimpleGUI as sg
from entidade.historico import *


class TelaHistorico():
    def __init__(self):
        self.__window = None
        self.init_opcoes()
        self.init_opcoes1()
        self.init_opcoes2()
        self.init_opcoes3()
        self.init_opcoes4()
        self.init_opcoes5()

    def menu_principal_adm(self):
        opcao  = - 1
        while opcao == -1:
            self.init_opcoes()
            button, values = self.__window.Read()
            if values['1']:
                opcao = 1
            if values['2']:
                opcao = 2
            if values['3']:
                opcao = 3
            if values['4']:
                opcao = 4
            if button == "Voltar":
                opcao = 5
            if button == "Sair":
                opcao = 6
            self.close()

        self.close()
        return opcao

    def menu_opcao_filtro(self):

        opcao  = - 1
        while opcao == -1:
            self.init_opcoes1()
            button, values = self.__window.Read()
            if values['1']:
                opcao = 1
            if values['2']:
                opcao = 2
            if button == "Voltar":
                opcao = 3
            if button == "Sair":
                opcao = 4
            self.close()

        self.close()
        return opcao

    def filtro_cor(self):

        opcao  = - 1
        while opcao == -1:
            self.init_opcoes2()
            button, values = self.__window.Read()
            if values['1']:
                opcao = 1
            if values['2']:
                opcao = 2
            self.close()
        self.close()
        return opcao

    def filtro_tamanho(self):

        opcao  = - 1
        while opcao == -1:
            self.init_opcoes3()
            button, values = self.__window.Read()
            if values['1']:
                opcao = 1
            if values['2']:
                opcao = 2
            self.close()
        self.close()
        return opcao

    def filtro_categoria(self):
        opcao  = - 1
        while opcao == -1:
            self.init_opcoes4()
            button, values = self.__window.Read()
            if values['1']:
                opcao = 1
            if values['2']:
                opcao = 2
            self.close()
        self.close()
        return opcao

    def filtro_cliente(self):

        opcao  = - 1
        while opcao == -1:
            self.init_opcoes5()
            button, values = self.__window.Read()
            if values['1']:
                opcao = 1
            if values['2']:
                opcao = 2
            self.close()
        self.close()
        return opcao

    def init_opcoes(self):
       
        sg.ChangeLookAndFeel('DarkGrey3')
        layout = [
            [sg.Text('HISTÓRICO', font=("Helvica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvica", 15))],
            [sg.Radio('Ver Histórico de Vendas', "RD1", key='1')],
            [sg.Radio('Alterar Histórico de Vendas', "RD1", key='2')],
            [sg.Radio('Incluir uma Venda no Histórico', "RD1", key='3')],
            [sg.Radio('Excluir uma Venda do Histórico', "RD1", key='4')],
            [sg.Button('Confirmar'), sg.Button('Voltar'), sg.Button('Sair')]

        ]
        self.__window = sg.Window('Sistema E-commerce', layout, size=(700,340),element_justification='c')

    def init_opcoes1(self):
       
        sg.ChangeLookAndFeel('DarkGrey3')
        layout = [
            [sg.Text('VISUALIZAÇÃO HISTÓRICO', font=("Helvica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvica", 15))],
            [sg.Radio('Ver Todas as Vendas', "RD1", key='1')],
            [sg.Radio('Aplicar Filtro', "RD1", key='2')],
            [sg.Button('Confirmar'), sg.Button('Voltar'), sg.Button('Sair')]

        ]
        self.__window = sg.Window('Sistema E-commerce', layout, size=(700,340),element_justification='c')

    def init_opcoes2(self):
       
        sg.ChangeLookAndFeel('DarkGrey3')
        layout = [
            [sg.Text('COR', font=("Helvica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvica", 15))],
            [sg.Radio('Todas as Cores', "RD1", key='1')],
            [sg.Radio('Escolher uma Cor', "RD1", key='2')],
            [sg.Button('Confirmar')]

        ]
        self.__window = sg.Window('Sistema E-commerce', layout, size=(700,340),element_justification='c')

    def init_opcoes3(self):
       
        sg.ChangeLookAndFeel('DarkGrey3')
        layout = [
            [sg.Text('TAMANHO', font=("Helvica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvica", 15))],
            [sg.Radio('Todas os Tamanhos', "RD1", key='1')],
            [sg.Radio('Escolher um Tamanho', "RD1", key='2')],
            [sg.Button('Confirmar')]

        ]
        self.__window = sg.Window('Sistema E-commerce', layout, size=(700,340),element_justification='c')

    def init_opcoes4(self):

        sg.ChangeLookAndFeel('DarkGrey3')
        layout = [
            [sg.Text('CATEGORIA', font=("Helvica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvica", 15))],
            [sg.Radio('Todas as Categorias', "RD1", key='1')],
            [sg.Radio('Escolher uma Categorias', "RD1", key='2')],
            [sg.Button('Confirmar')]

        ]
        self.__window = sg.Window('Sistema E-commerce', layout, size=(700,340),element_justification='c')

    def init_opcoes5(self):

        sg.ChangeLookAndFeel('DarkGrey3')
        layout = [
            [sg.Text('PRODUTOS', font=("Helvica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvica", 15))],
            [sg.Radio('Todos os Clientes', "RD1", key='1')],
            [sg.Radio('Escolher um Cliente', "RD1", key='2')],
            [sg.Button('Confirmar')]

        ]
        self.__window = sg.Window('Sistema E-commerce', layout, size=(700,340),element_justification='c')

    def escolha_cor(self):
        
        sg.ChangeLookAndFeel('DarkGrey3')
        layout = [
            [sg.Text('DADOS CATEGORIAS ', font=("Helvica", 25))],
            [sg.Text('Cor:', size=(15, 1)), sg.InputText('', key='cor')],
            [sg.Button('Confirmar')]
        ]
        self.__window = sg.Window('Sistema de COR').Layout(layout)

        button, values = self.open()
        cor = values['cor']

        self.close()
        return cor

    def escolha_tamanho(self):

        sg.ChangeLookAndFeel('DarkGrey3')
        layout = [
            [sg.Text('DADOS CATEGORIAS', font=("Helvica", 25))],
            [sg.Text('Tamanho:', size=(15, 1)),
             sg.InputText('', key='tamanho')],
            [sg.Button('Confirmar')]
        ]
        self.__window = sg.Window('Sistema E-commerce', layout, size=(700,340),element_justification='c')

        button, values = self.open()
        tamanho = values['tamanho']
        self.close()
        return tamanho

    def escolha_categoria(self):
        
        sg.ChangeLookAndFeel('DarkGrey3')
        layout = [
            [sg.Text('DADOS CATEGORIAS', font=("Helvica", 25))],
            [sg.Text('Categoria:', size=(15, 1)),
             sg.InputText('', key='categoria')],
            [sg.Button('Confirmar')]

        ]
        self.__window = sg.Window('Sistema E-commerce', layout, size=(700,340),element_justification='c')

        button, values = self.open()
        categoria = values['categoria']

        self.close()
        return categoria

    def imprime_historico(self, relatorio):
        string_todos_produtos = ""
        
        for codigo in relatorio:
            produto = relatorio[codigo][0]
            quantidade = relatorio[codigo][1]

            string_todos_produtos = string_todos_produtos + "PRODUTO: " + produto.categoria.tipo + '\n'
            string_todos_produtos = string_todos_produtos + "COR: " + produto.cor.nome + '\n'
            string_todos_produtos = string_todos_produtos + "TAMANHO: " + produto.tamanho.descricao + '\n'
            string_todos_produtos = string_todos_produtos + "QUANTIDADE: " + str(quantidade) + '\n\n'

        sg.Popup('LISTA DE HISTORICO', string_todos_produtos)

    def escolha_cor(self):
        sg.ChangeLookAndFeel('DarkGrey3')
        layout = [
            [sg.Text('SELECIONAR PRODUTO', font=("Helvica", 25))],
            [sg.Text('Digite o codigo do produto que deseja selecionar:',
                     font=("Helvica", 15))],
            [sg.Text('codigo:', size=(15, 1)), sg.InputText('', key='codigo')],
            [sg.Button('Confirmar')]
        ]
        self.__window = sg.Window('Sistema E-commerce', layout, size=(700,340),element_justification='c')

        button, values = self.open()
        codigo = values['codigo']
        self.close()
        return codigo

    def escolha_cliente(self):
        cpf = input().upper()
        cpf = cpf.strip()
        return cpf

    def mostra_mensagem(self, msg):
        sg.popup("", msg)

    def entrada_incorreta(self):
        opcoes = ['[1] Tentar Novamente','[2] Voltar para o menu anterior']
        
        for item in opcoes:
            print(item)

        print(linha())

        opcao = leiaInt('Digite sua opção: ')
        return opcao

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values
