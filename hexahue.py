#!/usr/bin/python3
from sys import argv
from PIL import Image

def usage():
	print(f"Usage: python3 {argv[0]} IMAGE [ PADDING (in pixels) ]")

# init colors, to init dictionary more easily
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green1 = (101, 255, 0)
green2 = (102, 255, 0)
blu = (0, 0, 255)
yellow = (255, 255, 0)
light_blue = (0, 255, 255)
magenta = (255, 0, 255)
gray = (128, 128, 128)

# init dict
# keys are tuples of tuples of the six colors, values are the decoded values
hexahue = {}
hexahue[(magenta, red, green1, yellow, blu, light_blue)] = 'a'
hexahue[(red, magenta, green1, yellow, blu, light_blue)] = 'b'
hexahue[(red, green1, magenta, yellow, blu, light_blue)] = 'c'
hexahue[(red, green1, yellow, magenta, blu, light_blue)] = 'd'
hexahue[(red, green1, yellow, blu, magenta, light_blue)] = 'e'
hexahue[(red, green1, yellow, blu, light_blue, magenta)] = 'f'
hexahue[(green1, red, yellow, blu, light_blue, magenta)] = 'g'
hexahue[(green1, yellow, red, blu, light_blue, magenta)] = 'h'
hexahue[(green1, yellow, blu, red, light_blue, magenta)] = 'i'
hexahue[(green1, yellow, blu, light_blue, red, magenta)] = 'j'
hexahue[(green1, yellow, blu, light_blue, magenta, red)] = 'k'
hexahue[(yellow, green1, blu, light_blue, magenta, red)] = 'l'
hexahue[(yellow, blu, green1, light_blue, magenta, red)] = 'm'
hexahue[(yellow, blu, light_blue, green1, magenta, red)] = 'n'
hexahue[(yellow, blu, light_blue, magenta, green1, red)] = 'o'
hexahue[(yellow, blu, light_blue, magenta, red, green1)] = 'p'
hexahue[(blu, yellow, light_blue, magenta, red, green1)] = 'q'
hexahue[(blu, light_blue, yellow, magenta, red, green1)] = 'r'
hexahue[(blu, light_blue, magenta, yellow, red, green1)] = 's'
hexahue[(blu, light_blue, magenta, red, yellow, green1)] = 't'
hexahue[(blu, light_blue, magenta, red, green1, yellow)] = 'u'
hexahue[(light_blue, blu, magenta, red, green1, yellow)] = 'v'
hexahue[(light_blue, magenta, blu, red, green1, yellow)] = 'w'
hexahue[(light_blue, magenta, red, blu, green1, yellow)] = 'x'
hexahue[(light_blue, magenta, red, green1, blu, yellow)] = 'y'
hexahue[(light_blue, magenta, red, green1, yellow, blu)] = 'z'

hexahue[(magenta, red, green2, yellow, blu, light_blue)] = 'a'
hexahue[(red, magenta, green2, yellow, blu, light_blue)] = 'b'
hexahue[(red, green2, magenta, yellow, blu, light_blue)] = 'c'
hexahue[(red, green2, yellow, magenta, blu, light_blue)] = 'd'
hexahue[(red, green2, yellow, blu, magenta, light_blue)] = 'e'
hexahue[(red, green2, yellow, blu, light_blue, magenta)] = 'f'
hexahue[(green2, red, yellow, blu, light_blue, magenta)] = 'g'
hexahue[(green2, yellow, red, blu, light_blue, magenta)] = 'h'
hexahue[(green2, yellow, blu, red, light_blue, magenta)] = 'i'
hexahue[(green2, yellow, blu, light_blue, red, magenta)] = 'j'
hexahue[(green2, yellow, blu, light_blue, magenta, red)] = 'k'
hexahue[(yellow, green2, blu, light_blue, magenta, red)] = 'l'
hexahue[(yellow, blu, green2, light_blue, magenta, red)] = 'm'
hexahue[(yellow, blu, light_blue, green2, magenta, red)] = 'n'
hexahue[(yellow, blu, light_blue, magenta, green2, red)] = 'o'
hexahue[(yellow, blu, light_blue, magenta, red, green2)] = 'p'
hexahue[(blu, yellow, light_blue, magenta, red, green2)] = 'q'
hexahue[(blu, light_blue, yellow, magenta, red, green2)] = 'r'
hexahue[(blu, light_blue, magenta, yellow, red, green2)] = 's'
hexahue[(blu, light_blue, magenta, red, yellow, green2)] = 't'
hexahue[(blu, light_blue, magenta, red, green2, yellow)] = 'u'
hexahue[(light_blue, blu, magenta, red, green2, yellow)] = 'v'
hexahue[(light_blue, magenta, blu, red, green2, yellow)] = 'w'
hexahue[(light_blue, magenta, red, blu, green2, yellow)] = 'x'
hexahue[(light_blue, magenta, red, green2, blu, yellow)] = 'y'
hexahue[(light_blue, magenta, red, green2, yellow, blu)] = 'z'

hexahue[(black, white, white, black, black, white)] = '.'
hexahue[(white, black, black, white, white, black)] = ','
hexahue[(white, white, white, white, white, white)] = ' '
hexahue[(black, black, black, black, black, black)] = ' '
hexahue[(black, gray, white, black, gray, white)] = '0'
hexahue[(gray, black, white, black, gray, white)] = '1'
hexahue[(gray, white, black, black, gray, white)] = '2'
hexahue[(gray, white, black, gray, black, white)] = '3'
hexahue[(gray, white, black, gray, white, black)] = '4'
hexahue[(white, gray, black, gray, white, black)] = '5'
hexahue[(white, black, gray, gray, white, black)] = '6'
hexahue[(white, black, gray, white, gray, black)] = '7'
hexahue[(white, black, gray, white, black, gray)] = '8'
hexahue[(black, white, gray, white, black, gray)] = '9'

if len(argv) < 2 or len(argv) > 3:
	usage()
	exit(1)

filename = argv[1]
padding = int(argv[2]) if len(argv) == 3 else 0

im = Image.open(filename)
im = im.convert("RGB")
width, height = im.size
x = padding
y = padding
plaintext = ""
while y < height-padding:
    current_letter = []
    for j in range(y, y+3):
        for i in range(x, x+2):
            current_letter.append(tuple(im.getpixel((i,j))))
    try:
        plaintext += hexahue[tuple(current_letter)]
    except KeyError:
        print(f"I broke trying to read {tuple(current_letter)}")
        print(f"Flag so far: {plaintext}")
        exit(0)
    x += 2
    # we reached the end of the row of boxes
    if x == width - padding:
        x = padding
        y += 3
    
print(plaintext)
