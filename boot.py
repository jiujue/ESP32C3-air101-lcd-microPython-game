from machine import Pin
import time
import random
from machine import Pin, SoftSPI,SPI
from ST7735 import TFT
import time
# 由于ftf屏的颜色有问题，因此需要重写一个函数修复一下
def TFTColor(r,g,b) :
  return ((b & 0xF8) << 8) | ((g & 0xFC) << 3) | (r >> 3)
#使用SoftSPI，SPI不行
spi = SoftSPI(baudrate=2400000, polarity=1, phase=0, sck=Pin(2), mosi=Pin(3), miso=Pin(10))
tft=TFT(spi,6,10,7) #DC, Reset, CS
tft.initr()
tft.rgb(True)
# tft.rotation(1) #方向调整

# 绘制背景色
tft.fill(TFTColor(0,0,0))


right_key = Pin(8, Pin.OUT,Pin.PULL_UP)
down_key = Pin(9, Pin.OUT,Pin.PULL_UP)
center_key = Pin(4, Pin.OUT,Pin.PULL_UP)#上拉io4，中心按钮按下是低电平，不按的时候电平悬浮
up_key = Pin(5, Pin.OUT,Pin.PULL_UP)
left_key = Pin(18, Pin.OUT,Pin.PULL_UP)

left_key.on()
up_key.on()
right_key.on()
down_key.on()
center_key.on()

x=20
y=20
w=5
h=7
step=1
goal = (60, 100)
timer = 0
while True:
#     tft.fill(TFTColor(0,0,0))
    tft.fillcircle(goal, 2, TFTColor(255,205,110))
    tft.fillrect((x,y),(w+10,h+5),TFTColor(0,0,255))
    tft.fillrect((x,y),(w+10,h+5),TFTColor(0,0,0))
    if right_key.value() == 0:
        x = x + step
        print('right_key')
    if up_key.value() == 0:
        y = y - step
        print('up_key')
    if down_key.value() == 0:
        y = y + step
        print('down_key')
    if left_key.value() == 0:
        x = x - step
        print('left_key')
    if center_key.value() == 0:
        tft.fill(TFTColor(0,0,0))
        tft.fillcircle(goal, 2, TFTColor(255,205,110))
        print('center_key')
    if x  > 100 :
        x = 0
    if x  < 0 :
        x = 100
    if y  > 180 or y < 0:
        y = 0
    if x ==goal[0] :
        if y == goal[1] :
#             w = w + 1
            tft.fillcircle(goal, 2, TFTColor(0,0,0))
    timer = timer + 1
    if timer > 100:
        timer = 0
        goal = (random.randint(10,100), random.randint(10,270))
    if x > 100:
        x = 0
    time.sleep_ms(5)  
         # sleep for 1 second


