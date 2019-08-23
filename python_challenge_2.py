# http://www.pythonchallenge.com/pc/def/ocr.html

# Steps i used to solve challenge:
# 1. The hint in the page source siad "find rare characters in the mess below:"
#    and it was followed by a bunch of random characters with few letters in it
# 2. I figured that these letters would be the answer 

import string

lower = string.ascii_lowercase 
upper = string.ascii_uppercase
file = open("challenge_2.txt", "r").read().split("<!--")[2]


chars = [x for x in file if (x in upper or x in lower)]

string = "".join(chars)

print ("The answer is: " + string)

