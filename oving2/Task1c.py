from Task1a import *

def hybrid(I1, I2, h):
    hi = 1 - np.matrix(h)
    m3 = np.matrix(applyFilterInFD(I1, h)[0]) + np.matrix(applyFilterInFD(I2, hi)[0])
    maxVal = m3.max()
    m3 *= 255/maxVal
    return Image.fromarray(m3)

lowPass = [[0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [0, 0, 1, 0, 0],
           [0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0]]

if __name__ == "__main__":
    I1 = Image.open(getImagePath("bush.tiff")).convert('L')
    I2 = Image.open(getImagePath("clinton.tiff")).convert('L')
    I3 = hybrid(I1, I2, np.array(lowPass))
    I3.show()
