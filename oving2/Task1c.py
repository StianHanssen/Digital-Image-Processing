from Task1a import *


def hybrid(I1, I2, h):
    I1 = applyFilterInFD(I1, h)
    I2 = applyFilterInFD(I2, h, True)
    m1 = np.matrix(imageToMatrix(I1))
    m2 = np.matrix(imageToMatrix(I2))
    m3 = m2 + m1
    return matrixToImage(m3.tolist())

if __name__ == "__main__":
    I1 = Image.open(getImagePath("bush.tiff")).convert('L')
    I2 = Image.open(getImagePath("clinton.tiff")).convert('L')
    I3 = hybrid(I1, I2, hg)
    I3.show()
