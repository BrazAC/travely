from PySide6.QtWidgets import QApplication, QWidget, QFrame, QVBoxLayout, QHBoxLayout, QPushButton, QLabel
from PySide6.QtCore import Signal
from .JanelaLista import JanelaLista

class JanelaOperador(JanelaLista):
    # Sinais
    sinal_btnCadastrarApertado = Signal()
    sinal_btnFinalizarApertado = Signal()

    def __init__(self, Qapplication):
        super().__init__(Qapplication) 

        # Editar widgets
        self.__editarWidgets()

    def __editarWidgets(self):
        # Botao Cadastrar
        self.botao_cadastrar.clicked.connect(self.sinal_btnCadastrarApertado.emit)
        self.botao_cadastrar.setText("Cadastrar")

        # Botao finalizar
        self.botao_remover.clicked.connect(self.sinal_btnFinalizarApertado.emit)
        self.botao_remover.setText("Finalizar")

    def mostrarJanela(self):
        self.showFullScreen()