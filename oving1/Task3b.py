from Task3a import *


def imageToRGBMatrix(I):
    data = list(I.getdata())
    width, height = I.size
    M = [None, None, None]
    for i in range(3):
        M[i] = [[j[i] for j in data[row * width:(row + 1) * width]] for row in range(height)]
    return M


def matrixToRGBImage(Mr, Mg, Mb):
    M = [Mr, Mg, Mb]
    I = [matrixToImage(M[i]) for i in range(3)]
    return Image.merge('RGB', (I[0], I[1], I[2]))

if __name__ == "__main__":
    M1 = imageToRGBMatrix(Image.open(getImagePath("4.2.06-lake.tiff")))
    M2 = [applyFilter(m, ha) for m in M1]
    M3 = [applyFilter(m, hg) for m in M1]
    I1 = matrixToRGBImage(M2[0], M2[1], M2[2])
    I2 = matrixToRGBImage(M3[0], M3[1], M3[2])
    I1.show()
    I2.show()
    #I1.save(getImagePath("Task-3b-haFilter.bmp", True))
    #I2.save(getImagePath("Task-3b-hgFilter.bmp", True))
