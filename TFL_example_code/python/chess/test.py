import imp
from PIL import Image
from piece_dict import piece_icons

from PIL import Image
im = Image.open(piece_icons["queen"], 'r')
width, height = im.size
pixel_values = list(im.getdata())
print(pixel_values)