import pyautogui


class Clickable:
    start_pos_x = 0
    start_pos_y = 0

    def __init__(self, start_pos_x, start_pos_y):
        self.start_pos_x = start_pos_x
        self.start_pos_y = start_pos_y

    def click(self, element_pos_x, element_pos_y):
        pyautogui.click(x=self.start_pos_x + element_pos_x, y=self.start_pos_y + element_pos_y)
        return
