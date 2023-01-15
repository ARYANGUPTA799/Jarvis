import os
import subprocess as sp
import os

import pyautogui
# from dotenv import load_dotenv

# load_dotenv()

PATH_SCREENSHOT = os.getenv("PATH_SCREENSHOT")
screenshots = 1


def takeScreenShot():
    try:
        global screenshots
        myScreenshot = pyautogui.screenshot()
        myScreenshot.save(str(PATH_SCREENSHOT)+f"{screenshots}.jpg")
        screenshots += 1
    except Exception as e:
        print(e)
        return False

    return True



paths = {
    'notepad': "C:\\Program Files\\Notepad++\\notepad++.exe",
    'calculator': "C:\\Windows\\System32\\calc.exe"
}


def open_camera():
    """ Open Camera using subprocess module to run the command """
    sp.run('start microsoft.windows.camera:', shell=True)


def open_path(app):
    """
    If the application name is present in paths list then it will open it
    Returns:
        bool: application opened or not
    """
    if app in paths.keys():
        try:
            os.startfile(paths[app])
        except Exception as e:
            print(e)
            return False
        return True

    return False


def open_cmd():
    os.system('start cmd')