from dependencies import *
from layer_1 import *
from layer_3 import *
#from layer_4 import *
#from layer_5 import *
#from layer_6 import *

####################################################
# *TYPE A STRING* #
# layout.write('')

# *USE KEYCODES (SINGLE OR MULTIPLE)* #
# keyboard.send(Keycode.EIGHT)
# keyboard.send(Keycode.SHIFT,Keycode.B)

# see ./lib/adafruit_hid/keycode.py for a list 


# *DELAY* #
# time.sleep(0.1)
####################################################

def layer2button1():

            layout.write('')

def layer2button2():

            layout.write('')

def layer2button3():

            layout.write('')

def layer2button4():

            layout.write('')

def layer2button5():

            keyboard.send(Keycode.WINDOWS)
            time.sleep(0.6)
            layout.write('notepad')
            time.sleep(0.7)
            keyboard.send(Keycode.RETURN)
            time.sleep(0.6)
            layout.write('Did you ever hear the tragedy of Darth Plagueis The Wise? I thought not. It\'s not a story the Jedi would tell you.')
            keyboard.send(Keycode.RETURN)
            layout.write('It\'s a Sith legend. Darth Plagueis was a Dark Lord of the Sith, so powerful and so wise he could use the Force to influence the midichlorians to create life.')
            keyboard.send(Keycode.RETURN)
            layout.write('He had such a knowledge of the dark side that he could even keep the ones he cared about from dying. The dark side of the Force is a pathway to many abilities some consider to be unnatural.')
            keyboard.send(Keycode.RETURN)
            layout.write('He became so powerful, the only thing he was afraid of was losing his power, which eventually, of course, he did.')
            keyboard.send(Keycode.RETURN)
            layout.write('Unfortunately, he taught his apprentice everything he knew, then his apprentice killed him in his sleep. Ironic.')
            keyboard.send(Keycode.RETURN)
            layout.write('He could save others from death, but not himself.')
            keyboard.send(Keycode.CONTROL, Keycode.S)
            time.sleep(0.7)
            layout.write('The Tragedy of Darth Plagueis The Wise.txt')
            time.sleep(0.7)
            keyboard.send(Keycode.RETURN)
            time.sleep(0.7)
            keyboard.send(Keycode.ALT, Keycode.F4)

def layer2button6():

            layout.write('')
            
def layer2button7():

            layout.write('')

def layer2button8():

            layout.write('')

def layer2button9():

            layout.write('')
            

