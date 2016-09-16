from PIL import Image
import math
import copy
import numpy as np


__author__ = 'Håkon Hukkelås'

def image_to_matrix(image):
    im = image
    width,height = im.size
    pixels = im.getdata()
    return [[pixels[y*width+x] for x in range(height)] for y in range(height)]

def matrix_to_image(matrix,mode):
    inline_list = [x for row in matrix for x in row]
    image = Image.new(mode,(len(matrix[0]),len(matrix)))
    image.putdata(inline_list)
    return image

def applyFilterInFD(I, h):
    xPad, yPad = I.size
    xHPad, yHPad = 2 * xPad - len(h), 2 * yPad - len(h)
    f = np.lib.pad(np.array(I), ((0, xPad), (0, yPad)), 'constant', constant_values=0)
    h = np.lib.pad(h, ((0, xHPad), (0, yHPad)), 'constant', constant_values=0)
    F = np.fft.fft2(f)
    AF = np.abs(np.fft.fftshift(F))
    H = np.fft.fft2(h)
    G = np.multiply(F, H)
    AG = np.abs(np.fft.fftshift(G))
    g = np.fft.ifft2(G).real
    return Image.fromarray(g[:xPad, :yPad]), Image.fromarray(AF), Image.fromarray(AG)

def aliasing(matrix):
    new_matrix = []
    for row_index in range(0,len(matrix),2):
        new_row = []
        row = matrix[row_index]
        for index in range(0,len(row),2):
            new_row.append(row[index])
        new_matrix.append(new_row)
    return new_matrix

h_g = [[1/256, 4/256, 6/256, 4/256, 1/256],
       [4/256, 16/256, 24/256, 16/256, 4/256],
       [6/256, 24/256, 36/256, 24/256, 6/256],
       [4/256, 16/256, 24/256, 16/256, 4/256],
       [1/256, 4/256, 6/256, 4/256, 1/256]]


#intensity_matrix_to_image(image_to_intensity_matrix(im)).show() To test the image transform
