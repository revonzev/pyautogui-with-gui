import pyautogui
import storagedata
import os.path
from os import makedirs
from time import sleep
from pathlib import Path

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
            pos = str(x) +" " + str(y)

            writesDatas(current_line, pos, "click")
            current_line += 1
        elif usr_in == "moveto":
            x, y = pyautogui.position()
            pos = str(x) +" " + str(y)

            writesDatas(current_line, pos, "moveto")
            current_line += 1
        elif usr_in == "type":
            sentance = pyautogui.prompt("The sentance: ")

            writesDatas(current_line, sentance, "type")
            current_line += 1
        elif usr_in == "scroll":
            times = pyautogui.prompt("How many scroll?")

            writesDatas(current_line, times, "scroll")
            current_line += 1
        elif usr_in == "sleep":
            time = pyautogui.prompt("How long?")
            
            writesDatas(current_line, time, "sleep")
            current_line += 1
        elif usr_in == "manual":
            writesDatas(current_line, time, "manual")
            current_line += 1
        elif usr_in == "copy":
            writesDatas(current_line, "copy", "copy")
            current_line += 1
        elif usr_in == "paste":
            writesDatas(current_line, "paste", "paste")
            current_line += 1
        elif usr_in == "stop":
            exit()

def runData():
    file_length = int(storagedata.readData(cmd_file, option="len"))
    current_line = getCurrentLine()

    while current_line < file_length+1:
        cmd = storagedata.readData(cmd_file, current_line)
        value = storagedata.readData(value_file, current_line)
        doc = storagedata.readData(doc_file, current_line)

        if cmd == "click":
            x, y = value.split(" ")
            x = int(x)
            y = int(y)
            pyautogui.click(x, y)
            print(current_line, doc)
        elif cmd == "moveto":
            x, y = value.split(" ")
            x = int(x)
            y = int(y)
            pyautogui.moveTo(x, y)
            print(current_line, doc)
        elif cmd == "type":
            sleep(1)
            pyautogui.typewrite(value)
            print(current_line, doc)
            sleep(5)
        elif cmd == "scroll":
            pyautogui.PAUSE = .5
            for i in range(0, int(value)):
                pyautogui.scroll(-500)
            print(current_line, doc)
            sleep(3)
            pyautogui.PAUSE = 1
        elif cmd == "sleep":
            sleep(int(value))
            print(current_line, doc)
        elif cmd == "manual":
            pyautogui.confirm("Input manualy. {}".format(value))
            print(current_line, doc)
        elif cmd == "copy":
            pyautogui.hotkey("ctrl", "c")
            print(current_line, doc)
        elif cmd == "paste":
            pyautogui.hotkey("ctrl", "v")
            print(current_line, doc)
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

def writesDatas(current_line, value, cmd):
    doc = pyautogui.prompt("Line {} Doc: ".format(current_line))

    storagedata.overwriteData(value_file, current_line, value)
    storagedata.overwriteData(doc_file, current_line, doc)
    storagedata.overwriteData(cmd_file, current_line, cmd)

# ----------------------------------------------------------------

def checkDataExist():
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
    checkDataExist()
    option = input("record or run? ")
    if option == "record":
        writeUsrIn()
    else:
        runData()