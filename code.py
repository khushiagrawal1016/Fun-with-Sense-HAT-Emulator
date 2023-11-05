from sense_hat import SenseHat
import time

s = SenseHat()
s.low_light = True

blue = (0, 0, 255)
white = (255,255,255)
nothing = (0,0,0)

def Nike():
	B = blue
	W = white
	O = nothing
	logo = [
	O, O, O, O, O, O, O, O,
	O, O, O, O, O, O, O, B,
	O, O, O, O, O, B, B, O,
	O, B, O, O, B, B, O, O,
	B, B, O, B, B, O, O, O,
	B, B, B, B, O, O, O, O,
	O, B, B, O, O, O, O, O,
	O, O, O, O, O, O, O, O,
	]
	return logo  

images = [Nike]
count = 0

while True:
	s.set_pixels(images[count % len(images)]())
	time.sleep(.75)
	count += 1
