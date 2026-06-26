from PySide6.QtWidgets import QApplication
# Importar model
# Importar views
from src.view.JanelaLogin import JanelaLogin
from src.model.Model import Model


class Controller:
    def __init__(self, app):
        self.__app = app
        # Model
        self.__model = Model(Controller=self)
        
        # Views
        self.__viewJanelaLogin = JanelaLogin(self.__app)
        
    def iniciarView(self):
        self.__viewJanelaLogin.mostrarJanela()