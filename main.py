from PyQt5 import QtCore, QtGui, QtWidgets
from classes import adicarter, captchaengine, captchaharv, acccreator

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(197, 171)
        self.btnCaptchaHarv = QtWidgets.QPushButton(Dialog)
        self.btnCaptchaHarv.setGeometry(QtCore.QRect(10, 10, 181, 32))
        font = QtGui.QFont()
        font.setFamily("YEEZY TSTAR")
        font.setPointSize(14)
        self.btnCaptchaHarv.setFont(font)
        self.btnCaptchaHarv.setAutoDefault(False)
        self.btnCaptchaHarv.setFlat(False)
        self.btnCaptchaHarv.setObjectName("btnCaptchaHarv")
        self.btnAccCreator = QtWidgets.QPushButton(Dialog)
        self.btnAccCreator.setGeometry(QtCore.QRect(10, 90, 181, 32))
        font = QtGui.QFont()
        font.setFamily("YEEZY TSTAR")
        font.setPointSize(14)
        self.btnAccCreator.setFont(font)
        self.btnAccCreator.setAutoDefault(False)
        self.btnAccCreator.setObjectName("btnAccCreator")
        self.btnCaptchaEngine = QtWidgets.QPushButton(Dialog)
        self.btnCaptchaEngine.setGeometry(QtCore.QRect(10, 50, 181, 32))
        font = QtGui.QFont()
        font.setFamily("YEEZY TSTAR")
        font.setPointSize(14)
        self.btnCaptchaEngine.setFont(font)
        self.btnCaptchaEngine.setAutoDefault(False)
        self.btnCaptchaEngine.setObjectName("btnCaptchaEngine")
        self.btnAdiCarter = QtWidgets.QPushButton(Dialog)
        self.btnAdiCarter.setGeometry(QtCore.QRect(10, 130, 181, 32))
        font = QtGui.QFont()
        font.setFamily("YEEZY TSTAR")
        font.setPointSize(14)
        self.btnAdiCarter.setFont(font)
        self.btnAdiCarter.setAutoDefault(False)
        self.btnAdiCarter.setObjectName("btnAdiCarter")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Project Theta"))
        self.btnCaptchaHarv.setText(_translate("Dialog", "Captcha Harvester"))
        self.btnAccCreator.setText(_translate("Dialog", "Account Creator"))
        self.btnCaptchaEngine.setText(_translate("Dialog", "Captcha Engine"))
        self.btnAdiCarter.setText(_translate("Dialog", "Adidas Carter"))
        self.btnAdiCarter.clicked.connect(self.startAdiCarter)
        self.btnCaptchaEngine.clicked.connect(self.startCaptchaEngine)
        self.btnCaptchaHarv.clicked.connect(self.startCaptchaHarv)
        self.btnAccCreator.clicked.connect(self.startAccCreator)

    def startAdiCarter(self):
        self.AdiCarter = QtWidgets.QDialog()
        self.AdiCarterUI = adicarter.Ui_Dialog()
        self.AdiCarterUI.setupUi(self.AdiCarter)
        self.AdiCarter.show()

    def startCaptchaHarv(self):
        self.CaptchaHarv = QtWidgets.QDialog()
        self.CaptchaHarvUI = captchaharv.Ui_Dialog()
        self.CaptchaHarvUI.setupUi(self.CaptchaHarv)
        self.CaptchaHarv.show()

    def startCaptchaEngine(self):
        self.CaptchaEngine = QtWidgets.QDialog()
        self.CaptchaEngineUI = captchaengine.Ui_Dialog()
        self.CaptchaEngineUI.setupUi(self.CaptchaEngine)
        self.CaptchaEngine.show()

    def startAccCreator(self):
        self.AccCreator = QtWidgets.QDialog()
        self.AccCreatorUI = acccreator.Ui_dialog()
        self.AccCreatorUI.setupUi(self.AccCreator)
        self.AccCreator.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
