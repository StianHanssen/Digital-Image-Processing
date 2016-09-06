from Task3a import *
from math import sqrt


def calculateMagnitude(Mx, My):
    return [[floor(sqrt((Mx[y][x] ** 2) + (My[y][x] ** 2))) for x in range(len(Mx[0]))] for y in range(len(Mx))]

sx = [[1, 0, -1],
      [2, 0, -2],
      [1, 0, -1]]

sy = [[1, 2, 1],
      [0, 0, 0],
      [-1, -2, -1]]

'''
M1 = imageToMatrix(Image.open("D:\\Prosjekter\\Universitet\\VisDat\\oving1\\images\\5.1.10-aerial.tiff"))
Mx = applyFilter(M1, sx)
My = applyFilter(M1, sy)
Mm = calculateMagnitude(Mx, My)
Ix = matrixToImage(Mx)
Iy = matrixToImage(My)
Im = matrixToImage(Mm)
Ix.show()
Iy.show()
Im.show()
#Ix.save("D:\\Prosjekter\\Universitet\\VisDat\\oving1\\processed images\\Task-3c-XGradient.bmp")
#Iy.save("D:\\Prosjekter\\Universitet\\VisDat\\oving1\\processed images\\Task-3c-YGradient.bmp")
#Im.save("D:\\Prosjekter\\Universitet\\VisDat\\oving1\\processed images\\Task-3c-Magnitude.bmp")
'''
