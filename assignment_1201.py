'''
Scraping Numbers from HTML using BeautifulSoup

The program will use urllib to read the HTML from the data files below, and parse the data, extracting numbers and compute the sum of the numbers in the file.

We provide two files for this assignment:

http://py4e-data.dr-chuck.net/comments_42.html (Sum = 2553)
http://py4e-data.dr-chuck.net/comments_64152.html (Sum = 2600)

You do not need to save these files to your folder since your program will read the data directly from the URL.

Hint: 
Look at the source code(HTML) of each file. 
Notice the tag within which you have the numbers. Try to extract those specific tags and their contents using BeautifulSoup.
Be careful of what the return type of each method is (string or a list or something else?).
'''

from bs4 import BeautifulSoup as bs
from urllib.request import urlopen

# Create variables to hold the links
link1= 'http://py4e-data.dr-chuck.net/comments_42.html'
link2 = 'http://py4e-data.dr-chuck.net/comments_64152.html'

'''
#Open the link and make a BeautifulSoup object
html = urlopen(link1)
soup = bs(html, 'html.parser')

#Extract all span tags and their contents
spans = soup('span')
sumnum = 0

#Iterate over each span in the list spans
for span in spans:
    #print (span.contents)
    sumnum = sumnum+int(span.contents[0])

print(sumnum)
'''

#Using List comprehension
print(sum([int(span.contents[0]) for span in bs(urlopen(link2), 'html.parser')('span')]))
