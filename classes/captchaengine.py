# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'captchaengine.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 107)
        self.txtAPIKey = QtWidgets.QLineEdit(Dialog)
        self.txtAPIKey.setGeometry(QtCore.QRect(150, 10, 241, 21))
        font = QtGui.QFont()
        font.setFamily("YEEZY TSTAR")
        font.setPointSize(14)
        self.txtAPIKey.setFont(font)
        self.txtAPIKey.setObjectName("txtAPIKey")
        self.boxSolvers = QtWidgets.QSpinBox(Dialog)
        self.boxSolvers.setGeometry(QtCore.QRect(150, 40, 241, 24))
        font = QtGui.QFont()
        font.setFamily("YEEZY TSTAR")
        font.setPointSize(14)
        self.boxSolvers.setFont(font)
        self.boxSolvers.setObjectName("boxSolvers")
        self.btnStart = QtWidgets.QPushButton(Dialog)
        self.btnStart.setGeometry(QtCore.QRect(322, 70, 71, 32))
        font = QtGui.QFont()
        font.setFamily("YEEZY TSTAR")
        font.setPointSize(14)
        self.btnStart.setFont(font)
        self.btnStart.setAutoDefault(False)
        self.btnStart.setObjectName("btnStart")
        self.btnStop = QtWidgets.QPushButton(Dialog)
        self.btnStop.setGeometry(QtCore.QRect(250, 70, 71, 32))
        font = QtGui.QFont()
        font.setFamily("YEEZY TSTAR")
        font.setPointSize(14)
        self.btnStop.setFont(font)
        self.btnStop.setAutoDefault(False)
        self.btnStop.setObjectName("btnStop")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 121, 16))
        font = QtGui.QFont()
        font.setFamily("YEEZY TSTAR")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 43, 131, 16))
        font = QtGui.QFont()
        font.setFamily("YEEZY TSTAR")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Captcha Engine"))
        self.btnStart.setText(_translate("Dialog", "Start"))
        self.btnStop.setText(_translate("Dialog", "Stop"))
        self.label.setText(_translate("Dialog", "2Captcha API Key"))
        self.label_2.setText(_translate("Dialog", "Concurrent Solvers"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

