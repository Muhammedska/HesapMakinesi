import sys
import os
from datetime import datetime
from PyQt5.QtWidgets import QWidget, QApplication, QLineEdit, QPushButton, QLabel, QMainWindow, QMessageBox, QFormLayout, QFileDialog
from PyQt5.QtGui import QIcon

from PyQt5 import QtCore, QtGui, QtWidgets

global hesap
global tumislemler
hesap = ''
tumislemler = []


class Ui_calc(object):
    def setupUi(self, calc):
        calc.setObjectName("calc")
        calc.resize(490, 609)
        calc.setMinimumSize(QtCore.QSize(0, 0))
        calc.setMaximumSize(QtCore.QSize(541, 635))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        calc.setWindowIcon(icon)
        calc.setWindowOpacity(1.0)
        self.centralwidget = QtWidgets.QWidget(calc)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 491, 611))
        self.tabWidget.setMinimumSize(QtCore.QSize(491, 611))
        self.tabWidget.setMaximumSize(QtCore.QSize(491, 611))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.islem_gor = QtWidgets.QLineEdit(self.tab)
        self.islem_gor.setGeometry(QtCore.QRect(30, 20, 421, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.islem_gor.setFont(font)
        self.islem_gor.setReadOnly(True)
        self.islem_gor.setObjectName("islem_gor")
        self.btn_kapat = QtWidgets.QPushButton(self.tab)
        self.btn_kapat.setGeometry(QtCore.QRect(30, 80, 201, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btn_kapat.setFont(font)
        self.btn_kapat.setObjectName("btn_kapat")
        self.btn_esittir = QtWidgets.QPushButton(self.tab)
        self.btn_esittir.setGeometry(QtCore.QRect(360, 80, 91, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btn_esittir.setFont(font)
        self.btn_esittir.setObjectName("btn_esittir")
        self.btn_temizle = QtWidgets.QPushButton(self.tab)
        self.btn_temizle.setGeometry(QtCore.QRect(250, 80, 91, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btn_temizle.setFont(font)
        self.btn_temizle.setObjectName("btn_temizle")
        self.btn_topla = QtWidgets.QPushButton(self.tab)
        self.btn_topla.setGeometry(QtCore.QRect(360, 180, 91, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btn_topla.setFont(font)
        self.btn_topla.setObjectName("btn_topla")
        self.btn_cikar = QtWidgets.QPushButton(self.tab)
        self.btn_cikar.setGeometry(QtCore.QRect(360, 280, 91, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btn_cikar.setFont(font)
        self.btn_cikar.setObjectName("btn_cikar")
        self.btn_carp = QtWidgets.QPushButton(self.tab)
        self.btn_carp.setGeometry(QtCore.QRect(360, 380, 91, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btn_carp.setFont(font)
        self.btn_carp.setObjectName("btn_carp")
        self.btn_bol = QtWidgets.QPushButton(self.tab)
        self.btn_bol.setGeometry(QtCore.QRect(360, 480, 91, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btn_bol.setFont(font)
        self.btn_bol.setObjectName("btn_bol")
        self.btn_3 = QtWidgets.QPushButton(self.tab)
        self.btn_3.setGeometry(QtCore.QRect(250, 180, 91, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btn_3.setFont(font)
        self.btn_3.setObjectName("btn_3")
        self.btn_2 = QtWidgets.QPushButton(self.tab)
        self.btn_2.setGeometry(QtCore.QRect(140, 180, 91, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btn_2.setFont(font)
        self.btn_2.setObjectName("btn_2")
        self.btn_1 = QtWidgets.QPushButton(self.tab)
        self.btn_1.setGeometry(QtCore.QRect(30, 180, 91, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btn_1.setFont(font)
        self.btn_1.setObjectName("btn_1")
        self.btn_4 = QtWidgets.QPushButton(self.tab)
        self.btn_4.setGeometry(QtCore.QRect(30, 280, 91, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btn_4.setFont(font)
        self.btn_4.setObjectName("btn_4")
        self.btn_5 = QtWidgets.QPushButton(self.tab)
        self.btn_5.setGeometry(QtCore.QRect(140, 280, 91, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btn_5.setFont(font)
        self.btn_5.setObjectName("btn_5")
        self.btn_6 = QtWidgets.QPushButton(self.tab)
        self.btn_6.setGeometry(QtCore.QRect(250, 280, 91, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btn_6.setFont(font)
        self.btn_6.setObjectName("btn_6")
        self.btn_8 = QtWidgets.QPushButton(self.tab)
        self.btn_8.setGeometry(QtCore.QRect(140, 380, 91, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btn_8.setFont(font)
        self.btn_8.setObjectName("btn_8")
        self.btn_9 = QtWidgets.QPushButton(self.tab)
        self.btn_9.setGeometry(QtCore.QRect(250, 380, 91, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btn_9.setFont(font)
        self.btn_9.setObjectName("btn_9")
        self.btn_7 = QtWidgets.QPushButton(self.tab)
        self.btn_7.setGeometry(QtCore.QRect(30, 380, 91, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btn_7.setFont(font)
        self.btn_7.setObjectName("btn_7")
        self.btn_0 = QtWidgets.QPushButton(self.tab)
        self.btn_0.setGeometry(QtCore.QRect(140, 480, 91, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btn_0.setFont(font)
        self.btn_0.setObjectName("btn_0")
        self.btn_yay_sa = QtWidgets.QPushButton(self.tab)
        self.btn_yay_sa.setGeometry(QtCore.QRect(250, 480, 91, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btn_yay_sa.setFont(font)
        self.btn_yay_sa.setObjectName("btn_yay_sa")
        self.btn_yay_so = QtWidgets.QPushButton(self.tab)
        self.btn_yay_so.setGeometry(QtCore.QRect(30, 480, 91, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btn_yay_so.setFont(font)
        self.btn_yay_so.setObjectName("btn_yay_so")
        self.tabWidget.addTab(self.tab, icon, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.History = QtWidgets.QListWidget(self.tab_2)
        self.History.setGeometry(QtCore.QRect(10, 40, 461, 541))
        self.History.setObjectName("History")
        self.label = QtWidgets.QLabel(self.tab_2)
        self.label.setGeometry(QtCore.QRect(20, 10, 81, 16))
        self.label.setObjectName("label")
        self.clearHistory = QtWidgets.QPushButton(self.tab_2)
        self.clearHistory.setGeometry(QtCore.QRect(380, 10, 91, 23))
        self.clearHistory.setObjectName("clearHistory")
        self.saveHistory = QtWidgets.QPushButton(self.tab_2)
        self.saveHistory.setGeometry(QtCore.QRect(280, 10, 91, 23))
        self.saveHistory.setObjectName("saveHistory")
        self.tabWidget.addTab(self.tab_2, icon, "")
        calc.setCentralWidget(self.centralwidget)

        self.retranslateUi(calc)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(calc)

    def retranslateUi(self, calc):
        _translate = QtCore.QCoreApplication.translate
        calc.setWindowTitle(_translate("calc", "Hesap Makinesi"))
        self.islem_gor.setPlaceholderText(_translate("calc", "İşleminiz"))
        self.btn_kapat.setText(_translate("calc", "İşlemi sil"))
        self.btn_esittir.setText(_translate("calc", "="))
        self.btn_temizle.setText(_translate("calc", "<-"))
        self.btn_topla.setText(_translate("calc", "+"))
        self.btn_cikar.setText(_translate("calc", "-"))
        self.btn_carp.setText(_translate("calc", "X"))
        self.btn_bol.setText(_translate("calc", "/"))
        self.btn_3.setText(_translate("calc", "3"))
        self.btn_2.setText(_translate("calc", "2"))
        self.btn_1.setText(_translate("calc", "1"))
        self.btn_4.setText(_translate("calc", "4"))
        self.btn_5.setText(_translate("calc", "5"))
        self.btn_6.setText(_translate("calc", "6"))
        self.btn_8.setText(_translate("calc", "8"))
        self.btn_9.setText(_translate("calc", "9"))
        self.btn_7.setText(_translate("calc", "7"))
        self.btn_0.setText(_translate("calc", "0"))
        self.btn_yay_sa.setText(_translate("calc", ")"))
        self.btn_yay_so.setText(_translate("calc", "("))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("calc", "Hesap Makinesi"))
        self.label.setText(_translate("calc", "İşlem Geçmişi"))
        self.clearHistory.setText(_translate("calc", "Temizle"))
        self.saveHistory.setText(_translate("calc", "Kaydet"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("calc", "İşlem Geçmişi"))

class calculator(QMainWindow,Ui_calc):
    global hesap
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Geçmiş işlemleri
        self.clearHistory.clicked.connect(self.clear_historical)
        self.saveHistory.clicked.connect(self.save_historical)


        # buton tıklama olayları
        self.btn_0.clicked.connect(self.buton_olaylari_btn_0)
        self.btn_1.clicked.connect(self.buton_olaylari_btn_1)
        self.btn_2.clicked.connect(self.buton_olaylari_btn_2)
        self.btn_3.clicked.connect(self.buton_olaylari_btn_3)
        self.btn_4.clicked.connect(self.buton_olaylari_btn_4)
        self.btn_5.clicked.connect(self.buton_olaylari_btn_5)
        self.btn_6.clicked.connect(self.buton_olaylari_btn_6)
        self.btn_7.clicked.connect(self.buton_olaylari_btn_7)
        self.btn_8.clicked.connect(self.buton_olaylari_btn_8)
        self.btn_9.clicked.connect(self.buton_olaylari_btn_9)

        self.btn_yay_sa.clicked.connect(self.buton_olaylari_btn_ya_sa)
        self.btn_yay_so.clicked.connect(self.buton_olaylari_btn_ya_so)

        self.btn_kapat.clicked.connect(self.buton_olaylari_btn_kapat)
        self.btn_esittir.clicked.connect(self.buton_olaylari_btn_esittir)
        self.btn_temizle.clicked.connect(self.buton_olaylari_btn_temizle)
        self.btn_topla.clicked.connect(self.buton_olaylari_btn_topla)
        self.btn_cikar.clicked.connect(self.buton_olaylari_btn_cikar)
        self.btn_carp.clicked.connect(self.buton_olaylari_btn_carp)
        self.btn_bol.clicked.connect(self.buton_olaylari_btn_bol)

    def buton_olaylari_btn_0(self):
        global hesap
        hesap += '0'
        self.islem_gorundu()
    def buton_olaylari_btn_1(self):
        global hesap
        hesap += '1'
        self.islem_gorundu()
    def buton_olaylari_btn_2(self):
        global hesap
        hesap += '2'
        self.islem_gorundu()
    def buton_olaylari_btn_3(self):
        global hesap
        hesap += '3'
        self.islem_gorundu()
    def buton_olaylari_btn_4(self):
        global hesap
        hesap += '4'
        self.islem_gorundu()
    def buton_olaylari_btn_5(self):
        global hesap
        hesap += '5'
        self.islem_gorundu()
    def buton_olaylari_btn_6(self):
        global hesap
        hesap += '6'
        self.islem_gorundu()
    def buton_olaylari_btn_7(self):
        global hesap
        hesap += '7'
        self.islem_gorundu()
    def buton_olaylari_btn_8(self):
        global hesap
        hesap += '8'
        self.islem_gorundu()
    def buton_olaylari_btn_9(self):
        global hesap
        hesap += '9'
        self.islem_gorundu()
    def buton_olaylari_btn_topla(self):
        global hesap
        hesap += '+'
        self.islem_gorundu()
    def buton_olaylari_btn_cikar(self):
        global hesap
        hesap += '-'
        self.islem_gorundu()
    def buton_olaylari_btn_carp(self):
        global hesap
        hesap += '*'
        self.islem_gorundu()
    def buton_olaylari_btn_bol(self):
        global hesap
        hesap += '/'
        self.islem_gorundu()
    def buton_olaylari_btn_esittir(self):
        global hesap
        if hesap == '':
            self.islem_gor.setText('Değer girilmedi')
        else:
            self.hesabi_bitir()
    def buton_olaylari_btn_kapat(self):
        global hesap
        hesap = ''
        self.islem_gorundu()
    def buton_olaylari_btn_temizle(self):
        global hesap
        temizle = hesap[0:len(hesap)-1]
        hesap = temizle
        self.islem_gorundu()
    def buton_olaylari_btn_ya_sa(self):
        global hesap
        hesap += ')'
        self.islem_gorundu()
    def buton_olaylari_btn_ya_so(self):
        global hesap
        hesap += '('
        self.islem_gorundu()
    def islem_gorundu(self):
        self.islem_gor.setText(hesap)

    def hesabi_bitir(self):
        global tumislemler
        global hesap
        utility = eval(hesap)
        fatality = utility
        gecmis = hesap +' = '+str(fatality)
        self.islem_gor.setText(gecmis)
        self.History.addItem(gecmis)
        tumislemler.append(gecmis)
        hesap = str(fatality)

    def save_historical(self):
        global tumislemler
        an = datetime.now()
        tarih = datetime.ctime(an)
        fileHorse =open('history_'+' .txt','w',encoding='utf-8')
        for i in tumislemler:
            fileHorse.write(i+' ,\n')
        fileHorse.close()
        QMessageBox.information(self,'Bildiri','Kayıt Başarılı oldu !')
        os.startfile('history_ .txt')
    def clear_historical(self):
        global tumislemler
        tumislemler = []
        self.History.clear()
App = QApplication(sys.argv)

AppUi = calculator()
AppUi.show()

App.exec_()
