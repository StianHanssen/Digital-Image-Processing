from Task1a import *


def sharpen(I, h):
    If = applyFilterInFD(I, h)[0]
    M = np.matrix(I)
    Mf = np.matrix(If)
    G = M + Mf
    return Image.fromarray(G)

if __name__ == "__main__":
    I1 = Image.open(getImagePath("4.2.06-lake.tiff")).convert('L')
    I2 = sharpen(I1, np.array(hs))
    I2.show()
    '''
    I2.save(getImagePath("Task-1b-SharpenedImage.png", True))
    '''
