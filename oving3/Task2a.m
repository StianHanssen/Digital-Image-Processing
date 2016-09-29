im = imread('processed images\Task-2a-noisy-bin.tiff');
s = strel('disk', 6);
im2 = imclose(im, s);
s = strel('disk', 7);
im3 = imopen(im2, s);
imshow(im3)
imwrite(im3,'processed images\Task-2a-morph.png')