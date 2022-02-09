from lcd import LcdI2C
import sys
from datetime import datetime
from time import sleep

cur_t = ''
if __name__ == '__main__':
    while True:
        lcd2004 = LcdI2C(0x27, 1)
        time = datetime.now().strftime("%h, %m  %H:%M")
        if time != cur_t:
            cur_t = time
            lcd2004.display_string(time, 1)
            print(f"\n\tSet: {time}")
        print(".", end='')
        sleep(1)
