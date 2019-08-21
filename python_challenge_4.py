# http://www.pythonchallenge.com/pc/def/linkedlist.php

from urllib import request
import re

url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='

url_start = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345'

page = request.urlopen(url)
contents = str(page.read())
page.close()

count = 0
while count != 400:
    count += 1
    temp = re.findall(r'\d+', contents)
    temp = list(map(int, temp))
    print(temp[0])
    next = temp[0]

    new_url = url + str(next)
    page = request.urlopen(new_url)
    content = contents = str(page.read())
    page.close()