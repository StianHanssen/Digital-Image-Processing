import numpy as np
from ImageTools import *


def addPadding(h, width, height, value=0):
    newh = [[0 for _ in range(width)] for _ in range(height)]
    for y in range(len(h)):
        for x in range(len(h[0])):
            newh[y][x] = h[y][x]
    return newh

def applyFilterInFD(I, h):
    width, height = I.size
    F = np.fft.fft2(np.array(imageToMatrix(I)))
    H = np.fft.fft2(np.array(addPadding(h, width, height)))
    G = np.multiply(F, H)
    g = np.fft.ifft2(G).real
    return matrixToImage(g.tolist())

def getAmplitudes(I, h):
    width, height = I.size
    F = np.fft.fft2(np.array(imageToMatrix(I)))
    H = np.fft.fft2(np.array(addPadding(h, width, height)))
    Fa = np.abs(np.fft.fftshift(F))
    G = np.multiply(F, H)
    Ga = np.abs(np.fft.fftshift(G))
    return matrixToImage(Fa.tolist()), matrixToImage(Ga.tolist())

if __name__ == "__main__":
    I1 = Image.open(getImagePath("bush.tiff")).convert('L')
    I2 = applyFilterInFD(I1, hg)
    Ab, Aa = getAmplitudes(I1, h)
    Ab.show()
    Aa.show()
    I1.show()
    I2.show()
