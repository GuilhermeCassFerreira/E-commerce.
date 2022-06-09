import PySimpleGUI as sg

class TelaSistema:
    def __init__(self):
        self.__window = None
        self.init_components()
        self.init_components1()
        self.init_components2()
        self.init_components3()
        self.init_components4()

    #fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
# precisa chamar self.init_components() aqui para o caso de chamar essa janela uma 2a vez. Não é possível reusar layouts de janelas depois de fechadas.
    def tela_inicial(self):
        opcao  = - 1
        while opcao == -1:
            self.init_components()
            button, values = self.__window.Read()
            if values['1']:
                opcao = 1
            if values['2']:
                opcao = 2
            if button == "Sair":
                opcao = 3
            self.close()

        self.close()
        return opcao

    def tela_login(self):
        opcao  = - 1
        while opcao == -1:
            self.init_components1()
            button, values = self.__window.Read()
            if values['1']:
                opcao = 1
            if values['2']:
                opcao = 2
            if button == "Voltar" :
                opcao = 3
            if button == "Sair":
                opcao = 4
            self.close()

        self.close()
        return opcao

    def falha(self):
        opcao  = - 1
        while opcao == -1:
            self.init_components2()
            button, values = self.__window.Read() 
            if button == "Tentar Novamente":
                opcao = 1
            if button == "Voltar":
                opcao = 2
            if button == "Sair":
                opcao = 3
            self.close()
             
        self.close()
        return opcao

    def tela_opcoes_adm(self):
        opcao  = - 1
        while opcao == -1:
            self.init_components3()
            button, values = self.__window.Read()
            if values['1']:
                opcao = 1
            if values['2']:
                opcao = 2
            if  values['3']:
                opcao = 3
            if button == "Sair":
                opcao = 4
            self.close()

        self.close()
        return opcao

    def tela_opcoes_usuario(self):
        opcao  = - 1
        while opcao == -1:
            self.init_components4()
            button, values = self.__window.Read()
            if values['1']:
                opcao = 1
            if values['2']:
                opcao = 2
            if values['3']:
                opcao = 3
            if button == "Sair":
                opcao = 4
            self.close()

        self.close()
        return opcao

    def close(self):
        self.__window.Close()

    def init_components(self):
        #sg.theme_previewer()
        sg.ChangeLookAndFeel('DarkGrey3')
        layout = [
            [sg.Text('Bem vindo ao sistema E-commerce!', font=('Helvica 25 roman'))],
            [sg.Text('Escolha sua opção', font=("Helvica",15))],
            [sg.Radio('Fazer login',"RD1", key='1')],
            [sg.Radio('Criar uma conta',"RD1", key='2')],
            [sg.Button('Confirmar'),sg.Button('Sair')]
        ]
        self.__window = sg.Window('Sistema E-commerce', layout, size=(700,340),element_justification='c')

    def init_components1(self):
        #sg.theme_previewer()
        sg.ChangeLookAndFeel('DarkGrey3')
        layout = [
            [sg.Text('Escolha sua opção', font=("Helvica",15))],
            [sg.Radio('Login Administrador',"RD1", key='1')],
            [sg.Radio('Login Cliente',"RD1", key='2')],
            [sg.Button('Confirmar'), sg.Button('Voltar'), sg.Button('Sair')]
        ]
        self.__window = sg.Window('Sistema E-commerce', layout, size=(700,340),element_justification='c')

    def init_components2(self):

        sg.ChangeLookAndFeel('DarkGrey3')
        layout = [
            
            [sg.Text('Entrada Incorreta!', font=("Helvica",25))],
            [sg.Text('O que você deseja?', font=("Helvica",15))],
            [sg.Button('Tentar Novamente'), sg.Button('Voltar'), sg.Button('Sair')]
        ]
        self.__window = sg.Window('Sistema E-commerce', layout, size=(700,340),element_justification='c')

    def init_components3(self):
        #sg.theme_previewer()
        sg.ChangeLookAndFeel('DarkGrey3')
        layout = [
            [sg.Text('Bem vindo ao sistema E-commerce!', font=("Helvica",25))],
            [sg.Text('Escolha sua opção', font=("Helvica",15))],
            [sg.Radio('Pessoas',"RD1", key='1')],
            [sg.Radio('Produtos',"RD1", key='2')],
            [sg.Radio('Histórico',"RD1", key='3')],
            [sg.Button('Confirmar'), sg.Button('Sair')]
        ]
        self.__window = sg.Window('Sistema E-commerce', layout, size=(700,340),element_justification='c')

    def init_components4(self):
        #sg.theme_previewer()
        sg.ChangeLookAndFeel('DarkGrey3')
        layout = [

            [sg.Text('Escolha sua opção', font=("Helvica",15))],
            [sg.Radio('Ir as Compras',"RD1", key='1')],
            [sg.Radio('Histórico de Compras',"RD1", key='2')],
            [sg.Radio('Dados Pessoais',"RD1", key='3')],
            [sg.Button('Confirmar'), sg.Button('Voltar'), sg.Button('Sair')]
        ]
        self.__window = sg.Window('Sistema E-commerce', layout, size=(700,340),element_justification='c')
