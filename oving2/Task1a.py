import numpy as np
from ImageTools import *


def applyFilterInFD(I, h, inverse=False):
    xPad, yPad = I.size
    xHPad, yHPad = 2 * xPad - len(h), 2 * yPad - len(h)
    f = np.lib.pad(np.array(I), ((0, xPad), (0, yPad)), 'constant', constant_values=0)
    h = np.lib.pad(h, ((0, xHPad), (0, yHPad)), 'constant', constant_values=0)

    F = np.fft.fft2(f)
    H = np.fft.fft2(h)
    if inverse:
        H = 1 - H
    G = np.multiply(F, H)

    AmpF = np.abs(np.fft.fftshift(F))
    AmpG = np.abs(np.fft.fftshift(G))

    g = np.fft.ifft2(G).real
    return Image.fromarray(g[:xPad, :yPad]).convert('L'), Image.fromarray(AmpF).convert('L'), Image.fromarray(AmpG).convert('L')

hs = [[0, -1, 0],
      [-1, 4, -1],
      [0, -1, 0]]

if __name__ == "__main__":
    I1 = Image.open(getImagePath("bush.tiff")).convert('L')
    I2, AF1, AG1 = applyFilterInFD(I1, np.array(hg))
    I3, AF2, AG2 = applyFilterInFD(I1, np.array(hs))
    AF1.show()
    AG1.show()
    I2.show()
    AF2.show()
    AG2.show()
    I3.show()
    '''
    AF1.save(getImagePath("Task-1a-LowPassAmpBefore.png", True))
    AG1.save(getImagePath("Task-1a-LowPassAmpAfter.png", True))
    I2.save(getImagePath("Task-1a-LowPassFiltered.png", True))
    AF2.save(getImagePath("Task-1a-HighPassAmpBefore.png", True))
    AG2.save(getImagePath("Task-1a-HighPassAmpAfter.png", True))
    I3.save(getImagePath("Task-1a-HighPassFiltered.png", True))
    '''
