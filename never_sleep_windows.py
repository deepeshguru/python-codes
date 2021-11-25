# This script is useful to prevent your system from sleep mode. This script automatically press f15 in every minute.
# Requiredment: pip install pynput

from pynput.keyboard import Key, Controller
from time import sleep

keyboard = Controller()

while(1):
  keyboard.press(Key.f15)
  keyboard.release(Key.f15)
  sleep(60)
