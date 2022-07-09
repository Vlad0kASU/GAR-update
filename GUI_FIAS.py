# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI_FIAS.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1100, 575)
        MainWindow.setMinimumSize(QtCore.QSize(1100, 0))
        icon = QtGui.QIcon.fromTheme("logo2.png")
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(249, 249, 249);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.scrollArea_2.setFont(font)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 874, 425))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.testCheckBox = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_2)
        self.testCheckBox.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.testCheckBox.setFont(font)
        self.testCheckBox.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"border : solid black;\n"
"border-width : 1px 1px 1px 1px;\n"
"\n"
"")
        self.testCheckBox.setObjectName("testCheckBox")
        self.gridLayout_4.addWidget(self.testCheckBox, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_2.setMinimumSize(QtCore.QSize(100, 0))
        self.label_2.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(0, 181, 45);\n"
"background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"border : solid black;\n"
"border-width : 1px 1px 1px 1px;\n"
"\n"
"")
        self.label_2.setObjectName("label_2")
        self.gridLayout_4.addWidget(self.label_2, 0, 1, 1, 1)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.gridLayout_2.addWidget(self.scrollArea_2, 1, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.allButton = QtWidgets.QPushButton(self.centralwidget)
        self.allButton.setMinimumSize(QtCore.QSize(160, 0))
        self.allButton.setMaximumSize(QtCore.QSize(160, 16777215))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.allButton.setFont(font)
        self.allButton.setStyleSheet("background-color: rgb(0, 77, 230);\n"
"alternate-background-color: rgb(255, 0, 255);\n"
"color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"border : solid black;\n"
"border-width : 2px 2px 2px 2px;\n"
"\n"
"")
        self.allButton.setObjectName("allButton")
        self.horizontalLayout.addWidget(self.allButton)
        self.xmlButton = QtWidgets.QPushButton(self.centralwidget)
        self.xmlButton.setMinimumSize(QtCore.QSize(160, 0))
        self.xmlButton.setMaximumSize(QtCore.QSize(160, 16777215))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.xmlButton.setFont(font)
        self.xmlButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"border : solid black;\n"
"border-width : 2px 2px 2px 2px;\n"
"\n"
"")
        self.xmlButton.setObjectName("xmlButton")
        self.horizontalLayout.addWidget(self.xmlButton)
        self.csvButton = QtWidgets.QPushButton(self.centralwidget)
        self.csvButton.setMinimumSize(QtCore.QSize(160, 0))
        self.csvButton.setMaximumSize(QtCore.QSize(160, 16777215))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.csvButton.setFont(font)
        self.csvButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"border : solid black;\n"
"border-width : 2px 2px 2px 2px;\n"
"\n"
"")
        self.csvButton.setObjectName("csvButton")
        self.horizontalLayout.addWidget(self.csvButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 1, 1, 1)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setMaximumSize(QtCore.QSize(200, 16777215))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 198, 425))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.choisedDirButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.choisedDirButton.setMinimumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.choisedDirButton.setFont(font)
        self.choisedDirButton.setStyleSheet("background-color: rgb(0, 77, 230);\n"
"color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"border : solid black;\n"
"border-width : 2px 2px 2px 2px;\n"
"\n"
"")
        self.choisedDirButton.setObjectName("choisedDirButton")
        self.verticalLayout.addWidget(self.choisedDirButton)
        self.notChoisedDirButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.notChoisedDirButton.setMinimumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.notChoisedDirButton.setFont(font)
        self.notChoisedDirButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"border : solid black;\n"
"border-width : 2px 2px 2px 2px;\n"
"\n"
"")
        self.notChoisedDirButton.setObjectName("notChoisedDirButton")
        self.verticalLayout.addWidget(self.notChoisedDirButton)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_2.addWidget(self.scrollArea, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(180, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.convertCsvChoisedButton = QtWidgets.QPushButton(self.centralwidget)
        self.convertCsvChoisedButton.setMinimumSize(QtCore.QSize(240, 30))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.convertCsvChoisedButton.setFont(font)
        self.convertCsvChoisedButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"border : solid black;\n"
"border-width : 1px 1px 1px 1px;\n"
"\n"
"")
        self.convertCsvChoisedButton.setObjectName("convertCsvChoisedButton")
        self.gridLayout_3.addWidget(self.convertCsvChoisedButton, 0, 1, 1, 1)
        self.convertCsvAllButton = QtWidgets.QPushButton(self.centralwidget)
        self.convertCsvAllButton.setMinimumSize(QtCore.QSize(240, 30))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.convertCsvAllButton.setFont(font)
        self.convertCsvAllButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"border : solid black;\n"
"border-width : 1px 1px 1px 1px;\n"
"\n"
"")
        self.convertCsvAllButton.setObjectName("convertCsvAllButton")
        self.gridLayout_3.addWidget(self.convertCsvAllButton, 1, 1, 1, 1)
        self.loadBdAllButton = QtWidgets.QPushButton(self.centralwidget)
        self.loadBdAllButton.setMinimumSize(QtCore.QSize(240, 30))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.loadBdAllButton.setFont(font)
        self.loadBdAllButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"border : solid black;\n"
"border-width : 1px 1px 1px 1px;\n"
"\n"
"")
        self.loadBdAllButton.setObjectName("loadBdAllButton")
        self.gridLayout_3.addWidget(self.loadBdAllButton, 1, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem2, 0, 0, 1, 1)
        self.loadBdChoisedButton = QtWidgets.QPushButton(self.centralwidget)
        self.loadBdChoisedButton.setMinimumSize(QtCore.QSize(240, 30))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.loadBdChoisedButton.setFont(font)
        self.loadBdChoisedButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"border : solid black;\n"
"border-width : 1px 1px 1px 1px;\n"
"\n"
"")
        self.loadBdChoisedButton.setObjectName("loadBdChoisedButton")
        self.gridLayout_3.addWidget(self.loadBdChoisedButton, 0, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem3, 0, 3, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_3, 2, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Парсер ФИАС"))
        self.testCheckBox.setText(_translate("MainWindow", "AS_ROOM_TYPES_20220317_9c4a3e2b-231d-48a0-9239-74ce32536b7a.XML"))
        self.label_2.setText(_translate("MainWindow", "12500|12500"))
        self.allButton.setText(_translate("MainWindow", "ALL"))
        self.xmlButton.setText(_translate("MainWindow", "XML"))
        self.csvButton.setText(_translate("MainWindow", "CSV"))
        self.choisedDirButton.setText(_translate("MainWindow", "PushButton"))
        self.notChoisedDirButton.setText(_translate("MainWindow", "PushButton"))
        self.label.setText(_translate("MainWindow", "Список директорий"))
        self.convertCsvChoisedButton.setText(_translate("MainWindow", "Конвертировать в CSV выбранное"))
        self.convertCsvAllButton.setText(_translate("MainWindow", "Конвертировать в CSV все"))
        self.loadBdAllButton.setText(_translate("MainWindow", "Загрузить в БД все"))
        self.loadBdChoisedButton.setText(_translate("MainWindow", "Загрузить в БД выбранное"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())