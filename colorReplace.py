from PIL import Image
import sys

### Get Input Image ###
image_PATH = None
for item in sys.argv:
	if item.endswith(".png") or item.endswith(".jpg"):
		image_PATH = item

if image_PATH == None:
	image_PATH = input("Drag image here: ").strip()


