'''
Following Links in Python
The program will use urllib to read the HTML from the data files below, extract the href= vaues from the anchor tags, scan for a tag that is in a particular position relative to the first name in the list, follow that link and repeat the process a number of times and report the last name you find.

We provide two files for this assignment.

Problem 1: Start at http://py4e-data.dr-chuck.net/known_by_Fikret.html 
Find the link at position 3 (index 2). Follow that link. Repeat this process 4 times. The answer is the last name that you retrieve.
Sequence of names: Fikret Montgomery Mhairade Butchi Anayah 
Last name in sequence: Anayah

Problem 2: Start at: http://py4e-data.dr-chuck.net/known_by_Rajwinder.html 
Find the link at position 18 (index 17). Follow that link. Repeat this process 7 times. The answer is the last name that you retrieve.
Hint: The first character of the name of the last page that you will load is: K

Strategy
The web pages tweak the height between the links and hide the page after a few seconds to make it difficult for you to do the assignment without writing a Python program. 
But frankly with a little effort and patience you can overcome these attempts to make it a little harder to complete the assignment without writing a Python program. 
But that is not the point. The point is to write a clever Python program to solve the program.
'''

from bs4 import BeautifulSoup as bs
from urllib.request import urlopen

# Ask the user to input URL, count and position of name
url = input('Enter URL: ')
if len(url)<1 : url = 'http://py4e-data.dr-chuck.net/known_by_Fikret.html'
count = int(input('Enter count: '))
pos = int(input('Enter position: '))-1
next_link = None

# Create a loop to extract the link and the name 'count' number of times
while count>0:

    # Change the url except for the first time
    if next_link is not None: url = next_link
    print ('Retrieving: '+url)

    #Open the url and extract the anchor tags
    soup = bs(urlopen(url), 'html.parser')
    tags = soup('a')

    #Find the link at the specified position and extract the name
    tag = tags[pos]
    next_link = tag.get('href', None)
    name = tag.contents[0]

    #Decrement the count variable
    count-=1

# Print the final name
print ('The final name is:',name)
