import PIL, random, sys
from PIL import Image, ImageDraw

origDimension = 1500


colorlist = [(0,0,0), (29,43,83), (126,37,83), (0,135,81), (171,82,54), (95,87,79), (194,195,199), (255,241,232), (255,0,77), (255,163,0), (255, 236, 39), (0,228,54), (41,173,255), (131,118,156), (255,119,168), (255,204,170)]

r = lambda: random.choice(colorlist)
rc = lambda: (r(),r(),r())

listSym = []

def create_square(border, draw, randColor):
    print(randColor)
    draw.rectangle(border, randColor)

def create_invader(border, draw, size):
    x0, y0, x1, y1 = border
    squareSize = (x1-x0)/size
    incrementer = 1
    element = 0
    randomColors=[r(),r(),r()]
    
    for y in range(0, size):
        for x in range(0, size):
            topLeftX = x*squareSize + x0
            topLeftY = y*squareSize + y0
            botRightX = topLeftX + squareSize
            botRightY = topLeftY + squareSize
            create_square((topLeftX, topLeftY, botRightX, botRightY), draw, random.choice(randomColors))

def main(size, invaders, imgSize):
    origDimension = imgSize
    origImage = Image.new('RGB', (origDimension, origDimension))
    draw = ImageDraw.Draw(origImage)
    
    invaderSize = origDimension/invaders
    padding = invaderSize/size
    # Will eventually create many
    for x in range(0, invaders):
        for y in range(0, invaders):
            topLeftX = x*invaderSize + padding
            topLeftY = y*invaderSize + padding
            botRightX = topLeftX + invaderSize - padding
            botRightY = topLeftY + invaderSize - padding
            
            create_invader((topLeftX, topLeftY, botRightX, botRightY), draw, size)

    origImage.save("Examples/Pico-"+str(size)+"x"+str(size)+"-"+str(invaders)+"-"+str(imgSize)+".jpg")

if __name__ == "__main__":
    main(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))

