from PySide6.QtWidgets import QMainWindow, QStackedWidget

class JanelaPrincipal(QMainWindow):
    def __init__(self, Qapplication):
        super().__init__(None) 
        self.setWindowTitle("Travely")
        self.resize(400, 300)
        
        # QStackedWidget que vai gerenciar o conteúdo
        self.widgetStackJanelas = QStackedWidget()
        
        # Define o QStackedWidget como o widget central da janela
        self.setCentralWidget(self.widgetStackJanelas)

    def mostrarJanela(self):
        self.showFullScreen()