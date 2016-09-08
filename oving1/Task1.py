from PIL import Image
from Task3a import getImagePath


def mean(r, g, b):
    return (r + g + b)/3

def values(r, g, b):
    return 0.2126*r + 0.715*g + 0.0722*b

def grayify(function, image):
    I = Image.new('L', image.size)
    I.putdata([function(r, g, b) for (r, g, b) in image.getdata()])
    return I

if __name__ == "__main__":
    I1 = Image.open(getImagePath("4.2.06-lake.tiff"))
    I2 = grayify(mean, I1)
    I3 = grayify(values, I1)
    I2.show()
    I3.show()
    #I2.save(getImagePath("Task-1-meanFilter.bmp", True))
    #I3.save(getImagePath("Task-1-valueFilter.bmp", True))
