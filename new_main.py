import sys
from PyQt5 import QtCore, QtGui, QtWidgets

from FormsPy.Form1 import Ui_MainWindow
from FormsPy.Form2 import Ui_EconomicEfficiencyWindow
from FormsPy.Form3 import Ui_Technical_efficiencyWindow
from FormsPy.Form4 import Ui_Social_Efficiency_Window
from db import DBApi

class WindowForm(QtWidgets.QMainWindow):
    def __init__(self):
        super(WindowForm, self).__init__()
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def ShowForm3(self):
        self.ui = Ui_Technical_efficiencyWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def ShowForm2(self):
        self.ui = Ui_EconomicEfficiencyWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def ShowForm4(self):
        self.ui = Ui_Social_Efficiency_Window()
        self.ui.setupUi(self.window)
        self.window.show()

    def showC1(self):
        self.ui.ButtonC1.clicked.connect(self.ShowForm3)

    def showC2(self):
        self.ui.ButtonC2.clicked.connect(self.ShowForm2)

    def showC3(self):
        self.ui.ButtonC3.clicked.connect(self.ShowForm4)




app = QtWidgets.QApplication([])
application = WindowForm()
application.show()

application.showC1()
application.showC2()
application.showC3()


sys.exit(app.exec_())
