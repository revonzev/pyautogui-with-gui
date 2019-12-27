# pyautogui with gui

Python pyautogui for automation without all of the clutter of manualy programming in the codes.

![](https://www.python.org/static/community_logos/python-powered-w-200x80.png)

When you run the scripts/run.py a console will pop-up, It will ask you "record or run? "
- Run

  This will run the program from the recorded data in "/data/". if the program or more likely the user want to exit the program while it is being automated or runned, move the crusor to the top right of the screen
  - cmd.txt Commands
    
    This is the command or action data
  - doc.txt
    
    This is the documentation data of the command or action to let users know when an action happend
  - value.txt
    
    This is the value for the action. for example action "type" the value is "hello world"
- Record

  GUI Example:

  ![](img/record-gui.jpg)

  This gui have 8 action

  This will let you record one of eight actions
  - Click

    Crusor click to a position
    
    Click the "Click" button on the GUI and move your crusor to the desired location to click the crusor when this automation run is run then press enter
  - Move to

    Crusor move to a position

    Click the "Move to" button on the GUI and move your crusor to the desired loaction to move the crusor when this automation run then press enter
  - Type

    Type the value it has been given in data

    Click the "Type" button and enter in the text to type in when the automation is run in the value textbox.
  - Scroll

    Scroll for the amount it has been given in data

    Click the "Scroll" button and enter in the amount of scrolls in the value. Note: the user need to run this first before continuing. DO NOT actualy scroll. user and automated scroll is different.
  - Wait
 
    The automation will wait for the amount of second it has been given in the data

    Click the "Wait" button and enter in the value of the automation to wait for (in seconds). this is good for when a page is loading.
  - Manual

    The automation will pop-up a confirmation button to check if the user has done the required task manualy

    Click the manual button. The documentation text box will be the information that shows up in the confirmation pop-up
  - Copy and Paste
    
    The automation will copy the selected item and keep it untill it copies again. Paste, pastes the copied item.
  - End
    
    Exit... that's it...

  There are three text box in this GUI
  - Line text box
    
    This is where the program will write or overwrite the data of the displayed number
  - Documentation text box

    This is where the program will print out in the console.
  - Value text box
    
    The value required for "Type", "Scroll", and "Wait" button. if the user did not write the required value there will be a pop-up reminding them.
  
  "OK" button saves the data the user has inputed for when the automation is runned in the "/data/" as said earlier. The shortcut for this button is enter
  
  "CANCLE" button does absolutely nothing

  When finished with the record program either click END then OK or.. the simpler and faster way.. click the big red X button in the top left window

Made by Revon Zev