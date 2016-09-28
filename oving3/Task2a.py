from Task1a import *
from scipy import ndimage as nd

if __name__ == "__main__":
    I1 = Image.open(getImagePath("noisy.tiff")).convert('L')
    T = global_threshold(I1, 128, 1)
    I2 = segment(I1, T)
    I2.show()
    print(np.matrix(I2))
    m2 = nd.binary_opening(np.matrix(I2)).astype(np.int)
    I3 = Image.fromarray(m2)
    I3.show()
