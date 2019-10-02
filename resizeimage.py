from PIL import Image

def makeSquare(im, minSize = 256, fillColor = (0, 0, 0, 0)):
    x, y = im.size
    size = max(minSize, x, y)
    newImage = Image.new('RGBA', (size, size), fillColor)
    formatImage = ((size - x) / 2, (size - y) / 2)
    newImage.paste(im, formatImage)
    return newImage

#Test Code:
testImage = Image.open(test.jpg)
newImageage = makeSquare(testImage)
newImageage.show()
