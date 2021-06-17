import sys

import random
from math import sqrt, ceil

from PyQt5 import QtWidgets, QtCore

from RSA_UI import Ui_MainWindow as first_window

prime_numbs = [0, 0]


def check(number):
    for i in range(2, ceil(sqrt(number)) + 1):
        if number % i == 0:
            return True
    return False


def prime_numbers(quantity, min_numb=1, max_numb=9800):
    global prime_numbs

    if min_numb != prime_numbs[0] and max_numb != prime_numbs[1]:
        t = []

        while min_numb < max_numb:
            flag = 0
            min_numb += 1
            for i in range(2, ceil(sqrt(min_numb)) + 1):
                if min_numb % i == 0:
                    flag = 1
                    break
            if flag == 0:
                t.append(min_numb)

        prime_numbs = [min_numb, max_numb, t]

        return [random.choice(t) for i in range(quantity)]
    else:
        return [random.choice(prime_numbs[2]) for i in range(quantity)]


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

        self.ui.lineEdit_OpenKey_d.setAlignment(QtCore.Qt.AlignCenter)
        self.ui.lineEdit_OpenKey_n.setAlignment(QtCore.Qt.AlignCenter)
        self.ui.lineEdit_CloseKey_e.setAlignment(QtCore.Qt.AlignCenter)
        self.ui.lineEdit_CloseKey_n.setAlignment(QtCore.Qt.AlignCenter)

        self.ui.statusbar.showMessage("Всё готово в работе!")

    def Generating(self):
        self.ui.statusbar.showMessage("Подождите...  Генерируем простые числа")
        f = True
        while f:
            p, q = map(int, prime_numbers(2))

            n = p * q
            nfoc = (p - 1) * (q - 1)

            flag = True
            while flag:
                d = prime_numbers(1)[0]
                if nfoc % d != 0 and d < nfoc:
                    flag = False
            global prime_numbs

            for i in prime_numbs[2]:
                e = i
                if ((e * d) % nfoc) == 1:
                    break

            if ((e * d) % nfoc) == 1:
                f = False

        self.ui.lineEdit_OpenKey_d.setText(str(d))
        self.ui.lineEdit_OpenKey_n.setText(str(n))
        self.ui.lineEdit_CloseKey_e.setText(str(e))
        self.ui.lineEdit_CloseKey_n.setText(str(n))

    def Encryption(self):
        try:
            open_key = [int(self.ui.lineEdit_OpenKey_d.text()), int(self.ui.lineEdit_OpenKey_n.text())]
        except ValueError:
            return self.ui.statusbar.showMessage("Открытый ключ не соответствует типу...")

        if check(open_key[0]):
            return self.ui.statusbar.showMessage("Ошибка открытого ключа...")

        massage = self.ui.textEdit_Massage.toPlainText()
        encmassage = ''

        for i in massage:
            encmassage += chr((ord(i)**open_key[0]) % open_key[1])

        return self.ui.textEdit_Massage.setPlainText(encmassage)

    def Decryption(self):
        try:
            close_key = [int(self.ui.lineEdit_CloseKey_e.text()), int(self.ui.lineEdit_CloseKey_n.text())]
        except ValueError:
            return self.ui.statusbar.showMessage("Закрытый ключ не соответствует типу...")

        if check(close_key[0]):
            return self.ui.statusbar.showMessage("Ошибка закрытого ключа...")

        massage = self.ui.textEdit_Massage.toPlainText()
        encmassage = ''

        for i in massage:
            encmassage += chr((ord(i) ** close_key[0]) % close_key[1])

        return self.ui.textEdit_Massage.setPlainText(encmassage)


app = QtWidgets.QApplication([])
application = RSA_Encripting()
application.show()

sys.exit(app.exec())
