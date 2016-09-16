from tools import *


__author__ = 'Håkon Hukkelås'

def do_task():
    im = Image.open("images/bush.tiff")
    im.show()
    new_im = matrix_to_image(aliasing(image_to_matrix(im)),'RGB')
    new_im.show()

do_task()
