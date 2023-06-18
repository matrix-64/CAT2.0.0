import pyautogui as pg

class keyboardModeCAT:
    Keys = {
    
    def __init__(self,i_shape):
        self.typing = False

    def action(self,sh):
        inp = sh[0]*32 + sh[1]
        
