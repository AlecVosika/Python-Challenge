# http://www.pythonchallenge.com/pc/def/integrity.html

# Steps i used to solve challenge:
# 1. Checked the page source and saw the "us" and "pw" section followed by random text
# 2. I clicked on the picture ans saw that it wanted me to type in a username and password
# 3. Noticed the inflate hint in this popup so i googled "python inflate"
# 4. This showed me that it was simply needing to be decompressed

import bz2

un = bz2.decompress(b"BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084")
un = un.decode("utf-8")
print("username: " + un)

pw = bz2.decompress(b"BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08")
pw = pw.decode("utf-8")
print("password: " + pw)

