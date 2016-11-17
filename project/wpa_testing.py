from area_segmentation import *
from math import sqrt

board_colors = [(49, 96, 148), (214, 71, 53)]
colors = [(49, 96, 148), (214, 71, 53), (217, 208, 199), (59, 36, 36), (111, 165, 89), (226, 201, 59), (176, 63, 119)]

def wta(p, thresh=0.34):
    s = sum(p)
    w = max(p)
    if s > 0 and w/s >= thresh:
        return tuple([(x if x == w else 0) for x in p])
    else:
        return (0, 0, 0)

def wta2(p):
    n_red, n_green, n_blue = 255, 255, 255
    red, green, blue = p
    if red < 65 and blue < 65 and green < 65:
        return (0, 0, 0)
    if 255 - red < 100 and 255 - blue < 100 and 255 - green < 100:
        return (255, 255, 255)
    if red < green or red < blue:
        n_red = 0
    if green < red or green < blue:
        n_green = 0
    if blue < red or blue < green:
        n_blue = 0
    return (n_red, n_green, n_blue)

def wta3(p):
    closest_colors = sorted(colors, key=lambda color: distance(color, p))
    c = closest_colors[0]
    return (0, 0, 0) if c in board_colors else (255, 255, 255)

def distance(color1, color2):
    r1, g1, b1 = color1
    r2, g2, b2 = color2
    return sqrt((r1 - r2) ** 2 + (g1 - g2) ** 2 + (b1 - b2) ** 2)

def map_color_wta(image):
        im = image.copy()
        width, height = image.size
        for i in range(width):
            for j in range(height):
                im.putpixel((i, j), wta3(im.getpixel((i, j))))
        return im

if __name__ == "__main__":
    im1 = Image.open(getImagePath("easy02.png"))
    map_color_wta(im1).show()
