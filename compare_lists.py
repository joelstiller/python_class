# Assignment: Compare Lists
# Write a program that compares two lists and prints a message depending on if the inputs are identical or not.

# Your program should be able to accept and compare two lists: list_one and list_two. If both lists are identical print "The lists are the same". 
# If they are not identical print "The lists are not the same." Try the following test cases for lists one and two:

def compare(list1,list2):
    status = 1
    firstlen = len(list1)
    nextlen  = len(list2)
    if firstlen != nextlen:
        print "The lists are not the same."
    else:
        for x in range(0, firstlen):
            if list1[x] != list2[x]:
                status = 2
        if status == 1:
            print "The lists are the same."
        elif status == 2:
            print "The lists are not the same."


list_one = ['celery','carrots','bread','milk']
list_two = ['celery','carrots','bread','milk']

compare(list_one,list_two)