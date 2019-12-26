import pyautogui
import storagedata
import os.path
from os import makedirs
from time import sleep
from pathlib import Path
# UI
from PyQt5 import QtCore, QtGui, QtWidgets
import sys


# File Locations
doc_file = r"..\data\doc.txt"
value_file = r"..\data\value.txt"
cmd_file = r"..\data\cmd.txt"

pyautogui.PAUSE = 1

usr_cmd = None
usr_line = 1

# ----------------------------------------------------------------

def writeUsrIn(doc, value, line):
    global usr_cmd, usr_line

    if usr_cmd == "click":
        x, y = pyautogui.position()
        value = str(x) +" " + str(y)
    elif usr_cmd == "moveto":
        x, y = pyautogui.position()
        value = str(x) +" " + str(y)
    elif usr_cmd == "type":
        if value == "":
            value = pyautogui.prompt("The sentance: ")
    elif usr_cmd == "scroll":
        if value == "":
            value = pyautogui.prompt("How many scroll?")
    elif usr_cmd == "sleep":
        if value == "":
            value = pyautogui.prompt("How long?")
    elif usr_cmd == "manual":
        if value == "":
            value = "manual"
    elif usr_cmd == "copy":
        if value == "":
            value = "copy"
    elif usr_cmd == "paste":
        if value == "":
            value = "paste"
    elif usr_cmd == "stop":
        exit()

    writesDatas(usr_line, value, doc, usr_cmd)
    usr_line += 1

def runData():
    file_length = int(storagedata.readData(cmd_file, option="len"))
    current_line = getCurrentLine()

    while current_line < file_length+1:
        cmd = storagedata.readData(cmd_file, current_line)
        value = storagedata.readData(value_file, current_line)
        doc = storagedata.readData(doc_file, current_line)

        print(current_line, doc)

        if cmd == "click":
            x, y = value.split(" ")
            x, y = int(x), int(y)
            pyautogui.click(x, y)
        elif cmd == "moveto":
            x, y = value.split(" ")
            x, y = int(x), int(y)
            pyautogui.moveTo(x, y)
        elif cmd == "type":
            sleep(1)
            pyautogui.typewrite(value)
            sleep(5)
        elif cmd == "scroll":
            pyautogui.PAUSE = .5
            for i in range(0, int(value)):
                pyautogui.scroll(-500)
            sleep(3)
            pyautogui.PAUSE = 1
        elif cmd == "sleep":
            sleep(int(value))
        elif cmd == "manual":
            pyautogui.confirm("Input manualy. {}".format(value))
        elif cmd == "copy":
            pyautogui.hotkey("ctrl", "c")
        elif cmd == "paste":
            pyautogui.hotkey("ctrl", "v")
        else:
            print(current_line, "Unknown command. Skipping...")
        
        current_line += 1

    pyautogui.confirm("Program finished")

# ----------------------------------------------------------------

def getCurrentLine():
    current_line = input("From line ")

    try:
        current_line = int(current_line)
    except ValueError:
        print("Value error. Starting from line one")
        current_line = 1

    if current_line <= 0:
        current_line = 1

    return current_line

def writesDatas(current_line, value, doc, cmd):
    storagedata.overwriteData(value_file, current_line, value)
    storagedata.overwriteData(doc_file, current_line, doc)
    storagedata.overwriteData(cmd_file, current_line, cmd)

# ----------------------------------------------------------------

def checkDataFileExist():
    if os.path.exists("..\\data") == False:
        makedirs("..\\data")

    if os.path.isfile(doc_file) == False:
        Path(doc_file).touch()

    if os.path.isfile(value_file) == False:
        Path(value_file).touch()

    if os.path.isfile(cmd_file) == False:
        Path(cmd_file).touch()

# Record GUI ----------------------------------------------------------------

class Ui_RecordWindow(object):
    def setupUi(self, MainMenu):
        MainMenu.setObjectName("MainMenu")
        MainMenu.resize(252, 301)
        MainMenu.setMinimumSize(QtCore.QSize(252, 301))
        MainMenu.setMaximumSize(QtCore.QSize(252, 301))
        MainMenu.setStyleSheet("")
        self.clickBtn = QtWidgets.QPushButton(MainMenu)
        self.clickBtn.setGeometry(QtCore.QRect(10, 40, 75, 23))
        self.clickBtn.setCheckable(False)
        self.clickBtn.setDefault(False)
        self.clickBtn.setFlat(False)
        self.clickBtn.setObjectName("clickBtn")
        self.clickBtn.clicked.connect(lambda: self.onClickCmd("click"))
        self.moveToBtn = QtWidgets.QPushButton(MainMenu)
        self.moveToBtn.setGeometry(QtCore.QRect(90, 40, 75, 23))
        self.moveToBtn.setCheckable(False)
        self.moveToBtn.setObjectName("moveToBtn")
        self.moveToBtn.clicked.connect(lambda: self.onClickCmd("moveto"))
        self.typeBtn = QtWidgets.QPushButton(MainMenu)
        self.typeBtn.setGeometry(QtCore.QRect(170, 40, 75, 23))
        self.typeBtn.setObjectName("typeBtn")
        self.typeBtn.clicked.connect(lambda: self.onClickCmd("type"))
        self.scrollBtn = QtWidgets.QPushButton(MainMenu)
        self.scrollBtn.setGeometry(QtCore.QRect(10, 70, 75, 23))
        self.scrollBtn.setObjectName("scrollBtn")
        self.scrollBtn.clicked.connect(lambda: self.onClickCmd("scroll"))
        self.waitBtn = QtWidgets.QPushButton(MainMenu)
        self.waitBtn.setGeometry(QtCore.QRect(90, 70, 75, 23))
        self.waitBtn.setObjectName("waitBtn")
        self.waitBtn.clicked.connect(lambda: self.onClickCmd("sleep"))
        self.manualBtn = QtWidgets.QPushButton(MainMenu)
        self.manualBtn.setGeometry(QtCore.QRect(170, 70, 75, 23))
        self.manualBtn.setObjectName("manualBtn")
        self.manualBtn.clicked.connect(lambda: self.onClickCmd("manual"))
        self.copyBtn = QtWidgets.QPushButton(MainMenu)
        self.copyBtn.setGeometry(QtCore.QRect(10, 100, 75, 23))
        self.copyBtn.setObjectName("copyBtn")
        self.copyBtn.clicked.connect(lambda: self.onClickCmd("copy"))
        self.pasteBtn = QtWidgets.QPushButton(MainMenu)
        self.pasteBtn.setGeometry(QtCore.QRect(90, 100, 75, 23))
        self.pasteBtn.setObjectName("pasteBtn")
        self.pasteBtn.clicked.connect(lambda: self.onClickCmd("paste"))
        self.endBtn = QtWidgets.QPushButton(MainMenu)
        self.endBtn.setGeometry(QtCore.QRect(170, 100, 75, 23))
        self.endBtn.setObjectName("endBtn")
        self.endBtn.clicked.connect(lambda: self.onClickCmd("stop"))
        self.docText = QtWidgets.QPlainTextEdit(MainMenu)
        self.docText.setGeometry(QtCore.QRect(10, 150, 231, 31))
        self.docText.setObjectName("docText")
        self.infoLabel = QtWidgets.QLabel(MainMenu)
        self.infoLabel.setGeometry(QtCore.QRect(10, 240, 231, 31))
        self.infoLabel.setTextFormat(QtCore.Qt.PlainText)
        self.infoLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.infoLabel.setObjectName("infoLabel")
        self.docLabel = QtWidgets.QLabel(MainMenu)
        self.docLabel.setGeometry(QtCore.QRect(10, 130, 81, 16))
        self.docLabel.setObjectName("docLabel")
        self.valueLabel = QtWidgets.QLabel(MainMenu)
        self.valueLabel.setGeometry(QtCore.QRect(10, 190, 121, 16))
        self.valueLabel.setObjectName("valueLabel")
        self.valueText = QtWidgets.QPlainTextEdit(MainMenu)
        self.valueText.setGeometry(QtCore.QRect(10, 210, 231, 31))
        self.valueText.setObjectName("valueText")
        self.okBtn = QtWidgets.QPushButton(MainMenu)
        self.okBtn.setGeometry(QtCore.QRect(40, 270, 75, 23))
        self.okBtn.setObjectName("okBtn")
        self.okBtn.clicked.connect(self.onClickWrite)
        self.pushButton_2 = QtWidgets.QPushButton(MainMenu)
        self.pushButton_2.setGeometry(QtCore.QRect(140, 270, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineSpinBox = QtWidgets.QSpinBox(MainMenu)
        self.lineSpinBox.setGeometry(QtCore.QRect(200, 10, 42, 22))
        self.lineSpinBox.setObjectName("lineSpinBox")
        self.lineSpinBox.setMinimum(1)
        self.label = QtWidgets.QLabel(MainMenu)
        self.label.setGeometry(QtCore.QRect(170, 10, 47, 13))
        self.label.setObjectName("lineLabel")

        self.retranslateUi(MainMenu)
        QtCore.QMetaObject.connectSlotsByName(MainMenu)

    def retranslateUi(self, MainMenu):
        _translate = QtCore.QCoreApplication.translate
        MainMenu.setWindowTitle(_translate("MainMenu", "Pyautogui GUI"))
        self.clickBtn.setToolTip(_translate("MainMenu", "Mouse click"))
        self.clickBtn.setText(_translate("MainMenu", "Click"))
        self.moveToBtn.setToolTip(_translate("MainMenu", "Mouse move to"))
        self.moveToBtn.setText(_translate("MainMenu", "Move to"))
        self.typeBtn.setText(_translate("MainMenu", "Type"))
        self.scrollBtn.setText(_translate("MainMenu", "Scroll"))
        self.waitBtn.setText(_translate("MainMenu", "Wait"))
        self.manualBtn.setToolTip(_translate("MainMenu", "User input needed"))
        self.manualBtn.setText(_translate("MainMenu", "Manual"))
        self.copyBtn.setToolTip(_translate("MainMenu", "Copy selected text"))
        self.copyBtn.setText(_translate("MainMenu", "Copy"))
        self.pasteBtn.setToolTip(_translate("MainMenu", "Paste text"))
        self.pasteBtn.setText(_translate("MainMenu", "Paste"))
        self.endBtn.setToolTip(_translate("MainMenu", "End this program"))
        self.endBtn.setText(_translate("MainMenu", "End"))
        self.infoLabel.setText(_translate("MainMenu", "Move your mouse to the position.\nBefore pressing enter."))
        self.docLabel.setText(_translate("MainMenu", "Documentation"))
        self.valueLabel.setText(_translate("MainMenu", "Value - Type, Scroll, Wait"))
        self.okBtn.setText(_translate("MainMenu", "OK"))
        self.okBtn.setShortcut(_translate("MainMenu", "Return"))
        self.pushButton_2.setText(_translate("MainMenu", "CANCEL"))
        self.label.setText(_translate("MainMenu", "Line"))
    
    @QtCore.pyqtSlot()
    def onClickCmd(self, cmd):
        global usr_cmd, usr_line
        usr_cmd = cmd
    
    @QtCore.pyqtSlot()
    def onClickWrite(self):
        global usr_line

        usr_doc = self.docText.document().toPlainText()
        usr_value = self.valueText.document().toPlainText()
        usr_line = self.lineSpinBox.value()

        writeUsrIn(usr_doc, usr_value, usr_line)

        self.lineSpinBox.setValue(usr_line)
        self.docText.document().setPlainText("")
        self.valueText.document().setPlainText("")


class RecordApp(QtWidgets.QMainWindow, Ui_RecordWindow):
    def __init__(self, parent=None):
        super(RecordApp, self).__init__(parent)
        self.setupUi(self)

def load_ui():
    app = QtWidgets.QApplication(sys.argv)
    form = RecordApp()
    form.show()
    app.exec_()

# ----------------------------------------------------------------

if __name__ == "__main__":
    checkDataFileExist()

    option = input("record or run? ")

    if option == "record":
        load_ui()
        #writeUsrIn()
    else:
        runData()