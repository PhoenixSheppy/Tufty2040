from picographics import PicoGraphics, DISPLAY_TUFTY_2040
from pimoroni import Button
import time
import jpegdec

display = PicoGraphics(display=DISPLAY_TUFTY_2040)
button_c = Button(9, invert=False)

WIDTH, HEIGHT = display.get_bounds()

IMAGE_NAME1 = "GFM23Attending.jpg"
IMAGE_NAME2 = "GFM23Staff.jpg"

def show_attending():
    j = jpegdec.JPEG(display)

    # Open the JPEG file
    j.open_file(IMAGE_NAME1)

    # Decode the JPEG
    j.decode()

def show_staff():
    j = jpegdec.JPEG(display)

    # Open the JPEG file
    j.open_file(IMAGE_NAME2)

    # Decode the JPEG
    j.decode()
    
badge_mode = "attending"
show_attending()
display.update()

while True:
    if button_c.is_pressed:
        if badge_mode == "attending":
            badge_mode = "staff"
            show_staff()
            display.update()
        else:
            badge_mode = "attending"
            show_attending()
            display.update()
        time.sleep(1)