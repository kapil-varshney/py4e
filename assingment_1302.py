'''
Calling a JSON API
The program will prompt for a location, contact a web service and retrieve JSON for the web service and parse that data, and retrieve the first place_id from the JSON. A place ID is a textual identifier that uniquely identifies a place as within Google Maps.

API End Points
To complete this assignment, you should use this API endpoint that has a static subset of the Google Data:

http://py4e-data.dr-chuck.net/geojson?

This API uses the same parameter (address) as the Google API. This API also has no rate limit so you can test as often as you like. If you visit the URL with no parameters, you get a list of all of the address values which can be used with this API. To call the API, you need to provide address that you are requesting as the address= parameter that is properly URL encoded using the urllib.urlencode() fuction.

You can test to see if your program is working with a location of:
"South Federal University" 
place_id: "ChIJJ8oO7_B_bIcR2AlhC8nKlok". 
"allama iqbal open university islamabad" 
place_id: "ChIJA1SH1B1qIjkR5PsU3PVJ0x0"
'''

import json
import urllib.request, urllib.parse

# Initialize the api link and ask the user for the location
api = 'http://py4e-data.dr-chuck.net/geojson?'
location = input('Please enter the location: ')
if len(location) <1: location='South Federal University'

# encode the location and add it to the url
url = api+urllib.parse.urlencode({'address':location})

# call the api and load the json
data = urllib.request.urlopen(url).read().decode()
info =json.loads(data)

# Find and print the place_id
print(info['results'][0]['place_id'])
