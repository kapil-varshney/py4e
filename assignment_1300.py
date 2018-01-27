import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

# The URL used to extrat the XML
url1 = 'http://py4e-data.dr-chuck.net/comments_42.xml'
url2 = 'http://py4e-data.dr-chuck.net/comments_64154.xml'

# Open the URL, read the data and convert it into an XML tree
uh = urllib.request.urlopen(url2)
data = uh.read()
tree = ET.fromstring(data)

# look for the count tag and extract the integers in a list
#nums = [x.find('count').text for x in tree.find('comments').findall('comment')]
nums = [int(x.text) for x in tree.findall('.//count')]

#print the sum of the integers
print (sum(nums))
