from Task1a import *

def fits(A, F, start_x, start_y):
    for col_i in range(len(F)):
        for row_i in range(len(F[0])):
            if A[start_y+col_i][start_x+row_i] == 0 and F[col_i][row_i] == 1:
                return False
    return True

def custom_erode(M, h, grayM, i):
    hSize = len(h)
    width = len(M[0])
    height = len(M)
    offset = floor(hSize/2)
    newM = [[0 for i in range(len(M[0]))] for j in range(len(M))]
    for y in range(height - hSize + 1):
        for x in range(width - hSize + 1):
            if fits(M, h, x, y):
                newM[y + offset][x + offset] = 1
            elif M[y + offset][x + offset] == 1:
                grayM[y + offset][x + offset] = i
    return newM, grayM

def contains_one(M):
    for row in M:
        for e in row:
            if e == 1:
                return True
    return False

def distance_transform(M, S):
    i = 0
    grayM = [[0 for i in range(len(M[0]))] for j in range(len(M))]
    while contains_one(M):
        M, grayM = custom_erode(M, S, grayM, i)
        i += 1
    return grayM, i

def expand_values(M, max_val):
    factor = 255 // max_val
    return [[e * factor for e in row] for row in M]

struct = [[1 for _ in range(3)] for _ in range(3)]

if __name__ == "__main__":
    I1 = Image.open(getImagePath("Task-2a-morph.png", True)).convert('L')
    T = global_threshold(I1, 128, 1)
    I2 = segment(I1, T)
    m, max_val = distance_transform(imageToMatrix(I2), struct)
    m2 = expand_values(m, max_val)
    I3 = matrixToImage(m2)
    I3.show()
    '''
    I3.save(getImagePath("Task-2b-distance-transform.png", True))
    '''
