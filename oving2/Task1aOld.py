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

def getAmplitudes(I, h, inverse=False):
    width, height = I.size
    ha = np.array(addPadding(h, 2*width, 2*height))
    if inverse:
        ha = 1 - ha
    F = np.fft.fft2(normalize(np.array(addPadding(imageToMatrix(I), 2*width, 2*height))))
    Fa = np.abs(np.fft.fftshift(F))
    H = np.fft.fft2(ha)
    Ha = np.abs(np.fft.fftshift(H))
    G = np.multiply(F, H)
    Ga = np.abs(np.fft.fftshift(G))
    return matrixToImage(Fa.tolist()), matrixToImage(Ha.tolist()), matrixToImage(Ga.tolist())

if __name__ == "__main__":
    I1 = Image.open(getImagePath("bush.tiff")).convert('L')
    I2 = applyFilterInFD(I1, hg)
    I3 = applyFilterInFD(I1, hg, True)
    Af, Ah1, Ag1 = getAmplitudes(I1, hg)
    _, Ah2, Ag2 = getAmplitudes(I1, hg, True)
    Af.show()
    Ah1.show()
    Ah2.show()
    Ag1.show()
    Ag2.show()
    I1.show()
    I2.show()
    I3.show()
