from PIL import Image
import sys
import math

def makePng(decimal):
	binary = bin(decimal)[2:]
	size = int(math.sqrt(len(binary)))
	#new white image
	image = Image.new("RGB", (size, size), "white")
	
	for i in range(0, size):
		for j in range(0, size):
				if binary[i*size+j] == '1':
						#if binary has value 1 at that point in the 2D array, 
						#mset pixel to black
						image.putpixel((i, j), (0, 0, 0))
	image.save("output.png")

makePng(int(sys.argv[1]))
