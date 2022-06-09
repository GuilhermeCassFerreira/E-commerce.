#from pyparsing import sgl_quoted_string
from limite.tela_abstrata import *
import PySimpleGUI as sg


class TelaCategoria():
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
            [sg.Text('CATEGORIAS ', font=("Helvica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvica", 15))],
            [sg.Radio('Incluir categoria', "RD1", key='1')],
            [sg.Radio('Alterar categorias', "RD1", key='2')],
            [sg.Radio('Listar categorias', "RD1", key='3')],
            [sg.Radio('Excluir categrias', "RD1", key='4')],
            [sg.Button('Confirmar'), sg.Button('Voltar'), sg.Button('Sair')]
        ]
        self.__window = sg.Window('Sistema E-commerce', layout, size=(700,340),element_justification='c')
    # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado

    def pega_dados_categoria(self):

        sg.ChangeLookAndFeel('DarkGrey3')
        layout = [
            [sg.Text('DADOS CATEGORIAS ', font=("Helvica", 25))],
            [sg.Text('Tipo:', size=(15, 1)), sg.InputText('', key='tipo')],
            [sg.Button('Confirmar'), sg.Button('Voltar'), sg.Button('Sair')]
        ]
        self.__window = sg.Window('Sistema E-commerce', layout, size=(700,340),element_justification='c')

        button, values = self.open()
    
        if button == "Sair" or button == "Voltar":
            self.close()
            return button
        
        else:
            if len(values['tipo']) == 0:
                self.mostra_mensagem("É preciso digitar algo")
                self.close()
                return self.pega_dados_categoria()
            
            tipo= (values['tipo']).upper()
            self.close()
            return tipo

    # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    def alterar_dados_categoria(self):
        sg.ChangeLookAndFeel('DarkGrey3')
        layout = [
            [sg.Text('ALTERAR DADOS CATEGORIAS ', font=("Helvica", 25))],
            [sg.Text('Tipo Categoria Antigo:', size=(15, 1)), sg.InputText('', key='tipo_antigo')],
            [sg.Text('Tipo Categoria Novo:', size=(15, 1)), sg.InputText('', key='tipo_novo')],
            [sg.Button('Confirmar'), sg.Button('Voltar'), sg.Button('Sair')]
        ]
        self.__window = sg.Window('Sistema E-commerce', layout, size=(700,340),element_justification='c')

        button, values = self.open()

        if button == "Sair" or button == "Voltar":
            self.close()
            return button
        else:
            if len(values['tipo_antigo']) == 0 or len(values['tipo_novo']) == 0:
                self.mostra_mensagem("É preciso digitar algo")
                self.close()
                return self.alterar_dados_categoria()

            tipo_antigo = (values['tipo_antigo']).upper()
            tipo_novo= (values['tipo_novo']).upper()
            self.close()
            return {"tipo_antigo": tipo_antigo, "tipo_novo": tipo_novo}

    def mostra_categoria(self, dados_categoria):
        string_todos_categorias = ""

        for categoria in dados_categoria:
            string_todos_categorias = string_todos_categorias + categoria.tipo + '\n'
        sg.Popup('LISTA DE CATEGORIA ', string_todos_categorias)

    def mostra_mensagem(self, msg):
        sg.popup("", msg)

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values
