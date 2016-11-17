from area_segmentation import *

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

def map_color_wta(image):
        im = image.copy()
        width, height = image.size
        for i in range(width):
            for j in range(height):
                im.putpixel((i, j), wta2(im.getpixel((i, j))))
        return im

im1 = Image.open(getImagePath("easy01.png"))
map_color_wta(im1).show()
