from Task1a import *


def hybrid(I1, I2, h):
    m = np.matrix(applyFilterInFD(I1, h)[0]) + np.matrix(applyFilterInFD(I2, h, True)[0])
    return Image.fromarray(m)

if __name__ == "__main__":
    I1 = Image.open(getImagePath("bush.tiff")).convert('L')
    I2 = Image.open(getImagePath("clinton.tiff")).convert('L')
    I3 = hybrid(I2, I1, np.array(hg))
    I3.show()
    '''
    I3.save(getImagePath("Task-1c-Clush.png", True))
    '''
