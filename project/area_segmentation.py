from Task1b import *
from Task3c import *
from wpa_testing import *
from PIL import ImageEnhance, ImageFilter


def extract_piece(name, x, y):
    x1, x2 = x * 100, (x + 1) * 100
    y1, y2 = y * 100, (y + 1) * 100
    im = Image.open(getImagePath(name))
    im = im.crop((x1, y1, x2, y2)).crop((4, 4, 96, 96))
    return im

def extract_all(im, dimensions):
    width, height = im.size
    p_width, p_height = width / dimensions[0], height / dimensions[1]
    pieces = []
    for y in range(dimensions[1]):
        for x in range(dimensions[0]):
            x1, x2 = x * p_width, (x + 1) * p_width
            y1, y2 = y * p_height, (y + 1) * p_height
            im2 = im.crop((x1, y1, x2, y2)).crop((4, 4, 96, 96))
            pieces.append(im2)
    return pieces

def inverter(im):
    width, height = im.size
    m = imageToMatrix(im)
    corner_sum = m[0][0] + m[0][1] + m[1][0]
    corner_sum += m[0][-1] + m[0][-2] + m[1][-1]
    corner_sum += m[-1][0] + m[-1][1] + m[-2][0]
    corner_sum += m[-1][-1] + m[-1][-2] + m[-2][-1]
    return invert_bin(im) if corner_sum > 6 else im

def invert_bin(im):
    def f(p):
        return 1 - p
    return im.point(lambda i: f(i))

if __name__ == "__main__":
    im1 = Image.open(getImagePath("difficult01.png"))
    im1 = map_color_wta(im1).convert('L')
    im1.show()
    for im in extract_all(im1, (8, 5)):
        m = inverter(region_growing_method(im, tuple([(1, 1)]), 1))
        m = from_bin_to_visual(m)
        m.show()
