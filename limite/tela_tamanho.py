#from pyparsing import sgl_quoted_string
from limite.tela_abstrata import *
import PySimpleGUI as sg


class TelaTamanho():
    def __init__(self):
        self.__window = None
        self.init_opcoes()
    # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado

    def tela_opcoes(self):
        opcao = - 1
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

    def init_opcoes(self):

        sg.ChangeLookAndFeel('DarkGrey3')
        layout = [
            [sg.Text('TAMANHOS ', font=("Helvica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvica", 15))],
            [sg.Radio('Incluir tamanhos', "RD1", key='1')],
            [sg.Radio('Alterar tamanhos', "RD1", key='2')],
            [sg.Radio('Listar tamanhos', "RD1", key='3')],
            [sg.Radio('Excluir tamanhos', "RD1", key='4')],
            [sg.Button('Confirmar'), sg.Button('Voltar'), sg.Button('Sair')]
        ]
        self.__window = sg.Window('Sistema E-commerce', layout, size=(700,340),element_justification='c')
    # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado

    def pega_dados_tamanho(self):

        sg.ChangeLookAndFeel('DarkGrey3')
        layout = [
            [sg.Text('DADOS TAMANHOS ', font=("Helvica", 25))],
            [sg.Text('Descricao:', size=(15, 1)),
             sg.InputText('', key='descricao')],
            [sg.Button('Confirmar'), sg.Button('Voltar'), sg.Button('Sair')]
        ]
        self.__window = sg.Window('Sistema E-commerce', layout, size=(700,340),element_justification='c')

        button, values = self.open()
        if button == "Sair" or button == "Voltar":
            self.close()
            return button
        
        else:
            if len(values['descricao']) == 0:
                self.mostra_mensagem("É preciso digitar algo")
                self.close()
                return self.pega_dados_tamanho()
            
            descricao = (values['descricao']).upper()
            self.close()
            return descricao
    
    def alterar_dados_tamanho(self):
        sg.ChangeLookAndFeel('DarkGrey3')
        layout = [
            [sg.Text('ALTERAR DADOS TAMANHOS ', font=("Helvica", 25))],
            [sg.Text('Descrição Tamanho Antigo:', size=(20, 1)), sg.InputText('', key='descricao_antigo')],
            [sg.Text('Descrição Tamanho Novo:', size=(20, 1)), sg.InputText('', key='descricao_novo')],
            [sg.Button('Confirmar'), sg.Button('Voltar'), sg.Button('Sair')]
        ]
        self.__window = sg.Window('Sistema E-commerce', layout, size=(700,340),element_justification='c')

        button, values = self.open()

        if button == "Sair" or button == "Voltar":
            self.close()
            return button

        else:
            if len(values['descricao_antigo']) == 0 or len(values['descricao_novo']) == 0:
                self.mostra_mensagem("É preciso digitar algo")
                self.close()
                return self.alterar_dados_tamanho()

            descricao_antigo = (values['descricao_antigo']).upper()
            descricao_novo= (values['descricao_novo']).upper()
            self.close()
            return {"descricao_antigo": descricao_antigo, "descricao_novo": descricao_novo}

    # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    def mostra_tamanho(self, dados_tamanho):
        string_todos_tamanhos = ""
        for tamanho in dados_tamanho:
            string_todos_tamanhos = string_todos_tamanhos + tamanho.descricao + '\n'
        sg.Popup('LISTA DE TAMANHOS ', string_todos_tamanhos)

    def mostra_mensagem(self, msg):
        sg.popup("", msg)

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values
