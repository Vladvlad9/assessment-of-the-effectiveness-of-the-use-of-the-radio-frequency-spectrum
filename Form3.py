# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Form3.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Technical_efficiencyWindow(object):
    def setupUi(self, Technical_efficiencyWindow):
        Technical_efficiencyWindow.setObjectName("Technical_efficiencyWindow")
        Technical_efficiencyWindow.resize(672, 522)
        self.centralwidget = QtWidgets.QWidget(Technical_efficiencyWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_Technical_efficiency = QtWidgets.QLabel(self.centralwidget)
        self.label_Technical_efficiency.setGeometry(QtCore.QRect(90, 0, 561, 91))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_Technical_efficiency.setFont(font)
        self.label_Technical_efficiency.setObjectName("label_Technical_efficiency")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(160, 160, 261, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(160, 140, 271, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(80, 160, 81, 16))
        self.label_4.setObjectName("label_4")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(120, 220, 41, 16))
        self.label_7.setObjectName("label_7")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(160, 220, 261, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.buttonBox = QtWidgets.QDialogButtonBox(self.centralwidget)
        self.buttonBox.setGeometry(QtCore.QRect(210, 430, 156, 23))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(160, 200, 271, 16))
        self.label_5.setObjectName("label_5")
        Technical_efficiencyWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Technical_efficiencyWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 672, 21))
        self.menubar.setObjectName("menubar")
        Technical_efficiencyWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Technical_efficiencyWindow)
        self.statusbar.setObjectName("statusbar")
        Technical_efficiencyWindow.setStatusBar(self.statusbar)

        self.retranslateUi(Technical_efficiencyWindow)
        QtCore.QMetaObject.connectSlotsByName(Technical_efficiencyWindow)

    def retranslateUi(self, Technical_efficiencyWindow):
        _translate = QtCore.QCoreApplication.translate
        Technical_efficiencyWindow.setWindowTitle(_translate("Technical_efficiencyWindow", "Техническая эффективность"))
        self.label_Technical_efficiency.setText(_translate("Technical_efficiencyWindow", "Техническая эффективность "))
        self.label_3.setText(_translate("Technical_efficiencyWindow", "Площадь покрытия сетью оператора"))
        self.label_4.setText(_translate("Technical_efficiencyWindow", "S покрытия  ="))
        self.label_7.setText(_translate("Technical_efficiencyWindow", "SРБ ="))
        self.label_5.setText(_translate("Technical_efficiencyWindow", "_"))


