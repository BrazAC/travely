import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QFrame, QVBoxLayout

from src.controller.Controller import Controller

if __name__ == "__main__":
    # Instanciar aplicação PySide6
    app = QApplication(sys.argv)

    # Instanciar controler passando a aplicação a ser controlada
    controller = Controller(app = app)

    # Mandar controller iniciar view
    controller.iniciarView()

    # Encerrar aplicação Pyside6
    sys.exit(app.exec())