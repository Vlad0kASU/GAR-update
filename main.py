import GUI_FIAS
import csv_to_ctl_1_2
import xml_to_csv_3_0
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import *
from time import sleep
import sys
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
import traceback
import os


class WorkerSignals(QObject):
    ''' Определяет сигналы, доступные из рабочего рабочего потока Worker(QRunnable).'''

    finish = pyqtSignal()
    error = pyqtSignal(tuple)
    result = pyqtSignal(object)
    progress = pyqtSignal(int)


class Worker(QRunnable):
    ''' Наследует от QRunnable, настройки рабочего потока обработчика, сигналов и wrap-up. '''

    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()

        # Хранить аргументы конструктора (повторно используемые для обработки)
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()

        # == Добавьте обратный вызов в наши kwargs ====================================###
        kwargs['progress_callback'] = self.signals.progress

    @pyqtSlot()
    def run(self):
        # Получите args/kwargs здесь; и обработка с их использованием
        try:  # выполняем метод `some_func` переданный из Main
            result = self.fn(*self.args, **self.kwargs)
        except:
            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            self.signals.error.emit((exctype, value, traceback.format_exc()))
        else:  # если ошибок не была, испускаем сигнал .result и передаем результат `result`
            self.signals.result.emit(result)  # Вернуть результат обработки
        finally:
            self.signals.finish.emit()  # Done / Готово

class MyPushButton(QtWidgets.QPushButton):
    def __init__(self, name, App, parent=None):
        super(MyPushButton, self).__init__(parent)
        self.setMinimumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.setFont(font)
        self.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                           "border-color: rgb(0, 0, 0);\n"
                           "border : solid black;\n"
                           "border-width : 2px 2px 2px 2px;\n"
                           "\n"
                           "")
        self.setObjectName(name)
        self.name = name
        self.setText(name[name.rfind('\\')+1:])
        self.clicked.connect(self.dirClick)
        self.App = App

    backslash = '\\'
    def dirClick(self):
        global dictButton
        for i in dictButton.values():
            i.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                           "border-color: rgb(0, 0, 0);\n"
                           "border : solid black;\n"
                           "border-width : 2px 2px 2px 2px;\n"
                           "\n"
                           "")
        self.setStyleSheet("background-color: rgb(0, 77, 230);\n"
                           "color: rgb(255, 255, 255);\n"
                           "border-color: rgb(0, 0, 0);\n"
                           "border : solid black;\n"
                           "border-width : 2px 2px 2px 2px;\n"
                           "\n"
                           "")
        try:
            os.chdir(self.name)
        except:
            try:
                os.chdir('..')
                os.chdir(self.name)
            except:
                pass

        self.App.placeCheckBox()

class App(QtWidgets.QMainWindow, GUI_FIAS.Ui_MainWindow):
    """
    Класс для gui приложения
    """
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.dirname = os.getcwd()
        self.dirfiles = os.listdir(self.dirname)
        self.fullpaths = map(lambda name: os.path.join(self.dirname, name), self.dirfiles)
        self.dirs = []
        self.dirs.append(os.getcwd())
        self.files = []
        for file in self.fullpaths:
            if os.path.isdir(file):
                self.dirs.append(file)
            if os.path.isfile(file) and (file.lower().endswith('xml') or file.lower().endswith('csv')):
                self.files.append(file)
        self.allButton.clicked.connect(self.allButtonClick)
        self.xmlButton.clicked.connect(self.xmlButtonClick)
        self.csvButton.clicked.connect(self.csvButtonClick)
        self.sort = 'all'
        self.dictCheckBox = {}
        # self.testButton = MyPushButton('test', self.dictCheckBox, self, self.scrollAreaWidgetContents)
        # self.verticalLayout.addWidget(self.testButton)

    def placeCheckBox(self):
        n = 0
        for i in self.dictCheckBox.values():
            self.gridLayout_4.removeWidget(i)
            n += 1
        dirname = os.getcwd()
        dirfiles = os.listdir(dirname)
        fullpaths = map(lambda name: os.path.join(dirname, name), dirfiles)

        files = []
        if self.sort == 'all':
            for file in fullpaths:
                if os.path.isfile(file) and (file.lower().endswith('xml') or file.lower().endswith('csv')):
                    files.append(file)
        elif self.sort == 'xml':
            for file in fullpaths:
                if os.path.isfile(file) and file.lower().endswith('xml'):
                    files.append(file)
        elif self.sort == 'csv':
            for file in fullpaths:
                if os.path.isfile(file) and file.lower().endswith('csv'):
                    files.append(file)

        self.dictCheckBox = {}
        n = 0
        for i in files:
            self.dictCheckBox[i] = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_2)
            tempCheckBox = self.dictCheckBox[i]
            tempCheckBox.setMinimumSize(QtCore.QSize(0, 30))
            font = QtGui.QFont()
            font.setFamily("Times New Roman")
            font.setPointSize(16)
            font.setBold(False)
            font.setWeight(50)
            tempCheckBox.setFont(font)
            tempCheckBox.setTabletTracking(False)
            tempCheckBox.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                            "border-color: rgb(0, 0, 0);\n"
                                            "border : solid black;\n"
                                            "border-width : 1px 1px 1px 1px;\n"
                                            "\n"
                                            "")
            tempCheckBox.setObjectName("tempCheckBox")
            self.gridLayout_4.addWidget(tempCheckBox, n, 0, 1, 1)
            self.dictCheckBox[i] = tempCheckBox
            self.dictCheckBox[i].setText(i[i.rfind('\\')+1:])
            n += 1

    def allButtonClick(self):
        self.sort = 'all'
        self.allButton.setStyleSheet("background-color: rgb(0, 77, 230);\n"
                                     "alternate-background-color: rgb(255, 0, 255);\n"
                                     "color: rgb(255, 255, 255);\n"
                                     "border-color: rgb(0, 0, 0);\n"
                                     "border : solid black;\n"
                                     "border-width : 2px 2px 2px 2px;\n"
                                     "\n"
                                     "")
        self.xmlButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                     "border-color: rgb(0, 0, 0);\n"
                                     "border : solid black;\n"
                                     "border-width : 2px 2px 2px 2px;\n"
                                     "\n"
                                     "")
        self.csvButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                     "border-color: rgb(0, 0, 0);\n"
                                     "border : solid black;\n"
                                     "border-width : 2px 2px 2px 2px;\n"
                                     "\n"
                                     "")
        self.placeCheckBox()

    def xmlButtonClick(self):
        self.sort = 'xml'
        self.allButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                     "border-color: rgb(0, 0, 0);\n"
                                     "border : solid black;\n"
                                     "border-width : 2px 2px 2px 2px;\n"
                                     "\n"
                                     "")

        self.xmlButton.setStyleSheet("background-color: rgb(0, 77, 230);\n"
                                     "alternate-background-color: rgb(255, 0, 255);\n"
                                     "color: rgb(255, 255, 255);\n"
                                     "border-color: rgb(0, 0, 0);\n"
                                     "border : solid black;\n"
                                     "border-width : 2px 2px 2px 2px;\n"
                                     "\n"
                                     "")
        self.csvButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                     "border-color: rgb(0, 0, 0);\n"
                                     "border : solid black;\n"
                                     "border-width : 2px 2px 2px 2px;\n"
                                     "\n"
                                     "")
        self.placeCheckBox()

    def csvButtonClick(self):
        self.sort = 'csv'
        self.allButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                     "border-color: rgb(0, 0, 0);\n"
                                     "border : solid black;\n"
                                     "border-width : 2px 2px 2px 2px;\n"
                                     "\n"
                                     "")
        self.xmlButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                     "border-color: rgb(0, 0, 0);\n"
                                     "border : solid black;\n"
                                     "border-width : 2px 2px 2px 2px;\n"
                                     "\n"
                                     "")
        self.csvButton.setStyleSheet("background-color: rgb(0, 77, 230);\n"
                                     "alternate-background-color: rgb(255, 0, 255);\n"
                                     "color: rgb(255, 255, 255);\n"
                                     "border-color: rgb(0, 0, 0);\n"
                                     "border : solid black;\n"
                                     "border-width : 2px 2px 2px 2px;\n"
                                     "\n"
                                     "")
        self.placeCheckBox()



def main():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = App()
    MainWindow.placeCheckBox()
    global dictButton
    dictButton = {}
    for i in MainWindow.dirs:
        dictButton[i] = MyPushButton(i, MainWindow, MainWindow.scrollAreaWidgetContents)
        MainWindow.verticalLayout.addWidget(dictButton[i])
    dictButton[os.getcwd()].setStyleSheet("background-color: rgb(0, 77, 230);\n"
                                          "color: rgb(255, 255, 255);\n"
                                          "border-color: rgb(0, 0, 0);\n"
                                          "border : solid black;\n"
                                          "border-width : 2px 2px 2px 2px;\n"
                                          "\n"
                                          "")
    MainWindow.show()
    app.exec_()


if __name__ == '__main__':
    main()
