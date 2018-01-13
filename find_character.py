# Assignment: Find Characters
# Write a program that takes a list of strings
#  and a string containing a single character, and prints a new list of all the strings containing that character.

def find_char(chr,xlist):
    for x in xlist:
        if chr in x:
            print x

word_list = ['hello','world','my','name','is','Anna']
find_char('o',word_list)