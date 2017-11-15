# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'captchaharv.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from threading import Thread
from classes import harvester
from selenium import webdriver

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 104)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(16, 13, 60, 16))
        font = QtGui.QFont()
        font.setFamily("YEEZY TSTAR")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.txtURL = QtWidgets.QLineEdit(Dialog)
        self.txtURL.setGeometry(QtCore.QRect(90, 10, 291, 21))
        font = QtGui.QFont()
        font.setFamily("YEEZY TSTAR")
        font.setPointSize(14)
        self.txtURL.setFont(font)
        self.txtURL.setObjectName("txtURL")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(16, 43, 60, 16))
        font = QtGui.QFont()
        font.setFamily("YEEZY TSTAR")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.txtSitekey = QtWidgets.QLineEdit(Dialog)
        self.txtSitekey.setGeometry(QtCore.QRect(90, 40, 291, 21))
        font = QtGui.QFont()
        font.setFamily("YEEZY TSTAR")
        font.setPointSize(14)
        self.txtSitekey.setFont(font)
        self.txtSitekey.setObjectName("txtSitekey")
        self.btnStart = QtWidgets.QPushButton(Dialog)
        self.btnStart.setGeometry(QtCore.QRect(10, 70, 381, 32))
        font = QtGui.QFont()
        font.setFamily("YEEZY TSTAR")
        font.setPointSize(14)
        self.btnStart.setFont(font)
        self.btnStart.setAutoDefault(False)
        self.btnStart.setObjectName("btnStart")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Captcha Harvester"))
        self.label.setText(_translate("Dialog", "URL"))
        self.txtURL.setText(_translate("Dialog", "http://dev.adidas.com"))
        self.label_2.setText(_translate("Dialog", "Sitekey"))
        self.btnStart.setText(_translate("Dialog", "Start Harvester"))
        self.btnStart.clicked.connect(self.startHarvester)

    def startHarvester(self):
        harvester.sitekey = self.txtSitekey.text()
        Thread(target = lambda: harvester.app.run(host = '0.0.0.0')).start()
        s = webdriver.Chrome()
        s.get(self.txtURL.text() + ':5000/solve')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
