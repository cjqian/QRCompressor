from PIL import Image
import sys

def makeDecimal(image):
	bStr = ""
	size = image.size[0]
	for i in range(0, size):
		for j in range(0, size):
			#if the pixel is black
			if image.getpixel((i, j)) == (0, 0, 0):
				bStr += "1"
			else:
				bStr += "0"
	decimal = int(bStr, 2)

	with open("output.txt", "w") as text_file:
		text_file.write(str(decimal))
image = Image.open(sys.argv[1])
makeDecimal(image)
