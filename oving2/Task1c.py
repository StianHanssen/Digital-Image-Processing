from Task1a import *


def hybrid(I1, I2, h):
    hi = (1 - np.matrix(h))
    F1, _, _, AH1 = applyFilterInFD(I1, h)
    F2, _, _, AH2 = applyFilterInFD(I1, hi)
    print(h)
    print(hi)
    AH1.show()
    AH2.show()
    T2 = applyFilterInFD(I2, hi)
    m3 = np.matrix(F1) + np.matrix(F2)
    maxVal = m3.max()
    m3 *= 255/maxVal
    return Image.fromarray(m3)

if __name__ == "__main__":
    I1 = Image.open(getImagePath("bush.tiff")).convert('L')
    I2 = Image.open(getImagePath("clinton.tiff")).convert('L')
    H = np.fft.fft2(h)
    I3 = hybrid(I2, I1, np.array(lowPass))
    I3.show()
    '''
    I3.save(getImagePath("Task-1c-Clush.png", True))
    '''
