#from pyparsing import sgl_quoted_string
from limite.tela_abstrata import *
import PySimpleGUI as sg


class TelaProduto():
    def __init__(self):
        self.__window = None
        self.init_opcoes()
        self.init_opcoes1()
        self.init_opcoes2()
    def tela_produtos_inicial_adm(self):
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

    def tela_produtos__adm(self):
        opcao  = - 1
        while opcao == -1:
            self.init_opcoes1()
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

    def tela_produto_usuario(self):

        opcao  = - 1
        while opcao == -1:
            self.init_opcoes2()
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

    def init_opcoes(self):

        sg.ChangeLookAndFeel('DarkGrey3')
        layout = [
            [sg.Text('PRODUTOS ', font=("Helvica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvica", 15))],
            [sg.Radio('Incluir produto', "RD1", key='1')],
            [sg.Radio('Listar produto', "RD1", key='2')],
            [sg.Radio('Alterar produto', "RD1", key='3')],
            [sg.Radio('Excluir produto', "RD1", key='4')],
            [sg.Button('Confirmar'), sg.Button('Voltar'), sg.Button('Sair')]

        ]
        self.__window = sg.Window('Sistema E-commerce', layout, size=(700,340),element_justification='c')

    def init_opcoes1(self):

        sg.ChangeLookAndFeel('DarkGrey3')
        layout = [
            [sg.Text('PRODUTOS ', font=("Helvica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvica", 15))],
            [sg.Radio('Incluir produto agora', "RD1", key='1')],
            [sg.Radio('Menu cor', "RD1", key='2')],
            [sg.Radio('Menu tamanho', "RD1", key='3')],
            [sg.Radio('Menu categoria', "RD1", key='4')],
            [sg.Button('Confirmar'), sg.Button('Voltar'), sg.Button('Sair')]

        ]
        self.__window = sg.Window('Sistema E-commerce', layout, size=(700,340),element_justification='c')

    def init_opcoes2(self):

        sg.ChangeLookAndFeel('DarkGrey3')
        layout = [
            [sg.Text('PRODUTOS ', font=("Helvica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvica", 15))],
            [sg.Radio('Ver Produtos Disponíveis', "RD1", key='1')],
            [sg.Radio('Comprar um Produto Agora', "RD1", key='2')],
            [sg.Button('Confirmar'), sg.Button('Voltar'), sg.Button('Sair')]

        ]
        self.__window = sg.Window('Sistema E-commerce', layout, size=(700,340),element_justification='c')
    # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado

    def pega_dados_produto(self):

        sg.ChangeLookAndFeel('DarkGrey3')
        layout = [
            [sg.Text('DADOS CATEGORIAS ', font=("Helvica", 25))],
            [sg.Text('Cor:', size=(15, 1)), sg.InputText('', key='cor')],
            [sg.Text('Tamanho:', size=(15, 1)),
             sg.InputText('', key='tamanho')],
            [sg.Text('Categoria:', size=(15, 1)),
             sg.InputText('', key='categoria')],
            [sg.Button('Confirmar'), sg.Button('Voltar'), sg.Button('Sair')]

        ]
        self.__window = sg.Window('Sistema E-commerce', layout, size=(700,340),element_justification='c')

        button, values = self.open()

        if button == "Voltar" or button == "Sair":
            self.close()
            return button
        else:
            cor = values['cor']
            tamanho = values['tamanho']
            categoria = values['categoria']

            self.close()
            return {"cor": cor, "tamanho": tamanho, "categoria": categoria}

    # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    def mostra_produto(self, dados_produto):
        string_todos_produtos = ""
        for produto in dados_produto:
            string_todos_produtos = string_todos_produtos + "CODIGO DO PRODUTO: " + str(produto.codigo) + '\n'
            string_todos_produtos = string_todos_produtos + "COR DO PRODUTO: " + produto.cor.nome + '\n'
            string_todos_produtos = string_todos_produtos + "TAMANHO DO PRODUTO: " + produto.tamanho.descricao + '\n'
            string_todos_produtos = string_todos_produtos + "CATEGORIA DO PRODUTO: " + produto.categoria.tipo + '\n\n'

        sg.Popup('LISTA DE PRODUTO ', string_todos_produtos)

    # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    def seleciona_produto(self):
        sg.ChangeLookAndFeel('DarkGrey3')
        layout = [
            [sg.Text('SELECIONAR PRODUTO ', font=("Helvica", 25))],
            [sg.Text('Digite o codigo do produto que deseja selecionar:',
                     font=("Helvica", 15))],
            [sg.Text('codigo:', size=(15, 1)), sg.InputText('', key='codigo')],
            [sg.Button('Confirmar'), sg.Button('Voltar'), sg.Button('Sair')]

        ]
        self.__window = sg.Window('Sistema E-commerce', layout, size=(700,340),element_justification='c')

        button, values = self.open()

        if button == "Sair" or button == "Voltar":
            self.close()
            return button
        else:
            codigo = values['codigo']
            self.close()
            return codigo

    def mostra_mensagem(self, msg):
        sg.popup("", msg)

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values
