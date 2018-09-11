from PIL import Image
from math import floor

def crop_image():
    image = Image.open('./Images/t05.jpg')
    width, height = image.size

    bottom_increment = floor(height/3)

    right = width
    down = bottom_increment
    up = 0
    i_name = 0
    overlap = 25

    while up <= floor(height/3)*2:
    	coords = (0,up,right,down)

    	cropped_image = image.crop(coords)
    	cropped_image.save('./Images/test_crop_' + str(i_name) + '.jpg')

    	down+=bottom_increment
    	up = (down - bottom_increment) - overlap
    	i_name += 1

if __name__ =='__main__':
    crop_image()
