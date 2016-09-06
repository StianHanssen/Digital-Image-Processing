from PIL import Image
from random import randint
from math import floor


def applyPixel(M, h, x, y):
    value = 0
    for i in range(len(h)):
        for j in range(len(h)):
            value += floor(M[y + i][x + j] * h[i][j])
    return value


def applyFilter(M, h):
    hSize = len(h)
    width = len(M[0])
    height = len(M)
    offset = floor(hSize/2)
    newM = [row[:] for row in M]
    for y in range(height - hSize + 1):
        for x in range(width - hSize + 1):
            newM[y + offset][x + offset] = applyPixel(M, h, x, y), M[y + offset][x + offset]
    return newM


def matrixToImage(M):
    line = [i for row in M for i in row]
    I = Image.new('LA', (len(M[0]), len(M)))
    I.putdata(line)
    return I.convert('L')


def imageToMatrix(I):
    data = list(I.convert('L').getdata())
    width, height = I.size
    return [data[row * width:(row + 1) * width] for row in range(height)]


def printMatrix(A):
    for row in A:
        print(row)

ha = [[1/9 for _ in range(5)] for _ in range(5)]
h = [[1, 4, 6, 4, 1],
     [4, 16, 24, 16, 4],
     [6, 24, 32, 24, 6],
     [4, 16, 24, 16, 4],
     [1, 4, 6, 4, 1]]
hg = [[i * 1/256 for i in row] for row in h]

'''
M1 = imageToMatrix(Image.open("D:\\Prosjekter\\Universitet\\VisDat\\oving1\\images\\5.1.10-aerial.tiff"))
I2 = matrixToImage(applyFilter(M1, ha))
I3 = matrixToImage(applyFilter(M1, hg))
I2.show()
I3.show()
I2.save("D:\\Prosjekter\\Universitet\\VisDat\\oving1\\processed images\\Task3a1.bmp")
I3.save("D:\\Prosjekter\\Universitet\\VisDat\\oving1\\processed images\\Task3a2.bmp")
'''
