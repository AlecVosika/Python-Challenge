# http://www.pythonchallenge.com/pc/return/5808.html

# Steps i used to solve challenge:
# 1. In the page source, the hit was "even, odd" and i am given a picture
#    with every other pixel a shade of black
# 2. Because of this, i figured the answer would be hidden in the different 
#    shades of black so i removed all those pixels and placed them on a new image

from PIL import Image

image = Image.open("challenge_11_cave.jpg")
(width,height) = image.size

even_image = Image.new('RGB', (width//2, height//2))
odd_image = Image.new('RGB', (width//2, height//2))

for x in range(width):
    for y in range(height):
        even_color = image.getpixel((x,y))
        odd_color = image.getpixel((x+1,y+1))
        if (x+y)%2 == 1:
            odd_image.putpixel((x // 2, y // 2), odd_color)
        else:
            even_image.putpixel((x // 2, y // 2), even_color)

even_image.save("challenge_11_answer_even.jpg")
odd_image.save("challenge_11_answer_odd.jpg")