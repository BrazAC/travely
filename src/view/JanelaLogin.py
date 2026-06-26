from PySide6.QtWidgets import QApplication, QWidget, QLabel, QFrame, QVBoxLayout

class JanelaLogin(QWidget):
    def __init__(self, Qapplication):
        super().__init__(None) 
        # Configurar janela
        self.setWindowTitle("Travely")
        self.resize(400, 300)

        # Widgets
        self.layout_principal = None

        # Inicializar widgets
        self.__criarComponentes()

        # Editar widgets
        #self.__editarComponentes()

    def __criarComponentes(self):
        # Configurar layout
        self.layout_principal = QVBoxLayout(self)

        # Adicionar widgets ao layout
        #self.layout_principal.addWidget(self.__elemento)

    def mostrarJanela(self):
        self.show()