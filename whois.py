import wget
import requests
import bs4
from PyQt5 import QtCore, QtGui, QtWidgets
import time

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1282, 616)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, -10, 1241, 41))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.submit = QtWidgets.QPushButton(self.centralWidget)
        self.submit.setGeometry(QtCore.QRect(570, 60, 92, 36))
        self.submit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.submit.setObjectName("submit")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralWidget)
        self.textBrowser.setGeometry(QtCore.QRect(10, 100, 1241, 421))
        self.textBrowser.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textBrowser.setObjectName("textBrowser")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1282, 28))
        self.menuBar.setObjectName("menuBar")
        self.menuCalculator = QtWidgets.QMenu(self.menuBar)
        self.menuCalculator.setObjectName("menuCalculator")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.menuBar.addAction(self.menuCalculator.menuAction())

        self.retranslateUi(MainWindow)
        self.submit.clicked.connect(self.write)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def write(self):
        a = self.lineEdit.text()
        self.textBrowser.append("querying target=>"+a)
        time.sleep(1)
        req = requests.get("https://www.whois.com/whois/"+a)
        t = bs4.BeautifulSoup(req.text,"html.parser")
        c = t.find_all('pre')
        for i in c:
            self.textBrowser.append(i.text+"\n")
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.submit.setText(_translate("MainWindow", "submit"))
        self.menuCalculator.setTitle(_translate("MainWindow", "calculator"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
