"""
Open the file romeo.txt and read it line by line. 
For each line, split the line into a list of words using the split() method. 
The program should build a list of words. 
For each word on each line check to see if the word is already in the list and if not append it to the list. 
When the program completes, sort and print the resulting words in alphabetical order.


Desired Output:
['Arise', 'But', 'It', 'Juliet', 'Who', 'already', 'and', 'breaks', 'east', 'envious', 'fair', 'grief', 'is', 'kill', 'light', 'moon', 'pale', 'sick', 'soft', 'sun', 'the', 'through', 'what', 'window', 'with', 'yonder']

"""

fname = input("Enter file name: ")
fh = open(fname)
lst = list()

#Iterate over each line in text file
for line in fh:
    
    #strip the line of whitespaces and split it in words
    words = line.strip().split()
    
    #Iterate over each word in the line
    for word in words:
        
        #Append the word not already in the list
        if word not in lst:
            lst.append(word)

# Print the sorted list
lst.sort()
print(lst)

