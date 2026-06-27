from PySide6.QtWidgets import QApplication, QWidget, QFrame, QVBoxLayout, QHBoxLayout, QPushButton, QLabel
from PySide6.QtCore import Signal

class JanelaLogin(QWidget):
    # Sinais
    sinal_btnGerenteApertado = Signal()
    sinal_btnOperadorApertado = Signal()

    def __init__(self, Qapplication):
        super().__init__(None) 
        # Widgets
        self.layout_principal = None
        self.layout_frame_labels = None
        self.layout_frame_botoes = None
        self.layout_frame_IMAGEM = None
        self.layout_frame_LOGIN = None
        self.frame_labels = None
        self.frame_botoes = None
        self.frame_IMAGEM = None
        self.frame_LOGIN = None
        self.label_textoBoasVindas = None
        self.botao_gerente = None
        self.botao_operador = None

        # Instanciar widgets
        self.__criarWidgets()

        # Editar widgets
        self.__editarWidgets()

    def __criarWidgets(self):
        # Layouts
        self.layout_principal = QHBoxLayout(self)
        self.layout_frame_labels = QHBoxLayout()
        self.layout_frame_botoes = QHBoxLayout()
        self.layout_frame_IMAGEM = QHBoxLayout()
        self.layout_frame_LOGIN = QVBoxLayout()

        # Frames
        self.frame_labels = QFrame() 
        self.frame_botoes = QFrame()
        self.frame_IMAGEM = QFrame()
        self.frame_LOGIN = QFrame()

        # Labels
        self.label_textoBoasVindas = QLabel("Boas vindas. Faça login:")

        # Botoes
        self.botao_gerente = QPushButton("Gerente")
        self.botao_operador = QPushButton("Operador")

    def __editarWidgets(self):
        # Botao gerente
        self.botao_gerente.clicked.connect(self.sinal_btnGerenteApertado.emit)

        # Botao operador
        self.botao_operador.clicked.connect(self.sinal_btnOperadorApertado.emit)

        # Frame imagem
        self.frame_IMAGEM.setFrameShape(QFrame.StyledPanel) 
        self.frame_IMAGEM.setStyleSheet("""
                                        QLabel {
                                            background-color: white;
                                            color: black;
                                            border: none;
                                            border-radius: 5px;
                                            padding: 10px;
                                        }""")
        self.layout_frame_IMAGEM.addWidget(self.label_textoBoasVindas) 
        self.frame_IMAGEM.setLayout(self.layout_frame_IMAGEM)
        self.layout_principal.addWidget(self.frame_IMAGEM)   # Adicionar frame ao layout principal

        # Frame labels
        self.frame_labels.setFrameShape(QFrame.StyledPanel) 
        self.frame_labels.setStyleSheet("""
                                        QLabel {
                                            background-color: white;
                                            color: black;
                                            border: none;
                                            border-radius: 5px;
                                            padding: 10px;
                                        }""")
        self.layout_frame_labels.addWidget(self.label_textoBoasVindas) 
        self.frame_labels.setLayout(self.layout_frame_labels)
        self.layout_frame_LOGIN.addWidget(self.frame_labels)   # Adicionar frame ao layout de login

        # Frame botoes
        self.frame_botoes.setFrameShape(QFrame.StyledPanel) 
        self.frame_botoes.setStyleSheet("""
                                        QLabel {
                                            background-color: white;
                                            color: black;
                                            border: none;
                                            border-radius: 5px; /*
                                            padding: 10px;
                                        }""")
        self.layout_frame_botoes.addWidget(self.botao_gerente)
        self.layout_frame_botoes.addWidget(self.botao_operador)
        self.frame_botoes.setLayout(self.layout_frame_botoes)
        self.layout_frame_LOGIN.addWidget(self.frame_botoes)   # Adicionar frame ao layout de login

        self.frame_LOGIN.setLayout(self.layout_frame_LOGIN)   # Adicionar layout_frame_login ao frame login
        self.layout_principal.addWidget(self.frame_LOGIN)    # Adicionar frame login ao layout principal

        # Atribuir layout_principal a janela da classe
        self.setLayout(self.layout_principal)

    def mostrarJanela(self):
        self.showFullScreen()