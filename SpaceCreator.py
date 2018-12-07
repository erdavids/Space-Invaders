import PIL, random, sys
from PIL import Image, ImageDraw

origDimension = 1500

r = lambda: rng.randint(50,215)
rc = lambda: (r(), r(), r())

gifMaking = 100001

listSym = []

seed = random.randrange(sys.maxsize)
rng = random.Random(seed)
print("Seed was:", seed)

APP_KEY = '44l77lU3T7nF9143VzV7AmLYR'
APP_SECRET = 'Czh8cNWxD7QNgbUGWALZI50LTvTSHI147SpBDA0DjNvaifoZEM'
ACCESS_TOKEN = '1067969736905015296-IEMh64UYEahOgxewnhb4VVkVy0JMZP'
ACCESS_SECRET = 'AfLAHDJeAvUqtg1tSZLRUQz5hDAd8neQFCGWJpl1wGGAY'

def create_square(border, draw, randColor, element, size, origImage):
    global gifMaking
    if (element == int(size/2)):
        draw.rectangle(border, randColor)
    elif (len(listSym) == element+1):
        draw.rectangle(border,listSym.pop())
    else:
        listSym.append(randColor)
        draw.rectangle(border, randColor)

#if (gifMaking%1 == 0):
        #origImage.save("Examples/Gif/" + str(gifMaking) + ".jpg")
#   gifMaking += 1

def create_invader(border, draw, size, origImage):
    x0, y0, x1, y1 = border
    squareSize = (x1-x0)/size
    randColors = [rc(), rc(), rc(), (0,0,0), (0,0,0), (0,0,0)]
    incrementer = 1
    element = 0

    for y in range(0, size):
        incrementer *= -1
        element = 0
        for x in range(0, size):
            topLeftX = x*squareSize + x0
            topLeftY = y*squareSize + y0
            botRightX = topLeftX + squareSize
            botRightY = topLeftY + squareSize


            create_square((topLeftX, topLeftY, botRightX, botRightY), draw, rng.choice(randColors), element, size, origImage)
            if (element == int(size/2) or element == 0):
                incrementer *= -1;
            element += incrementer


def main(imgSize):
    size = rng.randrange(3, 25+1, 2)
    invaders = rng.randint(6, 45)
    origDimension = imgSize
    origImage = Image.new('RGB', (origDimension, origDimension))
    draw = ImageDraw.Draw(origImage)

    invaderSize = origDimension/invaders
    padding = invaderSize/size
    # Will eventually create many
    for x in range(0, invaders):
        for y in range(0, invaders):
            topLeftX = x*invaderSize + padding/2
            topLeftY = y*invaderSize + padding/2
            botRightX = topLeftX + invaderSize - padding/2
            botRightY = topLeftY + invaderSize - padding/2

            create_invader((topLeftX, topLeftY, botRightX, botRightY), draw, size, origImage)
    print("Examples/Example-"+str(size)+"x"+str(size)+"-"+str(invaders)+"-"+str(imgSize)+".jpg")
    origImage.save("Examples/Example-"+str(size)+"x"+str(size)+"-"+str(invaders)+"-"+str(imgSize)+".jpg")

    twitter = Twython(APP_KEY, APP_SECRET, ACCESS_TOKEN, ACCESS_SECRET)
    photo = open('/home/pi/Generative/SolarSystemGenerator/Twitter/textured.png', 'rb')
    response = twitter.upload_media(media=photo)
    twitter.update_status(status='Randomly generated Solar System', media_ids=[response['media_id']])



if __name__ == "__main__":
    main(int(sys.argv[1]))
