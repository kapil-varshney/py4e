"""
Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
X-DSPAM-Confidence:    0.8475
Count these lines and extract the floating point values from each of the lines 
and compute the average of those values and produce an output as shown below. 
Do not use the sum() function or a variable named sum in your solution.
"""


# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)

total = 0 #initialize a variable to hold the sum in
count = 0 #initialize a variable to hold the count in

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    spos = line.find(':')
    num = line[spos+1:]
    num = float(num)
    total+=num
    count+=1

print("Average spam confidence:", total/count)
