import pyautogui
from time import sleep


class Clickable:
    start_pos_x = 0
    start_pos_y = 0
    break_before = 0.2
    break_after = 0.1

    def __init__(self, start_pos_x, start_pos_y):
        self.start_pos_x = start_pos_x
        self.start_pos_y = start_pos_y

    def clickLeft(self, element_pos_x, element_pos_y):
        pyautogui.moveTo(x=self.start_pos_x + element_pos_x, y=self.start_pos_y + element_pos_y)
        sleep(self.break_before)
        pyautogui.click(button='left')
        sleep(self.break_after)

    def clickRight(self, element_pos_x, element_pos_y):
        pyautogui.moveTo(x=self.start_pos_x + element_pos_x, y=self.start_pos_y + element_pos_y)
        sleep(self.break_before)
        pyautogui.click(button='right')
        sleep(self.break_after)
