from PySide6.QtWidgets import QApplication, QWidget, QFrame, QVBoxLayout, QHBoxLayout, QPushButton, QLabel
from PySide6.QtCore import Signal
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
from pathlib import Path

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
        self.image_label = None
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
        self.layout_frame_botoes = QVBoxLayout()
        self.layout_frame_IMAGEM = QHBoxLayout()
        self.layout_frame_LOGIN = QVBoxLayout()

        # Frames
        self.frame_labels = QFrame() 
        self.frame_botoes = QFrame()
        self.frame_IMAGEM = QFrame()
        self.frame_LOGIN = QFrame()

        # Labels
        self.label_textoBoasVindas = QLabel()
        self.image_label = QLabel()

        # Botoes
        self.botao_gerente = QPushButton("Gerente")
        self.botao_operador = QPushButton("Operador")

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
        self.botao_gerente.clicked.connect(self.sinal_btnGerenteApertado.emit)
        self.botao_gerente.setStyleSheet(estilo_botao)

        # Botao operador
        self.botao_operador.clicked.connect(self.sinal_btnOperadorApertado.emit)
        self.botao_operador.setStyleSheet(estilo_botao)

        # Layout botões
        # Formato: (Esquerda, Topo, Direita, Base)
        self.layout_frame_botoes.setContentsMargins(80, 300, 80, 0)

        # 2. Altera a distância (Margem) entre um botão e o outro
        self.layout_frame_botoes.setSpacing(1)

        # Label texto
        self.label_textoBoasVindas.setText("Travely") # Adicionei um \n para quebrar a linha se quiser
        self.label_textoBoasVindas.setAlignment(Qt.AlignCenter)        # Centraliza o texto

        self.label_textoBoasVindas.setStyleSheet("""
            QLabel {
                color: #eff0f1;
                font-size: 60px;
                font-family: 'Segoe UI', Helvetica, Arial;
                font-weight: 600;
                background-color: transparent; /* Para não sobrepor o fundo branco do seu Frame */
            }
        """)

        # Label imagem
        BASE_DIR = Path(__file__).resolve().parent
        CAMINHO_IMAGEM = BASE_DIR.parent / "assets" / "guys-meeting.jpg"
        if not CAMINHO_IMAGEM.exists(): print(f"AVISO: Imagem não encontrada no caminho absoluto: {CAMINHO_IMAGEM}")

        pixmap = QPixmap(str(CAMINHO_IMAGEM))
        scaled_pixmap = pixmap.scaled(1000, 2000, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.image_label.setPixmap(scaled_pixmap)
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_label.setStyleSheet("""
                                QFrame {
                                    background-color: #132237;
                                    color: black;
                                    border: 3px solid #ccc;
                                    border-radius: 5px;
                                    padding: 0px;
                                }""")
        
        # Frame imagem
        self.frame_IMAGEM.setFrameShape(QFrame.StyledPanel) 
        self.layout_frame_IMAGEM.addWidget(self.image_label)
        self.frame_IMAGEM.setLayout(self.layout_frame_IMAGEM)
        self.frame_IMAGEM.setStyleSheet("""
                                QFrame {
                                    background-color: #132237;
                                    color: black;
                                    border: 0px solid #ccc;
                                    border-radius: 5px;
                                    padding: 10px;
                                }""")

        # Frame labels
        self.frame_labels.setFrameShape(QFrame.StyledPanel) 
        self.frame_labels.setStyleSheet("""
                                QFrame {
                                    background-color: #132237;
                                    color: black;
                                    border: 0px solid #ccc;
                                    border-radius: 5px;
                                    padding: 10px;
                                }""")
        self.layout_frame_labels.addWidget(self.label_textoBoasVindas) 
        self.frame_labels.setLayout(self.layout_frame_labels)
        self.layout_frame_LOGIN.addWidget(self.frame_labels)   # Adicionar frame ao layout de login

        # Frame botoes
        self.frame_botoes.setFrameShape(QFrame.StyledPanel) 
        self.frame_botoes.setStyleSheet("""
                                QFrame {
                                    background-color: #132237;
                                    color: black;
                                    border: 0px solid #ccc;
                                    border-radius: 5px;
                                    padding: 10px;
                                }""")
        self.layout_frame_botoes.addWidget(self.botao_gerente)
        self.layout_frame_botoes.addWidget(self.botao_operador)
        self.frame_botoes.setLayout(self.layout_frame_botoes)
        self.layout_frame_LOGIN.addWidget(self.frame_botoes)   # Adicionar frame ao layout de login
        
        self.frame_LOGIN.setLayout(self.layout_frame_LOGIN)     # Adicionar layout_frame_login ao frame login
        self.layout_principal.addWidget(self.frame_IMAGEM)      # Adicionar frame imagem ao layout principal
        self.layout_principal.addWidget(self.frame_LOGIN)       # Adicionar frame login ao layout principal
        

        # Atribuir layout_principal a janela da classe
        self.setLayout(self.layout_principal)
        self.setStyleSheet("""
                                QFrame {
                                    background-color: #132237;
                                    color: black;
                                    border: 0px solid #ccc;
                                    border-radius: 5px;
                                    padding: 10px;
                                }""")

    def mostrarJanela(self):
        self.showFullScreen()