from PIL import Image
from Task3a import getImagePath

def f(p):
    return 255 - p

if __name__ == "__main__":
    I1 = Image.open(getImagePath("5.2.09-aerial.tiff"))
    I1.show()
    I2 = I1.point(lambda i: f(i))
    I2.show()
    #I2.save(getImagePath("Task-2a-invertFilter.bmp", True))
