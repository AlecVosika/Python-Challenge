# http://www.pythonchallenge.com/pc/def/ocr.html


import string

lower, upper = string.ascii_lowercase, string.ascii_uppercase
file = open("challenge_2.txt", "r").read().split("<!--")[2]


chars = [x for x in file if (x in upper or x in lower)]

string = "".join(chars)

print (string)

