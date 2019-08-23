# http://www.pythonchallenge.com/pc/return/5808.html

# Steps i used to solve challenge:
# 1. In the page source, the hit was "even, odd" and i am given a picture
#    with every other pixel a shade of black
# 2. Because of this, i figured the answer would be hidden in the different 
#    shades of black so i removed all those pixels and placed them on a new image

from PIL import Image

image = Image.open("challenge_11_cave.jpg")
# size = width, height = image.size

width = image.size[0]
height = image.size[1]

answer_image = Image.new('RGB', (width, height))

for x in range(0,width,2):
    for y in range(0,height,2):
        even_color = image.getpixel((x,y))
        odd_color = image.getpixel((x+1,y+1))

        answer_image.putpixel((x,y), even_color)
        answer_image.putpixel((x,y), odd_color)

answer_image.save("challenge_11_answer.jpg")