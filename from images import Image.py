from images import Image

image = Image("bilal.gif")

blackPixel = (0,0,0)

whitePixel (255,255,255)

for y in range(image.getHeight()):

    for x in range(image.getWidth()):

             (r,g,b) image.getPixel(x,y)

             avg = (r+g+b)/3

             if avg<128:

                 image.setPixel(x,y,blackPixel)

             else:

                 image.setPixel(x,y,whitePixel)

image.draw()