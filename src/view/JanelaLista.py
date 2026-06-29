from PySide6.QtWidgets import QApplication, QWidget, QFrame, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QListView
from PySide6.QtCore import Signal, QStringListModel

class JanelaLista(QWidget):
    def __init__(self, Qapplication):
        super().__init__(None) 
        # Widgets
        self.layout_principal = None
        self.layout_frame_lista = None
        self.layout_frame_botoes = None
        self.frame_lista = None
        self.frame_botoes = None
        self.botao_cadastrar = None
        self.botao_remover = None
        self.lista_view = None
        self.modelo_dados = None

        # Instanciar widgets
        self.__criarWidgets()

        # Editar widgets
        self.__editarWidgets()

    def __criarWidgets(self):
        # Layouts
        self.layout_principal = QVBoxLayout(self)
        self.layout_frame_lista = QHBoxLayout()
        self.layout_frame_botoes = QHBoxLayout()

        # Frames
        self.frame_lista = QFrame() 
        self.frame_botoes = QFrame()

        # Botoes
        self.botao_cadastrar = QPushButton()
        self.botao_remover = QPushButton()

        # Lista
        self.lista_view = QListView()
        self.modelo_dados = QStringListModel()

    def __editarWidgets(self):
        # Estilo botões
        estilo_botao = """
                        QPushButton {
                            background-color: #2c3e50;
                            color: white;
                            border-radius: 6px;
                            padding: 10px;
                            font-family: 'Segoe UI', Arial;
                            font-size: 20px;
                            font-weight: 600;
                            min-width: 30px;
                            min-height: 45px;
                        }
                        QPushButton:hover {
                            background-color: #34495e;
                        }
                        QPushButton:pressed {
                            background-color: #1a252f;
                        }
                        
                        """

        # Botao gerente
        self.botao_cadastrar.setStyleSheet(estilo_botao)

        # Botao operador
        self.botao_remover.setStyleSheet(estilo_botao)

        # Lista view
        self.lista_view.setModel(self.modelo_dados)
        
        # Configurar layout frame_lista
        self.layout_frame_lista.setContentsMargins(80, 140, 80, 140) # Formato: (Esquerda, Topo, Direita, Base)

        # Frame lista
        self.frame_lista.setFrameShape(QFrame.StyledPanel) 
        self.frame_lista.setStyleSheet("""
                                QFrame {
                                    background-color: #132237;
                                    color: black;
                                    border: 0px solid #ccc;
                                    border-radius: 5px;
                                    padding: 10px;
                                }""")
        self.layout_frame_lista.addWidget(self.lista_view)
        self.frame_lista.setLayout(self.layout_frame_lista)
        self.layout_principal.addWidget(self.frame_lista, 8)   # Adicionar frame ao layout principal, strech factor maior

        # Layout botões
        self.layout_frame_botoes.setContentsMargins(200, 0, 200, 0) # Formato: (Esquerda, Topo, Direita, Base)
        self.layout_frame_botoes.setSpacing(100) # 2. Altera a distância (Margem) entre um botão e o outro

        # Frame botoes
        self.frame_botoes.setFrameShape(QFrame.StyledPanel) 
        self.frame_botoes.setStyleSheet("""
                                QFrame {
                                    background-color: #132237;
                                    color: black;
                                    border: 0px solid #ccc;
                                    border-radius: 5px;
                                    padding: 0px;
                                }""")
        self.layout_frame_botoes.addWidget(self.botao_cadastrar)
        self.layout_frame_botoes.addWidget(self.botao_remover)
        self.frame_botoes.setLayout(self.layout_frame_botoes)
        self.layout_principal.addWidget(self.frame_botoes, 1)   # Adicionar frame ao layout principal, strech factor menor

        # Configurar layout principal
        #self.layout_principal.setContentsMargins(80, 40, 80, 40) # Formato: (Esquerda, Topo, Direita, Base)
        #self.layout_principal.setSpacing(10) # 2. Altera a distância (Margem) entre um frame e outro

        # Atribuir layout_principal a janela da classe
        self.setLayout(self.layout_principal)

    def mostrarJanela(self):
        self.showFullScreen()