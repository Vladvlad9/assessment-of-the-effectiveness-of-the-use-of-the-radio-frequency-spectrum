# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Form1.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(826, 430)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(50, 20, 729, 224))
        self.widget.setObjectName("widget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.ButtonC3 = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.ButtonC3.setFont(font)
        self.ButtonC3.setObjectName("ButtonC3")
        self.gridLayout.addWidget(self.ButtonC3, 0, 5, 1, 1)
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(34)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.ButtonC2 = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.ButtonC2.setFont(font)
        self.ButtonC2.setObjectName("ButtonC2")
        self.gridLayout.addWidget(self.ButtonC2, 0, 3, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(34)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 4, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(34)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)
        self.ButtonC1 = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.ButtonC1.setFont(font)
        self.ButtonC1.setObjectName("ButtonC1")
        self.gridLayout.addWidget(self.ButtonC1, 0, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 1, 0, 1, 1)
        self.label_Title = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_Title.setFont(font)
        self.label_Title.setObjectName("label_Title")
        self.gridLayout_3.addWidget(self.label_Title, 0, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_AnswerE = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(34)
        self.label_AnswerE.setFont(font)
        self.label_AnswerE.setText("")
        self.label_AnswerE.setTextInteractionFlags(
            QtCore.Qt.LinksAccessibleByMouse | QtCore.Qt.TextSelectableByKeyboard | QtCore.Qt.TextSelectableByMouse)
        self.label_AnswerE.setObjectName("label_AnswerE")
        self.gridLayout_2.addWidget(self.label_AnswerE, 0, 0, 1, 1)
        self.label_Answer_C1 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(34)
        self.label_Answer_C1.setFont(font)
        self.label_Answer_C1.setText("")
        self.label_Answer_C1.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label_Answer_C1.setObjectName("label_Answer_C1")
        self.gridLayout_2.addWidget(self.label_Answer_C1, 0, 1, 1, 1)
        self.label_Answer_C2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(34)
        self.label_Answer_C2.setFont(font)
        self.label_Answer_C2.setText("")
        self.label_Answer_C2.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label_Answer_C2.setObjectName("label_Answer_C2")
        self.gridLayout_2.addWidget(self.label_Answer_C2, 0, 2, 1, 1)
        self.label_Answer_C3 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(34)
        self.label_Answer_C3.setFont(font)
        self.label_Answer_C3.setText("")
        self.label_Answer_C3.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label_Answer_C3.setObjectName("label_Answer_C3")
        self.gridLayout_2.addWidget(self.label_Answer_C3, 0, 3, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 2, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 826, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(
            _translate("MainWindow", "Оценка эффективности использования радиочастотного спектра"))
        self.ButtonC3.setText(_translate("MainWindow", "C3"))
        self.label.setText(_translate("MainWindow", "E = "))
        self.ButtonC2.setText(_translate("MainWindow", "C2"))
        self.label_3.setText(_translate("MainWindow", "  +"))
        self.label_2.setText(_translate("MainWindow", "  +"))
        self.ButtonC1.setText(_translate("MainWindow", "C1"))
        self.label_Title.setText(_translate("MainWindow", "Оценка эффективности использования\n"
                                                          "радиочастотного спектра"))


