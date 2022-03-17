import sys
from PyQt5 import QtWidgets

from FormsPy.Form1 import Ui_MainWindow
from FormsPy.Form2 import Ui_EconomicEfficiencyWindow
from FormsPy.Form3 import Ui_Technical_efficiencyWindow
from FormsPy.Form4 import Ui_Social_Efficiency_Window

from db import DBApi

db = DBApi()
#db.create_all_database()

app = QtWidgets.QApplication(sys.argv)
Dialog = QtWidgets.QDialog()
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()


def openEconomicEfficiencyWindow():  # C2
    global EconomicEfficiencyWindow
    EconomicEfficiencyWindow = QtWidgets.QMainWindow()
    ui = Ui_EconomicEfficiencyWindow()
    ui.setupUi(EconomicEfficiencyWindow)
    Dialog.close()
    EconomicEfficiencyWindow.show()


ui.ButtonC2.clicked.connect(openEconomicEfficiencyWindow)


def openTechnical_efficiencyWindow():  # C1
    global Technical_efficiencyWindow
    Technical_efficiencyWindow = QtWidgets.QMainWindow()
    ui123 = Ui_Technical_efficiencyWindow()
    ui123.setupUi(Technical_efficiencyWindow)
    Technical_efficiencyWindow.show()

    ui123.select_value()
    ui123.ResultButton_click()


ui.ButtonC1.clicked.connect(openTechnical_efficiencyWindow)


def openUi_Social_Efficiency_Window():  # C3
    global Social_Efficiency_Window
    Social_Efficiency_Window = QtWidgets.QMainWindow()
    ui1 = Ui_Social_Efficiency_Window()
    ui1.setupUi(Social_Efficiency_Window)
    Social_Efficiency_Window.show()




ui.ButtonC3.clicked.connect(openUi_Social_Efficiency_Window)

sys.exit(app.exec_())
