"""
Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

Desired Output:
04 3
06 1
07 1
09 2
10 3
11 6
14 1
15 2
16 4
17 2
18 1
19 1

"""



name = input("Enter file:")
# If the user doesn't enter a filename, provide a default name
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

hr_dict = {}

#Iterate over each line in the file
for line in handle:
    
    #for each line that starts with 'From '
    if line.startswith('From '):
        
        #Stripping the line of any whitespaces, and creating a list of words
        words = line.strip().split()
        
        #Extracting the time
        time = words[5]
        time = time.split(':')
        
        #Extracting the hour and counting it in a dictionary
        hr = time[0]
        hr_dict[hr] = hr_dict.get(hr,0) + 1

# Converting the dictionary into a list and sorting it by hours
hr_list = list(hr_dict.items())
hr_list.sort()

#printing the hour and its count
for h, v in hr_list:
    print (h,v)
