from Task1a import *


def sharpen(I, h):
    If = applyFilterInFD(I, h)[0]
    M = np.matrix(I)
    Mf = np.matrix(If)
    G = M + Mf
    return Image.fromarray(G)

H = [[0, -1, 0],
     [-1, 4, -1],
     [0, -1, 0]]

if __name__ == "__main__":
    I1 = Image.open(getImagePath("bush.tiff")).convert('L')
    I2 = sharpen(I1, np.array(H))
    I2.show()
