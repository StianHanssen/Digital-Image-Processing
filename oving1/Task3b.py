from Task3a import *


def imageToRGBMatrix(I):
    data = list(I.getdata())
    width, height = I.size
    S = [None, None, None]
    for i in range(3):
        S[i] = [[j[i] for j in data[row * width:(row + 1) * width]] for row in range(height)]
    return S


def matrixToRGBImage(Mr, Mg, Mb):
    M = [Mr, Mg, Mb]
    I = [matrixToImage(M[i]) for i in range(3)]
    return Image.merge('RGB', (I[0], I[1], I[2]))

'''
M1 = imageToRGBMatrix(Image.open("D:\\Prosjekter\\Universitet\\VisDat\\oving1\\images\\4.1.07-jelly-beans.tiff"))
M2 = [applyFilter(m, ha) for m in M1]
M3 = [applyFilter(m, hg) for m in M1]
I1 = matrixToRGBImage(M2[0], M2[1], M2[2])
I2 = matrixToRGBImage(M3[0], M3[1], M3[2])
I1.show()
I2.show()
#I1.save("D:\\Prosjekter\\Universitet\\VisDat\\oving1\\processed images\\Task-3b-haFilter.bmp")
#I2.save("D:\\Prosjekter\\Universitet\\VisDat\\oving1\\processed images\\Task-3b-hgFilter.bmp")
'''
