from PIL import Image
from random import randint
from math import floor
import os


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
            newM[y + offset][x + offset] = applyPixel(M, h, x, y)
    return newM

def matrixToImage(M):
    line = [i for row in M for i in row]
    I = Image.new('L', (len(M[0]), len(M)))
    I.putdata(line)
    return I

def imageToMatrix(I):
    data = list(I.convert('L').getdata())
    width, height = I.size
    return [data[row * width:(row + 1) * width] for row in range(height)]

def printMatrix(A):
    for row in A:
        print(row)

def getImagePath(imageName, save=False):
    path = os.path.dirname(os.path.abspath(__file__))
    path += ("\\processed images\\" if save else "\\images\\") + imageName
    return path

ha = [[1/9 for _ in range(3)] for _ in range(3)]
h = [[1, 4, 6, 4, 1],
     [4, 16, 24, 16, 4],
     [6, 24, 32, 24, 6],
     [4, 16, 24, 16, 4],
     [1, 4, 6, 4, 1]]
hg = [[i * 1/256 for i in row] for row in h]

if __name__ == "__main__":
    M1 = imageToMatrix(Image.open(getImagePath("5.1.10-aerial.tiff")))
    I2 = matrixToImage(applyFilter(M1, ha))
    I3 = matrixToImage(applyFilter(M1, hg))
    I2.show()
    I3.show()
    #I2.save(getImagePath("Task-3a-haFilter.bmp", True))
    #I3.save(getImagePath("Task-3a-hgFilter.bmp", True))
