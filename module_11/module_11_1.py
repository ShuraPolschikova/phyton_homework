from PIL import Image, ImageDraw

with Image.open("mops.jpg") as im:
    draw = ImageDraw.Draw(im)
    draw.line((0, 0) + im.size, fill=128)
    draw.line((0, im.size[1]/2, im.size[0]/2, 0), fill=128)
    draw.line((0, im.size[1], im.size[0], 0), fill=128)
    draw.line((0, im.size[1]*3/4, im.size[0]*3/4, 0), fill=128)
    im.show()


print(im.format)
print(im.fp)
print(im.size)
print(im.mode)
print(im.getbands())
