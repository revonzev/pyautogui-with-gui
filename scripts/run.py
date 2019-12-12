import pyautogui
import storagedata
import os.path
from os import makedirs
from time import sleep
from pathlib import Path

# File Locations
doc_file = r"..\data\doc.txt"
value_file = r"..\data\value.txt"
cmd_file = r"..\data\cmd.txt"

pyautogui.PAUSE = 1

def writeUsrIn():
    current_line = getCurrentLine()

    while True:
        usr_in = pyautogui.prompt("Options: click, moveto, type, scroll, sleep, manual\ncopy, paste, stop")
        
        if usr_in == "click":
            x, y = pyautogui.position()
            value = str(x) +" " + str(y)
        elif usr_in == "moveto":
            x, y = pyautogui.position()
            value = str(x) +" " + str(y)
        elif usr_in == "type":
            value = pyautogui.prompt("The sentance: ")
        elif usr_in == "scroll":
            value = pyautogui.prompt("How many scroll?")
        elif usr_in == "sleep":
            value = pyautogui.prompt("How long?")
        elif usr_in == "manual":
            value = "manual"
        elif usr_in == "copy":
            value = "copy"
        elif usr_in == "paste":
            value = "paste"
        elif usr_in == "stop":
            exit()
        else:
            continue
        
        doc = pyautogui.prompt("Line {} Doc: ".format(current_line))
        writesDatas(current_line, value, doc, usr_in)
        current_line += 1

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

# ----------------------------------------------------------------

if __name__ == "__main__":
    checkDataFileExist()

    option = input("record or run? ")

    if option == "record":
        writeUsrIn()
    else:
        runData()