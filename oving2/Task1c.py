from Task1a import *


def hybrid(I1, I2, h):
    xPad, yPad = I1.size
    xHPad, yHPad = 2 * xPad - len(h), 2 * yPad - len(h)
    f1 = np.lib.pad(np.array(I1), ((0, xPad), (0, yPad)), 'constant', constant_values=0)
    f2 = np.lib.pad(np.array(I2), ((0, xPad), (0, yPad)), 'constant', constant_values=0)
    h = np.lib.pad(h, ((0, xHPad), (0, yHPad)), 'constant', constant_values=0)

    F1 = np.fft.fft2(f1)
    F2 = np.fft.fft2(f2)
    H1 = np.fft.fft2(h)
    H2 = 1 - H1
    G1 = np.multiply(F1, H1)
    G2 = np.multiply(F2, H2)
    G3 = G1 + G2

    g = np.fft.ifft2(G3).real
    return Image.fromarray(g[:xPad, :yPad]).convert('L')


if __name__ == "__main__":
    I1 = Image.open(getImagePath("bush.tiff")).convert('L')
    I2 = Image.open(getImagePath("clinton.tiff")).convert('L')
    I3 = hybrid(I1, I2, np.array(hg))
    I3.show()
    '''
    I3.save(getImagePath("Task-1c-Clush.png", True))
    '''
