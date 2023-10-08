##########################################
#    COLORS
##########################################

cyan = (0, 150, 150)
blue = (0, 0, 255)
red = (255, 0, 0)
orange = (255, 126, 0)
white = (100, 100, 100)
green = (0, 100, 0)
violet = (100, 0, 50)
pink = (255, 80, 255)
off = (0,0,0)

##########################################
#    LAYER COLORS
##########################################

layer_1_color = green
layer_2_color = cyan
layer_3_color = violet
#layer_4_color = blue
#layer_5_color = red
#layer_6_color = pink
running_color = orange
startup_color = white

##########################################
#    IMPORT LAYER FILES
##########################################

from layer_1 import *
from layer_2 import *
from layer_3 import *
#from layer_4 import *
#from layer_5 import *
#from layer_6 import *

##########################################
#    FLASH COLORS ON STARTUP
##########################################
while i < 2:
    pixel[0] = startup_color
    pixel[1] = off
    time.sleep(0.1)
    pixel[0] = off
    pixel[1] = startup_color
    time.sleep(0.1)
    i = i + 1

##########################################
#    MAIN CODE
##########################################

while True:
    try:
        while layer == 1:
            pixel[0] = layer_1_color
            pixel[1] = layer_1_color

            if not btn1.value:
                pixel[0] = running_color
                layer1button1()
                time.sleep(0.1)
                pixel[0] = layer_1_color
                time.sleep(0.1)
            if not btn2.value:
                pixel[0] = running_color
                layer1button2()
                time.sleep(0.1)
                pixel[0] = layer_1_color
                time.sleep(0.1)
            if not btn3.value:
                pixel[0] = running_color
                layer1button3()
                time.sleep(0.1)
                pixel[0] = layer_1_color
                time.sleep(0.1)
            if not btn4.value:
                pixel[0] = running_color
                layer1button4()
                time.sleep(0.1)
                pixel[0] = layer_1_color
                time.sleep(0.1)
            if not btn5.value:
                pixel[0] = running_color
                layer1button5()
                time.sleep(0.1)
                pixel[0] = layer_1_color
                time.sleep(0.1)
            if not btn6.value:
                pixel[0] = running_color
                layer1button6()                
                time.sleep(0.1)
                pixel[0] = layer_1_color
                time.sleep(0.1)
            if not btn7.value:
                pixel[0] = running_color
                layer1button7()
                time.sleep(0.1)
                pixel[0] = layer_1_color
                time.sleep(0.1)
            if not btn8.value:
                pixel[0] = running_color
                layer1button8()
                time.sleep(0.1)
                pixel[0] = layer_1_color
                time.sleep(0.1)
            if not btn9.value:
                pixel[0] = running_color
                layer1button9()
                time.sleep(0.1)
                pixel[0] = layer_1_color
                time.sleep(0.1)
    #-----------------------------------------            
            if not btn0.value:
                layer = 2
                time.sleep(0.15)
    #-----------------------------------------            
        time.sleep(0.1)

        while layer == 2:
            pixel[0] = layer_2_color
            pixel[1] = layer_2_color
            if not btn1.value:
                pixel[0] = running_color
                layer2button1()
                time.sleep(0.1)
                pixel[0] = layer_2_color
                time.sleep(0.1)
            if not btn2.value:
                pixel[0] = running_color
                layer2button2()
                time.sleep(0.1)
                pixel[0] = layer_2_color
                time.sleep(0.1)
            if not btn3.value:
                pixel[0] = running_color
                layer2button3()
                time.sleep(0.1)
                pixel[0] = layer_2_color
                time.sleep(0.1)
            if not btn4.value:
                pixel[0] = running_color
                layer2button4()
                time.sleep(0.1)
                pixel[0] = layer_2_color
                time.sleep(0.1)
            if not btn5.value:
                pixel[0] = running_color
                layer2button5()
                time.sleep(0.1)
                pixel[0] = layer_2_color
                time.sleep(0.1)
            if not btn6.value:
                pixel[0] = running_color
                layer2button6()
                time.sleep(0.1)
                pixel[0] = layer_2_color
                time.sleep(0.1)
            if not btn7.value:
                pixel[0] = running_color
                layer2button7()
                time.sleep(0.1)
                pixel[0] = layer_2_color
                time.sleep(0.1)
            if not btn8.value:
                pixel[0] = running_color
                layer2button8()
                time.sleep(0.1)
                pixel[0] = layer_2_color
                time.sleep(0.1)
            if not btn9.value:
                pixel[0] = running_color
                layer2button9()
                time.sleep(0.1)
                pixel[0] = layer_2_color
                time.sleep(0.1)
    #-----------------------------------------            
            if not btn0.value:
                layer = 3
                time.sleep(0.15)
    #-----------------------------------------
        time.sleep(0.1)

        while layer == 3:
            pixel[0] = layer_3_color
            pixel[1] = layer_3_color
            if not btn1.value:
                pixel[0] = running_color
                layer3button1()
                time.sleep(0.1)
                pixel[0] = layer_3_color
                time.sleep(0.1)
            if not btn2.value:
                pixel[0] = running_color
                layer3button2()
                time.sleep(0.1)
                pixel[0] = layer_3_color
                time.sleep(0.1)
            if not btn3.value:
                pixel[0] = running_color
                layer3button3()
                time.sleep(0.1)
                pixel[0] = layer_3_color
                time.sleep(0.1)
            if not btn4.value:
                pixel[0] = running_color
                layer3button4()
                time.sleep(0.1)
                pixel[0] = layer_3_color
                time.sleep(0.1)
            if not btn5.value:
                pixel[0] = running_color
                layer3button5()
                time.sleep(0.1)
                pixel[0] = layer_3_color
                time.sleep(0.1)
            if not btn6.value:
                pixel[0] = running_color
                layer3button6()
                time.sleep(0.1)
                pixel[0] = layer_3_color
                time.sleep(0.1)
            if not btn7.value:
                pixel[0] = running_color
                layer3button7()
                time.sleep(0.1)
                pixel[0] = layer_3_color
                time.sleep(0.1)
            if not btn8.value:
                pixel[0] = running_color
                layer3button8()
                time.sleep(0.1)
                pixel[0] = layer_3_color
                time.sleep(0.1)
            if not btn9.value:
                pixel[0] = running_color
                layer3button9()
                time.sleep(0.1)
                pixel[0] = layer_3_color
                time.sleep(0.1)
    #-----------------------------------------            
            if not btn0.value:
                layer = 1
                time.sleep(0.15)
    #-----------------------------------------
        time.sleep(0.1)
    except Exception:
        pixel[0] = red
        exit()

time.sleep(0.1)

