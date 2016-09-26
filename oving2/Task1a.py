import numpy as np
from ImageTools import *


def applyFilterInFD(I, h, inverse=False):
    xPad, yPad = I.size
    xHPad, yHPad = 2 * xPad - len(h), 2 * yPad - len(h)
    f = np.lib.pad(np.array(I), ((0, xPad), (0, yPad)), 'constant', constant_values=0)
    h = np.lib.pad(h, ((0, xHPad), (0, yHPad)), 'constant', constant_values=0)

    F = np.fft.fft2(f)
    H = np.fft.fft2(h)
    AH = np.abs(np.fft.fftshift(H))
        H = 1 - H
    G = np.multiply(F, H)

    AmpF = np.abs(np.fft.fftshift(F))
    AmpG = np.abs(np.fft.fftshift(G))

    g = np.fft.ifft2(G).real
    return Image.fromarray(g[:xPad, :yPad]), Image.fromarray(AG), Image.fromarray(AF), Image.fromarray(AH)

def applyFilter(I, H):
    xPad, yPad = I.size
    xHPad, yHPad = 2 * xPad - len(h), 2 * yPad - len(h)
    f = np.lib.pad(np.array(I), ((0, xPad), (0, yPad)), 'constant', constant_values=0)
    F = np.fft.fft2(f)
    AF = np.abs(np.fft.fftshift(F))
    AH = np.abs(np.fft.fftshift(H))
    G = np.multiply(F, H)
    AG = np.abs(np.fft.fftshift(G))
    g = np.fft.ifft2(G).real
    return Image.fromarray(g[:xPad, :yPad]), Image.fromarray(AG), Image.fromarray(AF), Image.fromarray(AH)

def SpaceToFrequency(h, size):
    xHPad, yHPad = 2 * size[0] - len(h), 2 * size[1] - len(h)
    h = np.lib.pad(np.array(h), ((0, xHPad), (0, yHPad)), 'constant', constant_values=0)
    return np.fft.fft2(h)

if __name__ == "__main__":
    I1 = Image.open(getImagePath("bush.tiff")).convert('L')
    I2, AF, AG, _ = applyFilterInFD(I1, np.array(hg))
    AF.show()
    AG.show()
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
