from Task2b import *

def subtract(M1, M2):
    newM = [[0 for i in range(len(M1[0]))] for j in range(len(M1))]
    for y in range(len(M1)):
        for x in range(len(M1[0])):
            if M1[y][x] != M2[y][x]:
                newM[y][x] = M1[y][x]
    return newM

def hits(A, F, start_x, start_y):
    for col_i in range(len(F)):
        for row_i in range(len(F[0])):
            if A[start_y+col_i][start_x+row_i] == 0 and F[col_i][row_i] == 1:
                return True
    return False

def dilate(M, h):
    hSize = len(h)
    width = len(M[0])
    height = len(M)
    offset = floor(hSize/2)
    newM = [[0 for i in range(len(M[0]))] for j in range(len(M))]
    for y in range(height - hSize + 1):
        for x in range(width - hSize + 1):
            if hits(M, h, x, y):
                newM[y + offset][x + offset] = 1
    return newM

def erode(M, h):
    hSize = len(h)
    width = len(M[0])
    height = len(M)
    offset = floor(hSize/2)
    newM = [[0 for i in range(len(M[0]))] for j in range(len(M))]
    for y in range(height - hSize + 1):
        for x in range(width - hSize + 1):
            if fits(M, h, x, y):
                newM[y + offset][x + offset] = 1
    return newM

if __name__ == "__main__":
    I1 = Image.open(getImagePath("Task-2a-morph.png", True)).convert('L')
    T = global_threshold(I1, 128, 1)
    I2 = segment(I1, T)
    m1 = imageToMatrix(I2)
    m2 = erode(m1, struct)
    m3 = subtract(m1, m2)
    I3 = from_bin_to_visual(matrixToImage(m3))
    I3.show()
    '''
    I3.save(getImagePath("Task-2c-boundary.png", True))
    '''
