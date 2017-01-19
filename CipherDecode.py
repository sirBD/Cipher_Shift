import string
import collections

def caesar(rotate_string, rotate_number):
    upper = collections.deque(string.ascii_uppercase)
    lower = collections.deque(string.ascii_lowercase)

    upper.rotate(rotate_number)
    lower.rotate(rotate_number)

    upper = ''.join(list(upper))
    lower = ''.join(list(lower))

    return rotate_string.translate(str.maketrans(string.ascii_uppercase, upper)).translate(str.maketrans(string.ascii_lowercase, lower))
#maketrans - takes the FROM argument (rotate_string) and makes it suitable for the TRANSLATE function to the TO argument (asciicharacters etc.)
our_string = "YWJJU"

for i in range(len(string.ascii_uppercase)):
    print (i, caesar(our_string, i))
    
    
#To get the key number, take the difference between 26 and the numbered value on the left of the ouput (shift number).
