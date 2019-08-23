# http://www.pythonchallenge.com/pc/return/bull.html

# Steps i used to solve challenge:
# 1. I opened the page source and say the title siad "what are you looking at?"
#    and there was also a txt file called "sequence" so i googled 
#    "what are you looking at sequence" and discovered the "Look-and-say sequence"
# 2. Next i needed to code the look and say sequence with the following array
#    a = [1, 11, 21, 1211, 111221... for a length of 30
# 3. Then we print the length of the answer

start = '1'

def sequence(start):

    pointer = start[0]
    count = 0
    next_pointer = ''

    for i in start:
        if i == pointer:
            count += 1
        else:
            next_pointer += str(count) + pointer
            count = 1
        
        pointer = i
    next_pointer += str(count) + pointer

    return next_pointer

for i in range(30):
    start = sequence(start)

print(len(start))