'''
Extracting Data from JSON
The program will prompt for a URL, read the JSON data from that URL using urllib and then parse and extract the comment counts from the JSON data, and compute the sum of the numbers in the file. 

We provide two files for this assignment.
http://py4e-data.dr-chuck.net/comments_42.json (Sum=2553)
http://py4e-data.dr-chuck.net/comments_64155.json (Sum ends with 64)

You do not need to save these files to your folder since your program will read the data directly from the URL.
'''


import urllib.request
import json

# The URL to be used for extracting JSON
url1 = 'http://py4e-data.dr-chuck.net/comments_42.json'
url2 = 'http://py4e-data.dr-chuck.net/comments_64155.json'

#Open the url, read the json and load it
data = urllib.request.urlopen(url2).read().decode()
info = json.loads(data)

#Extract all the integers in 'count' and sum them up
'''
num = []
comments = info['comments']
for comment in comments:
    num.append(comment['count'])
print(sum(num))
'''

#Using List comprehension
print('Sum:',sum([comment['count'] for comment in info['comments']]))
