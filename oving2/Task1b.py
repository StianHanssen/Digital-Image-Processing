from Task1a import *


def sharpen(I, h):
    I1 = applyFilterInFD(I, h)
    M = np.matrix(imageToMatrix(I))
    M1 = np.matrix(imageToMatrix(I1))
    G = M + M1
    return matrixToImage(G.tolist())

H = [[0, -1, 0],
     [-1, 4, -1],
     [0, -1, 0]]

if __name__ == "__main__":
    I1 = Image.open(getImagePath("bush.tiff")).convert('L')
    I2 = sharpen(I1, H)
    Ab.show()
