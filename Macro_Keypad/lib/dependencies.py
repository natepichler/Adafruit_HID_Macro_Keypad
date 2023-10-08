import time
import usb_hid
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keyboard_layout_base import KeyboardLayoutBase
import sys
import storage
import neopixel
import board
from digitalio import DigitalInOut, Direction, Pull
#from datetime import date
pixel = neopixel.NeoPixel(board.D10, 2, auto_write=True, bpp = 3, pixel_order=neopixel.GRB)
i=0
kbd = Keyboard(usb_hid.devices)
keyboard = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(kbd)
layer = 1
##########################################
#    SET PINS
##########################################
btn1_pin = board.D5
btn2_pin = board.D2
btn3_pin = board.D9
btn4_pin = board.D6
btn5_pin = board.D3
btn6_pin = board.D8
btn7_pin = board.D4
btn8_pin = board.D1
btn9_pin = board.D7
btn0_pin = board.D0
btn1 = DigitalInOut(btn1_pin)
btn1.direction = Direction.INPUT
btn1.pull = Pull.UP
btn2 = DigitalInOut(btn2_pin)
btn2.direction = Direction.INPUT
btn2.pull = Pull.UP
btn3 = DigitalInOut(btn3_pin)
btn3.direction = Direction.INPUT
btn3.pull = Pull.UP
btn4 = DigitalInOut(btn4_pin)
btn4.direction = Direction.INPUT
btn4.pull = Pull.UP
btn5 = DigitalInOut(btn5_pin)
btn5.direction = Direction.INPUT
btn5.pull = Pull.UP
btn6 = DigitalInOut(btn6_pin)
btn6.direction = Direction.INPUT
btn6.pull = Pull.UP
btn7 = DigitalInOut(btn7_pin)
btn7.direction = Direction.INPUT
btn7.pull = Pull.UP
btn8 = DigitalInOut(btn8_pin)
btn8.direction = Direction.INPUT
btn8.pull = Pull.UP
btn9 = DigitalInOut(btn9_pin)
btn9.direction = Direction.INPUT
btn9.pull = Pull.UP
btn0 = DigitalInOut(btn0_pin)
btn0.direction = Direction.INPUT
btn0.pull = Pull.UP
