# http://www.pythonchallenge.com/pc/def/equality.html

import re

file = open("challenge_3.txt", "r").read()

code = file

word = "".join(re.findall('[a-z][A-Z]{3}([a-z])[A-Z]{3}[a-z]', code))

print(word)