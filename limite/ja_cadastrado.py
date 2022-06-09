class JaCadastrado(Exception):
    def __init__(self):
        super().__init__("já está cadastrado(a)!")
