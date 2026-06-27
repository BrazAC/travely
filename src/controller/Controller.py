from PySide6.QtWidgets import QApplication
# Importar model
from src.model.Model import Model
# Importar views
from src.view.JanelaPrincipal import JanelaPrincipal
from src.view.JanelaLogin import JanelaLogin
from src.view.JanelaDashboard import JanelaDashboard

class Controller:
    def __init__(self, app):
        self.__app = app
        # Model
        self.__model = Model(Controller=self)
        
        # Views
        self.__viewJanelaPrincipal = JanelaPrincipal(self.__app)
        self.__viewJanelaLogin = JanelaLogin(self.__app)
        self.__viewJanelaDashboard = JanelaDashboard(self.__app)

        # Organizar Widget de baralho de janelas
        self.organizarWidgetStackJanelaPrincipal()

    def organizarWidgetStackJanelaPrincipal(self):
        self.__viewJanelaPrincipal

        # Adicionar views ao baralho da janela principal
        self.__viewJanelaPrincipal.widgetStackJanelas.addWidget(self.__viewJanelaLogin)     # Índice 0
        self.__viewJanelaPrincipal.widgetStackJanelas.addWidget(self.__viewJanelaDashboard) # Índice 1

        # Conectar sinais
        self.__viewJanelaLogin.sinal_btnGerenteApertado.connect(self.mudarView_dashboard)

    # Mudar views
    def mudarView_login(self):
        self.__viewJanelaPrincipal.widgetStackJanelas.setCurrentIndex(0)
    def mudarView_dashboard(self):
        self.__viewJanelaPrincipal.widgetStackJanelas.setCurrentIndex(1)

    def iniciarView(self):
        self.mudarView_login()
        self.__viewJanelaPrincipal.mostrarJanela()