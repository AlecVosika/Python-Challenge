
# http://www.pythonchallenge.com/pc/def/oxygen.html

# This challenge doesn't give us any useful info.
# because of this, im assuming we need to use the
# image library in python.

from PIL import Image


image = Image.open("challenge_7_oxygen.png")

y = 48
end = 607
step = 7 

# The image has a like of segmented blocks of grays and blacks.
# This made me think i could just extract the RGB code for them 
# and convert that number to the character equivalent
for x in range(0, end, step):
    print(chr(image.getpixel((x,y))[0]), end="")
# this gives: 
#           smart guy, you made it. the next level is 
#           [105, 110, 116, 101,103, 114, 105, 116, 121]

my_array = [105, 110, 116, 101,103, 114, 105, 116, 121]
answer = ""

# converts each decimal in array to its character equivalent
for x in my_array:
    answer += chr(x)

print("\n\n" + answer)