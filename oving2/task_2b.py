from tools import *


__author__ = 'Håkon Hukkelås'

def do_task():
    im = Image.open("images/bush.tiff")
    im.show()
    matrix = image_to_matrix(im)
    im = applyFilterInFD(im.convert('L'),h_g)[0]
    im.show()
    new_im = matrix_to_image(aliasing(image_to_matrix(im)),'L')
    new_im.show()

do_task()
