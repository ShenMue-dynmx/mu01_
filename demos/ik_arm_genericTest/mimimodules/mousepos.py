import pyautogui

def screenSpec():
    print("screen spec:"+str(pyautogui.size()))
    return pyautogui.size()
def getMouse():
    return pyautogui.position()