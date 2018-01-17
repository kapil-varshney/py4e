"""
Strings
6.5 Write code using find() and string slicing (see section 6.10) 
to extract the number at the end of the line below. 
Convert the extracted value to a floating point number and print it out.
"""

# Given text
text = "X-DSPAM-Confidence:    0.8475"

#Finding the starting position
spos = text.find('0')

# Slicing the required string and converting it into float
num = float(text[spos:])

print(num)
