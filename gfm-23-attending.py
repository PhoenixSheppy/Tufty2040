from picographics import PicoGraphics, DISPLAY_TUFTY_2040
import time
import jpegdec

display = PicoGraphics(display=DISPLAY_TUFTY_2040)

WIDTH, HEIGHT = display.get_bounds()

IMAGE_NAME = "GFM23Attending.jpg"

def show_photo():
    j = jpegdec.JPEG(display)

    # Open the JPEG file
    j.open_file(IMAGE_NAME)

    # Decode the JPEG
    j.decode()

while True:
    show_photo()
    display.update()
    time.sleep(1)

