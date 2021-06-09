import sys

from PyQt5 import QtWidgets

from RSA_UI import Ui_MainWindow as first_window


class RSA_Encripting(QtWidgets.QMainWindow):
    def __init__(self):
        super(RSA_Encripting, self).__init__()
        self.ui = first_window()
        self.ui.setupUi(self)
        self.init_UI()

    def init_UI(self):
        # self.setWindowIcon(QIcon("logo.png")) # Need to make an icon for the app
        self.ui.pushButton_Generate.clicked.connect(self.Generating)
        self.ui.pushButton_Encrypt.clicked.connect(self.Encryption)
        self.ui.pushButton_Decipher.clicked.connect(self.Decryption)

    def Generating(self):
        pass

    def Encryption(self):
        pass

    def Decryption(self):
        pass


app = QtWidgets.QApplication([])
application = RSA_Encripting()
application.show()

sys.exit(app.exec())
