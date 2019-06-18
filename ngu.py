import pyautogui
import time
import sys
from screens import Screens

from game_mode.fast15 import Fast15

time.sleep(5)
position = pyautogui.position()

mode = sys.argv[1]
print(position)
if not mode:
    print("Mode is mandatory")
    sys.exit(1)

if mode == 'fast15':
    Fast15(Screens(position.x, position.y))
