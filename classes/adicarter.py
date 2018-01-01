from PyQt5 import QtCore, QtGui, QtWidgets
from classes import adidas
from datetime import datetime
import random, time

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1281, 498)
        self.txtSKU = QtWidgets.QLineEdit(Dialog)
        self.txtSKU.setGeometry(QtCore.QRect(90, 388, 191, 21))
        font = QtGui.QFont()
        font.setFamily("YEEZY TSTAR")
        font.setPointSize(14)
        self.txtSKU.setFont(font)
        self.txtSKU.setObjectName("txtSKU")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 390, 60, 16))
        font = QtGui.QFont()
        font.setFamily("YEEZY TSTAR")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.boxSize = QtWidgets.QComboBox(Dialog)
        self.boxSize.setGeometry(QtCore.QRect(90, 418, 191, 26))
        font = QtGui.QFont()
        font.setFamily("YEEZY TSTAR")
        font.setPointSize(14)
        self.boxSize.setFont(font)
        self.boxSize.setObjectName("boxSize")
        self.boxSize.addItem("")
        self.boxSize.addItem("")
        self.boxSize.addItem("")
        self.boxSize.addItem("")
        self.boxSize.addItem("")
        self.boxSize.addItem("")
        self.boxSize.addItem("")
        self.boxSize.addItem("")
        self.boxSize.addItem("")
        self.boxSize.addItem("")
        self.boxSize.addItem("")
        self.boxSize.addItem("")
        self.boxSize.addItem("")
        self.boxSize.addItem("")
        self.boxSize.addItem("")
        self.boxSize.addItem("")
        self.boxSize.addItem("")
        self.boxSize.addItem("")
        self.boxSize.addItem("")
        self.boxSize.addItem("")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 422, 60, 16))
        font = QtGui.QFont()
        font.setFamily("YEEZY TSTAR")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.btnAddTask = QtWidgets.QPushButton(Dialog)
        self.btnAddTask.setGeometry(QtCore.QRect(20, 460, 261, 32))
        font = QtGui.QFont()
        font.setFamily("YEEZY TSTAR")
        font.setPointSize(14)
        self.btnAddTask.setFont(font)
        self.btnAddTask.setAutoDefault(False)
        self.btnAddTask.setObjectName("btnAddTask")
        self.tableProxies = QtWidgets.QTableWidget(Dialog)
        self.tableProxies.setGeometry(QtCore.QRect(20, 11, 261, 321))
        font = QtGui.QFont()
        font.setFamily("YEEZY TSTAR")
        font.setPointSize(10)
        self.tableProxies.setFont(font)
        self.tableProxies.setObjectName("tableProxies")
        self.tableProxies.setColumnCount(2)
        self.tableProxies.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableProxies.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableProxies.setHorizontalHeaderItem(1, item)
        self.tableProxies.horizontalHeader().setDefaultSectionSize(115)
        self.tableProxies.horizontalHeader().setStretchLastSection(True)
        self.btnProxies = QtWidgets.QPushButton(Dialog)
        self.btnProxies.setGeometry(QtCore.QRect(20, 340, 261, 32))
        font = QtGui.QFont()
        font.setFamily("YEEZY TSTAR")
        font.setPointSize(14)
        self.btnProxies.setFont(font)
        self.btnProxies.setAutoDefault(False)
        self.btnProxies.setObjectName("btnProxies")
        self.tableTasks = QtWidgets.QTableWidget(Dialog)
        self.tableTasks.setGeometry(QtCore.QRect(300, 10, 971, 441))
        font = QtGui.QFont()
        font.setFamily("YEEZY TSTAR")
        font.setPointSize(10)
        self.tableTasks.setFont(font)
        self.tableTasks.setObjectName("tableTasks")
        self.tableTasks.setColumnCount(4)
        self.tableTasks.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableTasks.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableTasks.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableTasks.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableTasks.setHorizontalHeaderItem(3, item)
        self.tableTasks.horizontalHeader().setDefaultSectionSize(130)
        self.tableTasks.horizontalHeader().setStretchLastSection(True)
        self.timeStart = QtWidgets.QTimeEdit(Dialog)
        self.timeStart.setGeometry(QtCore.QRect(1150, 463, 118, 24))
        font = QtGui.QFont()
        font.setFamily("YEEZY TSTAR")
        font.setPointSize(14)
        self.timeStart.setFont(font)
        self.timeStart.setObjectName("timeStart")
        self.btnStartTask = QtWidgets.QPushButton(Dialog)
        self.btnStartTask.setGeometry(QtCore.QRect(1022, 460, 121, 32))
        font = QtGui.QFont()
        font.setFamily("YEEZY TSTAR")
        font.setPointSize(14)
        self.btnStartTask.setFont(font)
        self.btnStartTask.setAutoDefault(False)
        self.btnStartTask.setObjectName("btnStartTask")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(0, 370, 291, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(Dialog)
        self.line_2.setGeometry(QtCore.QRect(280, 0, 20, 501))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dyspo"))
        self.label.setText(_translate("Dialog", "SKU"))
        self.boxSize.setItemText(0, _translate("Dialog", "4.0"))
        self.boxSize.setItemText(1, _translate("Dialog", "4.5"))
        self.boxSize.setItemText(2, _translate("Dialog", "5.0"))
        self.boxSize.setItemText(3, _translate("Dialog", "5.5"))
        self.boxSize.setItemText(4, _translate("Dialog", "6.0"))
        self.boxSize.setItemText(5, _translate("Dialog", "6.5"))
        self.boxSize.setItemText(6, _translate("Dialog", "7.0"))
        self.boxSize.setItemText(7, _translate("Dialog", "7.5"))
        self.boxSize.setItemText(8, _translate("Dialog", "8.0"))
        self.boxSize.setItemText(9, _translate("Dialog", "8.5"))
        self.boxSize.setItemText(10, _translate("Dialog", "9.0"))
        self.boxSize.setItemText(11, _translate("Dialog", "9.5"))
        self.boxSize.setItemText(12, _translate("Dialog", "10.0"))
        self.boxSize.setItemText(13, _translate("Dialog", "10.5"))
        self.boxSize.setItemText(14, _translate("Dialog", "11.0"))
        self.boxSize.setItemText(15, _translate("Dialog", "11.5"))
        self.boxSize.setItemText(16, _translate("Dialog", "12.0"))
        self.boxSize.setItemText(17, _translate("Dialog", "12.5"))
        self.boxSize.setItemText(18, _translate("Dialog", "13.0"))
        self.boxSize.setItemText(19, _translate("Dialog", "FSR"))
        self.label_2.setText(_translate("Dialog", "Size"))
        self.btnAddTask.setText(_translate("Dialog", "Add Task"))
        item = self.tableProxies.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Type"))
        item = self.tableProxies.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Address"))
        self.btnProxies.setText(_translate("Dialog", "Load Proxies"))
        item = self.tableTasks.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Status"))
        item = self.tableTasks.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "SKU"))
        item = self.tableTasks.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Size"))
        item = self.tableTasks.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Proxy"))
        self.btnStartTask.setText(_translate("Dialog", "Start Tasks @"))
        self.threads = [None] * 9999
        self.btnAddTask.clicked.connect(self.addtasks)
        self.btnStartTask.clicked.connect(self.starttask)
        self.btnProxies.clicked.connect(self.loadproxies)

    def loadproxies(self):
        directory = QtWidgets.QFileDialog.getOpenFileName()[0]
        proxylist = []
        with open(directory, 'r') as g:
            for line in g:
                item = {'type' : line[0:line.find('://')].replace('\n', ''), 'address' : line[line.find('://')+3:].replace('\n', '')}
                proxylist.append(item)
        for item in proxylist:
            height = self.tableProxies.rowCount()
            self.tableProxies.insertRow(height)
            self.tableProxies.setItem(height, 0, QtWidgets.QTableWidgetItem(item['type']))
            self.tableProxies.setItem(height, 1, QtWidgets.QTableWidgetItem(item['address']))

    def addtasks(self):
        height = self.tableProxies.rowCount()
        index = 0
        while index < height:
            self.tableTasks.insertRow(index)
            self.tableTasks.setItem(index, 0, QtWidgets.QTableWidgetItem('Not Started'))
            self.tableTasks.setItem(index, 1, QtWidgets.QTableWidgetItem(self.txtSKU.text()))
            if self.boxSize.currentText().lower() == 'fsr':
                self.tableTasks.setItem(index, 2, QtWidgets.QTableWidgetItem(random.choice(['4.0','4.5','5.0','5.5','6.0','6.5','7.0','7.5','8.0','8.5','9.0','9.5','10.0','10.5','11.0','11.5','12.0','12.5','13.0'])))
            else:
                self.tableTasks.setItem(index, 2, QtWidgets.QTableWidgetItem(self.boxSize.currentText()))
            if self.tableProxies.item(index, 0).text().lower() == 'socks5':
                self.tableTasks.setItem(index, 3, QtWidgets.QTableWidgetItem('socks5://' + self.tableProxies.item(index, 1).text()))
            elif self.tableProxies.item(index, 0).text().lower() == 'http':
                self.tableTasks.setItem(index, 3, QtWidgets.QTableWidgetItem('http://' + self.tableProxies.item(index, 1).text()))
            index += 1

    def starttask(self):
        height = self.tableTasks.rowCount()
        index = 0
        starttime = datetime.strptime(self.timeStart.text(), '%I:%M %p')
        while index < height:
            self.threads[index] = adiCart(self.tableTasks.item(index, 1).text(), self.tableTasks.item(index, 2).text(), self.tableTasks.item(index, 3).text(), starttime, index)
            self.threads[index].status.connect(self.updateTasks)
            self.threads[index].start()
            index += 1

    def updateTasks(self, data):
        self.tableTasks.setItem(data[1], 0, QtWidgets.QTableWidgetItem(data[0]))

class adiCart(QtCore.QThread):
    status = QtCore.pyqtSignal(object)

    def __init__(self, sku, size, proxy, starttime, height):
        QtCore.QThread.__init__(self)
        self.sku = sku
        self.size = size
        self.proxy = proxy
        self.starttime = starttime
        self.height = height

    def run(self):
        self.status.emit(['Initializing', self.height])
        self.s = adidas.adidas('US', self.proxy)
        self.s.setupatc(self.sku)
        self.status.emit(['Waiting...', self.height])
        while True:
            if datetime.now() > self.starttime:
                break
        while True:
            checkstock = self.s.checkstock(self.sku, self.size)
            if checkstock:
                self.status.emit(['In Stock, Carting...', self.height])
                break
            elif checkstock == False:
                self.status.emit(['OOS, Waiting', self.height])
                time.sleep(5)
        self.status.emit(['Need Recap Token!', self.height])
        while True:
            if self.s.atcwrecaptcha(self.sku, self.size):
                break
            else:
                self.status.emit(['Failed Cart, Retrying...', self.height])
        self.status.emit(['Carted', self.height])
        self.s.opencart()
        self.s.chrome.get('https://www.adidas.com/on/demandware.store/Sites-adidas-US-Site/en_US/Cart-Show')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
