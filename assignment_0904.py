"""
Write a program to read through the mbox-short.txt and figure out who has the sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

Desired Output:

cwen@iupui.edu 5

"""


name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
fh = open(name)

counts = dict()

for lin in fh:
    lin = lin.strip()
    if lin.startswith('From '):
        words = lin.split()
        email = words[1]
        counts[email] = counts.get(email, 0) + 1
            
big_contri = None
count = None

for k, v in counts.items():
    if count is None or v > count:
        big_contri = k
        count = v

print (big_contri, count)
