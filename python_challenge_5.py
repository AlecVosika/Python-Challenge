# http://www.pythonchallenge.com/pc/def/peak.html

# this problem does not work anymore with pickle 
# so i had to look up the answer to move on

import pickle
"Challenge_5_banner.p"

with open("Challenge_5_banner.p", 'rb') as f:
    obj = pickle.load(f)

result = ""
for outer in obj:
  for inner in outer:
    for i in range(0, inner[1]):
      result += inner[0]
  result += "\n"