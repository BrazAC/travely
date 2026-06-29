class Model:
    def __init__(self, Controller):
        self.__controller = Controller

    def consultarViagens(self):
        # Aqui você vai fazer o SELECT SUA MÃE FROM TABELA
        listaViagens = ['1,2,3,4', '1,2,3,4', '1,2,3,4']
        return listaViagens