from PyQt5 import QtCore, QtGui, QtWidgets
from python_anticaptcha import AnticaptchaClient, NoCaptchaTaskProxylessTask
from classes.twocaptcha import TwoCaptchaCosmo
import requests

solve = True

class antiCaptcha(QtCore.QThread):
    def __init__(self, apikey, sitekey, url):
        QtCore.QThread.__init__(self)
        self.apikey = apikey
        self.sitekey = sitekey
        self.url = url
        self.s = requests.Session()
    def run(self):
        global solve
        while solve:
            client = AnticaptchaClient(self.apikey)
            task = NoCaptchaTaskProxylessTask(self.url, self.sitekey)
            try:
                job = client.createTask(task)
            except Exception:
                print('Anti-Captcha Balance Zero')
                break
            job.join()
            payload = {
                'g-recaptcha-response' : job.get_solution_response()
            }
            while True:
                try:
                    self.s.post('http://127.0.0.1:5000/solve', data = payload)
                    break
                except:
                    print('Please Start Captcha Harvester. (THIS STORES THE TOKENS.)')
            print('Submitted Anti-Captcha')

class twoCaptcha(QtCore.QThread):
    def __init__(self, apikey, sitekey, url):
        QtCore.QThread.__init__(self)
        self.apikey = apikey
        self.sitekey = sitekey
        self.url = url
        self.s = requests.Session()
    def run(self):
        while True:
            twoCaptcha = TwoCaptchaCosmo(self.apikey, self.sitekey, self.url)
            key = twoCaptcha.Solve()
            if 'ERROR' in key:
                print('Two Captcha Balance Zero')
                break
            payload = {
                'g-recaptcha-response' : key
            }
            while True:
                try:
                    self.s.post('http://127.0.0.1:5000/solve', data = payload)
                    break
                except:
                    print('Please Start Captcha Harvester. (THIS STORES THE TOKENS.)')
            print('Submitted 2Captcha')

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 291)
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 381, 61))
        font = QtGui.QFont()
        font.setFamily("YEEZY TSTAR")
        font.setPointSize(14)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.rad2CapOn = QtWidgets.QRadioButton(self.groupBox)
        self.rad2CapOn.setGeometry(QtCore.QRect(10, 34, 100, 20))
        font = QtGui.QFont()
        font.setFamily("YEEZY TSTAR")
        font.setPointSize(14)
        self.rad2CapOn.setFont(font)
        self.rad2CapOn.setObjectName("rad2CapOn")
        self.rad2CapOff = QtWidgets.QRadioButton(self.groupBox)
        self.rad2CapOff.setGeometry(QtCore.QRect(70, 34, 100, 20))
        font = QtGui.QFont()
        font.setFamily("YEEZY TSTAR")
        font.setPointSize(14)
        self.rad2CapOff.setFont(font)
        self.rad2CapOff.setObjectName("rad2CapOff")
        self.txtAPIKey2CAP = QtWidgets.QLineEdit(self.groupBox)
        self.txtAPIKey2CAP.setGeometry(QtCore.QRect(130, 33, 241, 22))
        font = QtGui.QFont()
        font.setFamily("YEEZY TSTAR")
        font.setPointSize(14)
        self.txtAPIKey2CAP.setFont(font)
        self.txtAPIKey2CAP.setObjectName("txtAPIKey2CAP")
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 80, 381, 61))
        font = QtGui.QFont()
        font.setFamily("YEEZY TSTAR")
        font.setPointSize(14)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.radAntiOn = QtWidgets.QRadioButton(self.groupBox_2)
        self.radAntiOn.setGeometry(QtCore.QRect(10, 34, 100, 20))
        font = QtGui.QFont()
        font.setFamily("YEEZY TSTAR")
        font.setPointSize(14)
        self.radAntiOn.setFont(font)
        self.radAntiOn.setObjectName("radAntiOn")
        self.radAntiOff = QtWidgets.QRadioButton(self.groupBox_2)
        self.radAntiOff.setGeometry(QtCore.QRect(70, 34, 100, 20))
        font = QtGui.QFont()
        font.setFamily("YEEZY TSTAR")
        font.setPointSize(14)
        self.radAntiOff.setFont(font)
        self.radAntiOff.setObjectName("radAntiOff")
        self.txtAPIKeyANTI = QtWidgets.QLineEdit(self.groupBox_2)
        self.txtAPIKeyANTI.setGeometry(QtCore.QRect(130, 34, 241, 22))
        font = QtGui.QFont()
        font.setFamily("YEEZY TSTAR")
        font.setPointSize(14)
        self.txtAPIKeyANTI.setFont(font)
        self.txtAPIKeyANTI.setObjectName("txtAPIKeyANTI")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 170, 321, 21))
        font = QtGui.QFont()
        font.setFamily("YEEZY TSTAR")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 200, 181, 21))
        font = QtGui.QFont()
        font.setFamily("YEEZY TSTAR")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 230, 181, 21))
        font = QtGui.QFont()
        font.setFamily("YEEZY TSTAR")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.txtURL = QtWidgets.QLineEdit(Dialog)
        self.txtURL.setGeometry(QtCore.QRect(122, 200, 251, 22))
        font = QtGui.QFont()
        font.setFamily("YEEZY TSTAR")
        font.setPointSize(14)
        self.txtURL.setFont(font)
        self.txtURL.setObjectName("txtURL")
        self.txtSitekey = QtWidgets.QLineEdit(Dialog)
        self.txtSitekey.setGeometry(QtCore.QRect(122, 230, 251, 22))
        font = QtGui.QFont()
        font.setFamily("YEEZY TSTAR")
        font.setPointSize(14)
        self.txtSitekey.setFont(font)
        self.txtSitekey.setObjectName("txtSitekey")
        self.boxSolvers = QtWidgets.QSpinBox(Dialog)
        self.boxSolvers.setGeometry(QtCore.QRect(325, 170, 47, 23))
        font = QtGui.QFont()
        font.setFamily("YEEZY TSTAR")
        font.setPointSize(14)
        self.boxSolvers.setFont(font)
        self.boxSolvers.setObjectName("boxSolvers")
        self.btnStart = QtWidgets.QPushButton(Dialog)
        self.btnStart.setGeometry(QtCore.QRect(290, 260, 81, 22))
        font = QtGui.QFont()
        font.setFamily("YEEZY TSTAR")
        font.setPointSize(14)
        self.btnStart.setFont(font)
        self.btnStart.setAutoDefault(False)
        self.btnStart.setObjectName("btnStart")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(0, 150, 401, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.btnStop = QtWidgets.QPushButton(Dialog)
        self.btnStop.setGeometry(QtCore.QRect(200, 260, 81, 22))
        font = QtGui.QFont()
        font.setFamily("YEEZY TSTAR")
        font.setPointSize(14)
        self.btnStop.setFont(font)
        self.btnStop.setAutoDefault(False)
        self.btnStop.setObjectName("btnStop")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Captcha Engine"))
        self.groupBox.setTitle(_translate("Dialog", "2Captcha"))
        self.rad2CapOn.setText(_translate("Dialog", "On"))
        self.rad2CapOff.setText(_translate("Dialog", "Off"))
        self.groupBox_2.setTitle(_translate("Dialog", "Anti-Captcha"))
        self.radAntiOn.setText(_translate("Dialog", "On"))
        self.radAntiOff.setText(_translate("Dialog", "Off"))
        self.label.setText(_translate("Dialog", "Concurrent Solvers per Service"))
        self.label_2.setText(_translate("Dialog", "URL"))
        self.label_3.setText(_translate("Dialog", "Sitekey"))
        self.btnStart.setText(_translate("Dialog", "Start"))
        self.btnStop.setText(_translate("Dialog", "Stop"))
        self.txtAPIKeyANTI.setDisabled(True)
        self.txtAPIKey2CAP.setDisabled(True)
        self.radAntiOn.toggled.connect(self.checkAnti)
        self.rad2CapOn.toggled.connect(self.check2Cap)
        self.btnStart.clicked.connect(self.getRecaptcha)
        self.btnStop.clicked.connect(self.stopRecaptcha)

    def checkAnti(self):
        if self.radAntiOn.isChecked():
            self.txtAPIKeyANTI.setDisabled(False)
        elif self.radAntiOff.isChecked():
            self.txtAPIKeyANTI.setDisabled(True)

    def check2Cap(self):
        if self.rad2CapOn.isChecked():
            self.txtAPIKey2CAP.setDisabled(False)
        elif self.rad2CapOff.isChecked():
            self.txtAPIKey2CAP.setDisabled(True)

    def getRecaptcha(self):
        global solve
        self.current = 0
        solve = True
        self.maxcount = int(self.boxSolvers.text())
        self.antithread = [None] * self.maxcount
        self.twothread = [None] * self.maxcount
        self.antithreadstatus = [None] * self.maxcount
        self.twothreadstatus = [None] * self.maxcount

        while self.current < self.maxcount:
            if self.radAntiOn.isChecked():
                self.antithread[self.current] = antiCaptcha(self.txtAPIKeyANTI.text(), self.txtSitekey.text(), self.txtURL.text())
                self.antithread[self.current].start()
                self.antithreadstatus[self.current] = True
            if self.rad2CapOn.isChecked():
                self.twothread[self.current] = twoCaptcha(self.txtAPIKeyANTI.text(), self.txtSitekey.text(), self.txtURL.text())
                self.twothread[self.current].start()
                self.twothreadstatus[self.current] = True
            self.current += 1

    def stopRecaptcha(self):
        global solve
        solve = False


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
