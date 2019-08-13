from PIL import Image
import sys
from tqdm import tqdm
import os
from ast import literal_eval

currentPath = os.popen("pwd").read()[:-1]
print(currentPath)


def listCounts(inputList):
	outputDict = {}

	for point in inputList:
		if point not in outputDict:
			outputDict[point] = 1
		elif point in outputDict:
			outputDict[point] += 1

	return outputDict


def findLargestVals(inputDict):
	allVals = []
	for point in inputDict:
		allVals.append(inputDict[point])

	bigs = []
	while len(bigs) < 5:
		for i, val in enumerate(allVals):
			if val == max(allVals) and len(bigs) < 5:
				allVals.pop(i)
				bigs.append(val)

	points = {}
	for point in inputDict:
		if inputDict[point] in bigs:
			points[point] = inputDict[point]

	return points


#  START  #

# Get Input Image #
image_PATH = None
for item in sys.argv:
	if item.endswith(".png") or item.endswith(".jpg"):
		image_PATH = item

if image_PATH is None:
	image_PATH = input("Drag image here: ").strip()

# Get raw data from image #
im = Image.open(image_PATH)
raw_data = list(im.getdata())

# Count all Colors in image #
counts = listCounts(raw_data)
mostCommon = findLargestVals(counts)

# Get user Color Selection #
print("\nMost common colors are:")
for i, color in enumerate(mostCommon.keys()):
	print("  " + str(i) + " - " + str(color[:3]) + " " * (15 - len(str(color[:3]))) + "   | " + str(mostCommon[color]))

colorSelectPhrase = "\nWhich color would you like to pick to replace? (0-4): "
userSelection = int(input(colorSelectPhrase))
userColor = list(mostCommon.keys())[userSelection]
print(f"You picked: {userColor[:3]}")

# Get replace Color #
colorInPhrase = "Type the color that you want to replace with as (R, G, B): "
userNewColor_string = input(colorInPhrase).strip()
userNewColor_tuple = literal_eval(userNewColor_string)

# MAKE NEW COLOR DATA #
newData = []
print("Making new Data")
for pixel in tqdm(raw_data):
	if pixel == userColor:
		newData.append(userNewColor_tuple)
	else:
		newData.append(pixel)
# print(newData)
# quit()

# Send new color data to new image file #
newIm = Image.new("RGB", (im.size[0], im.size[1]))
print(len(newData), type(newData), type(newData[0]))
newIm.putdata(newData)
newIm.save(currentPath + "/output.png")
