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
I1 = Image.open("D:\\Prosjekter\\Visdat\\oving1\\images\\4.2.06-lake.tiff")
I2 = grayify(f, im)
I3 = grayify(g, im)
I2.show()
I3.show()
'''
