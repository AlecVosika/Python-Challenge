# http://www.pythonchallenge.com/pc/def/channel.html

# steps i used to solve
# 1. View page source and notice "zip" comment in html  
# 2. Replace .html in the url with .zip
# 3. Extract the zip file to a folder
# 4. Read the readme.txt file for hint

from urllib import request
import re
import zipfile

####################################################
# The code below was used to open every file until it hit the last one
# The last file told me to "collect the comments"
####################################################
file_location = "challenge_6_files\\"
first_file = "challenge_6_files\\90052.txt"

first_file = open(first_file)
contents = first_file.read()
first_file.close()
print(contents)

count = 1
while count != 2000:
    try:
        count += 1
        temp = re.findall(r'\d+', contents)
        temp = list(map(int, temp))
        print(temp[0])
        next = temp[0]
        
        next_file = str(file_location + str(next) + ".txt")
        
        next_file = open(next_file)
        contents = next_file.read()
        next_file.close()
        pass

    except IndexError:
        break
print("total number of files in channel.zip is 910")
print("Files opened: " + str(count))

############################################################
# The code below needed to utilize the zipfile library
# because zipped files can have comments attached to them.
# This means that we need to extract those comments
############################################################
zip_file = zipfile.ZipFile( "challenge_6_files\\channel.zip" )

comments = []

def next_nothing( filename ):
    text = zip_file.read( filename )
    next = text.split( )[-1]
    next = next.decode("utf-8")

    if( next != "comments." ):
        next_nothing( next + ".txt" )
        comments.append(zip_file.getinfo( next + ".txt" ).comment)

next_nothing( "90052.txt" )

for comment in reversed( comments ):
    comment = comment.decode("utf-8")
    print ( comment, end="" )
