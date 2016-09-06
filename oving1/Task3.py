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


def matrixToImage(M, maxValue):
    line = [i for row in M for i in row]
    data = [(i, maxValue) for i in line]
    I = Image.new('LA', (len(M[0]), len(M)))
    I.putdata(line)
    return I


def imageToMatrix(I):
    data = list(I.convert('LA').getdata())
    values = [i[0] for i in data]
    width, height = I.size
    return [values[row * width:(row + 1) * width] for row in range(height)], data[0][1]


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

I1 = Image.open("D:\\Prosjekter\\Universitet\\VisDat\\oving1\\images\\5.1.10-aerial.tiff")
M1, maxValue = imageToMatrix(I1)
I2 = matrixToImage(applyFilter(M1, ha), maxValue)
I2.show()
