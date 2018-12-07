

# Creates, colors, and returns array
def colorArray():
    list = []
    for row in range(0, height):
        list.append([])
        for col in range(0, width):
            list[row].append((0,0,0))
    randColors = pickColors()
    for row in range(0, height):
        # index 0 and 6
        zeroSix = random.choice(randColors)
        # index 1 and 5
        oneFive = random.choice(randColors)
        # index 2 and 4
        twoFour = random.choice(randColors)
        # index 3
        three = random.choice(randColors)
        # Add the colors to the array
        list[row][0] = zeroSix
        list[row][1] = oneFive
        list[row][2] = twoFour
        list[row][3] = three
        list[row][4] = twoFour
        list[row][5] = oneFive
        list[row][6] = zeroSix
    return list

def colorArray():
    list = []
    colorList = []
    for row in range(0, height):
        list.append([])
        for col in range(0, width):
            list[row].append((0,0,0))
    randColors = pickColors()
    print(randColors)
    for row in range(0, height):
        symmetryTracker = 0
        symmetryIterator = 1
        for col in range(0, width):
            currentColor = random.choice(randColors)
            if (symmetryTracker < width/2):
                colorList.append(currentColor)
            elif (symmetryTracker == width/2 or symmetryTracker == 0):
                symmetryIterator *= -1
            else:
                currentColor = colorList.pop()
            
            list[row][col] = currentColor
            print(list[row][col])
            symmetryTracker += symmetryIterator
    return list

