from lcd import LcdI2C

if __name__ == '__main__':
    import sys
    lcd2004 = LcdI2C(0x27, 1)

    if len(sys.argv) > 1:
        lcd2004.display_string(sys.argv[1], 1)
    else:
        lcd2004.display_string("Wait string...", 1)
