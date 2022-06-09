from DAOs.categoria_dao import CategoriaDAO
from limite.tela_categoria import TelaCategoria
from entidade.categoria import Categoria
from limite.ja_cadastrado import JaCadastrado
from limite.cadrasto import Cadastrado

class ControladorCategorias():
  # Fazer lançamento e tratamento de exceções, ao invés de apenas mostrar mensagem na tela.
  def __init__(self, controlador_sistema):
    #self.__categorias = []
    self.__categorias_DAO = CategoriaDAO()
    self.__controlador_sistema = controlador_sistema
    self.__tela_categoria = TelaCategoria()

  def confere_categoria_tipo(self, tipo: str):
    for categoria in self.__categorias_DAO.get_all():
      if (categoria.tipo == tipo):
        return categoria
    return None

  def confere_output(self, adm, output):
      if output == "Sair":
          self.__controlador_sistema.encerra_sistema()
      elif output == "Voltar":
          self.abre_tela(adm)
      else:
          return output
    
  def incluir_categoria(self):
    dados_categoria = self.__tela_categoria.pega_dados_categoria()
    nova_categoria = self.confere_categoria_tipo(dados_categoria)

    try:
      if nova_categoria == None:
        categoria = Categoria(dados_categoria)
        self.__categorias_DAO.add(categoria)
        raise Cadastrado
      else:
        
        raise JaCadastrado
    except JaCadastrado as j:
      self.__tela_categoria.mostra_mensagem("Cor não foi" + str(j))
    except Cadastrado as i:
      self.__tela_categoria.mostra_mensagem("A categoria foi" + str(i))


  def alterar_categoria(self):
        self.__tela_categoria.mostra_mensagem("ATENÇÃO: Digite o tipo da categoria que você deseja alterar")
        categoriaAntigo = self.__tela_categoria.alterar_dados_categoria()
        self.__tela_categoria.mostra_mensagem("ATENÇÃO: Digite o tipo da categoria pelo qual você deseja substituir")
        categoriaNova = self.__tela_categoria.alterar_dados_categoria()
        verefica1 = False
        verefica = False
        for tamanho in self.__categorias_DAO.get_all():
            if tamanho.tipo == categoriaAntigo:
                verefica = True
            if tamanho.tipo == categoriaNova:
                verefica1 = True
                self.__tela_categoria.mostra_mensagem(
                    "ATENÇÃO: A categoria que você deseja alterar já se encontra na lista")
        if verefica == True and verefica1 != True:
            for tamanho in self.__categorias_DAO.get_all():
                if tamanho.tipo == categoriaAntigo:
                    self.__tela_categoria.mostra_mensagem("ATENÇÃO: Categoria alterado com suesso")
                    tamanho.tipo = categoriaNova
        if verefica == False:
            self.__tela_categoria.mostra_mensagem(
                "ATENÇÃO: A categoria que deseja alterar não se encontra na lista de categorias")
        

  # Sugestão: se a lista estiver vazia, mostrar a mensagem de lista vazia
  def lista_categoria(self):

    self.__tela_categoria.mostra_categoria(self.__categorias_DAO.get_all())

  def excluir_categoria(self):
    self.lista_categoria()
    tipo_categoria = self.__tela_categoria.seleciona_categoria()
    categoria = self.confere_categoria_tipo(tipo_categoria)

    if(categoria is not None):
      #self.__amigos.remove(amigo)
      self.__categorias_DAO.remove(categoria.tipo)
      self.lista_categoria()
    else:
      self.__tela_categoria.mostra_mensagem("ATENCAO: Categoria não existente")
    '''    tipo = self.__tela_categoria.seleciona_categoria()
    for categoria in self.__categorias_DAO.get_all():
      if categoria.tipo == tipo:
        self.__categorias_DAO.remove(categoria.tipo)
        self.__tela_categoria.mostra_mensagem("ATENÇÃO: Categoria removido")
      else:
        self.__tela_categoria.mostra_mensagem("ATENÇÃO: Esee categoria não está cadastrado")'''

    
  def retornar_menu__produto(self, adm):
    self.__controlador_sistema.controlador_produtos.menu_incluir_produto(adm)

  def abre_tela(self, adm):
    lista_opcoes = {1: self.incluir_categoria, 2: self.alterar_categoria, 3: self.lista_categoria, 4: self.excluir_categoria, 5: self.retornar_menu__produto, 6: self.__controlador_sistema.abre_tela_inicial}
    
    continua = True
    while continua:
      opcao_escolhida = self.__tela_categoria.tela_opcoes()
      if opcao_escolhida == 5:
        lista_opcoes[opcao_escolhida](adm)
      else:
        lista_opcoes[opcao_escolhida]()

  '''  def instancia_categorias(self):
    categoria1 = Categoria('CALÇA')
    categoria2 = Categoria('CAMISETA')
    categoria3 = Categoria('MOLETON')
    categoria4 = Categoria('SHORT')
    self.__categorias_DAO.add(categoria1)
    self.__categorias_DAO.add(categoria2)
    self.__categorias_DAO.add(categoria3)
    self.__categorias_DAO.add(categoria4)'''

  @property
  def categorias(self):
    return self.__categorias_DAO.get_all()

  def imprime_cabecalho_categorias_cadastradas(self):
    self.__tela_categoria.cabecalho_categorias_cadastradas()
