from PIL import Image


def f(r, g, b):
    return (r + g + b)/3

def g(r, g, b):
    return 0.2126*r + 0.715*g + 0.0722*b

def grayify(function, image):
    I = Image.new('L', image.size)
    I.putdata([function(r, g, b) for (r, g, b) in image.getdata()])
    return I

'''
I1 = Image.open("D:\\Prosjekter\\Universitet\\VisDat\\oving1\\images\\4.2.06-lake.tiff")
I2 = grayify(f, I1)
I3 = grayify(g, I1)
I2.show()
I3.show()
#I2.save("D:\\Prosjekter\\Universitet\\VisDat\\oving1\\processed images\\Task-1-meanFilter.bmp")
#I3.save("D:\\Prosjekter\\Universitet\\VisDat\\oving1\\processed images\\Task-1-valueFilter.bmp")
'''
