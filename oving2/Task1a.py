import numpy as np
from ImageTools import *


def normalize(arr):
    arr = arr.astype('float')
    for i in range(3):
        minval = arr[..., i].min()
        maxval = arr[..., i].max()
        if minval != maxval:
            arr[..., i] -= minval
            arr[..., i] *= (255.0/(maxval-minval))
    return arr

def addPadding(h, width, height, value=0):
    newh = [[0 for _ in range(width)] for _ in range(height)]
    for y in range(len(h)):
        for x in range(len(h[0])):
            newh[y][x] = h[y][x]
    return newh

def applyFilterInFD(I, h, inverse=False):
    width, height = I.size
    ha = np.array(addPadding(h, 2*width, 2*height))
    if inverse:
        ha = 1 - ha
    F = np.fft.fft2(normalize(np.array(addPadding(imageToMatrix(I), 2*width, 2*height))))
    H = np.fft.fft2(ha)
    G = np.multiply(F, H)
    g = np.fft.ifft2(G).real
    return matrixToImage(g.tolist()).crop((0, 0, width, height))

def getAmplitudes(I, h):
    offset = floor(len(h)/2)
    width, height = I.size
    width += offset
    height += offset
    F = np.fft.fft2(np.array(addPadding(imageToMatrix(I), width, height)))
    H = np.fft.fft2(np.array(addPadding(h, width, height)))
    Ha = np.abs(np.fft.fftshift(H))
    Fa = np.abs(np.fft.fftshift(F))
    G = np.multiply(F, H)
    Ga = np.abs(np.fft.fftshift(G))
    return matrixToImage(Fa.tolist()), matrixToImage(Ha.tolist()), matrixToImage(Ga.tolist())

if __name__ == "__main__":
    I1 = Image.open(getImagePath("bush.tiff")).convert('L')
    I2 = applyFilterInFD(I1, hg)
    Ab, Af, Aa = getAmplitudes(I1, hg)
    Ab.show()
    Aa.show()
    Af.show()
    I1.show()
    I2.show()
