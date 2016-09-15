import numpy as np
from ImageTools import *

def applyFilterInFD(I, h):
    xPad, yPad = I.size
    xHPad, yHPad = 2 * xPad - len(h), 2 * yPad - len(h)
    f = np.lib.pad(np.array(I), ((0, xPad), (0, yPad)), 'constant', constant_values=0)
    h = np.lib.pad(h, ((0, xHPad), (0, yHPad)), 'constant', constant_values=0)
    F = np.fft.fft2(f)
    AF = np.abs(np.fft.fftshift(F))
    H = np.fft.fft2(h)
    G = np.multiply(F, H)
    AG = np.abs(np.fft.fftshift(G))
    g = np.fft.ifft2(G).real
    return Image.fromarray(g[:xPad, :yPad]), Image.fromarray(AF), Image.fromarray(AG)

if __name__ == "__main__":
    I1 = Image.open(getImagePath("bush.tiff")).convert('L')
    I2, AF, AG = applyFilterInFD(I1, np.array(hg))
    AF.show()
    AG.show()
    I2.show()
