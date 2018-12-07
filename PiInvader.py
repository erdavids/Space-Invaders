import random
import time
import board
import neopixel
# Lambdas for picking random RGBs
r = lambda: random.randint(0,255)
rc = lambda: (r(), r(), r())
rcr = lambda: (0, r(), r())
rcg = lambda: (r(), 0, r())
rcb = lambda: (r(), r(), 0)
# List of colors for random choice
randColors = [rcr(), rcg(), rcb(), (0,0,0), (0,0,0), (0,0,0)]
# Dimensions of the 7x7 array
width = 7
height = 7
# Initialize the 2D Lists
array = []
arrayNext = []
# Single list
finalList = []

for x in range(0, width*height):
    finalList.append((0,0,0))

normalize

# neopixels
pixels = neopixel.NeoPixel(board.D4, 49, brightness=.2)
pixels.fill((0,0,0))
pixels.show()
for y in range(0, height):
    array.append([])
    for x in range(0, width):
        array[y].append((0,0,0))
for y in range(0, height):
    arrayNext.append([])
    for x in range(0, height):
        array[y].append((0,0,0))
def pickColors():
    return (rc(), rc(), rc())

def colorArray():
    list = []
    for y in range(0, height):
        list.append([])
    for x in range(0, width):
        list[y].append((0,0,0))
    randColors = pickColors()
    for y in range(0, height):
        # index 0 and 6
        zeroSix = random.choice(randColors)
        # index 1 and 5
        oneFive = random.choice(randColors)
        # index 2 and 4
        twoFour = random.choice(randColors)
        # index 3
        three = random.choice(randColors)
        # Add the colors to the array
        list[y][0] = zeroSix
        list[y][1] = oneFive
        list[y][2] = twoFour
        list[y][3] = three
        list[y][4] = twoFour
        list[y][5] = oneFive
        list[y][6] = zeroSix
    return list
def convertToSingleList(list):
    counter = 0
    for x in range(0, width):
        for y in range(0, height):
            finalList[counter] = list[x][y]
            counter += 1
def replaceFromBottom(oldList, newList):
    for i in range(0, height):
        for x in range(0, height - 1):
            oldList[x] = oldList[x + 1]
        oldList[height-1] = newList[i]
#        outputToDisplay(oldList)
#        time.sleep(.05)
def replaceFromTop(oldList, newList):
    for i in range(0, height):
        for x in range(0, height - 1):
            oldList[height - 1 - x] = oldList[height - 2 - x]
        #print x
        oldList[0] = newList[height - 1 - i]
#        outputToDisplay(oldList)
#        time.sleep(.05)
def replaceFromRight(oldList, newList):
    for x in range(0, width):
        for y in range(0, height):
            for j in xrange(width-1):
                oldList[y][j] = oldList[y][j+1]
            oldList[y][width - 1] = newList[y][0+x]
#        outputToDisplay(oldList)
#        time.sleep(.05)
def replaceFromLeft(oldList, newList):
    for x in range(0, width):
        for y in range(0, height):
            for j in range(0, width-1):
                oldList[y][width - 1 - j] = oldList[y][width - 2 - j]
            oldList[y][0] = newList[y][width - 1 - x]
        outputToDisplay(oldList)
        time.sleep(.05)
def outputToDisplay(list):
    convertToSingleList(list)
    for x in range(0, len(finalList)):
        pixels[x] = finalList[x]
    pixels.show()
# def main():
while True:
    pickColors()
    colorArray(array)
    outputToDisplay(array)
    time.sleep(1)
    pickColors()
    colorArray(arrayNext)
    replaceFromLeft(array, arrayNext)
    time.sleep(1)
#pixels[5] = (255,255,255)
#pixels.show()
# if __name__ == "__main__":
#     main()
