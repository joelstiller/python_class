# Odd/Even:
# Create a function called odd_even that counts from 1 to 2000. 
# As your loop executes have your program print the number of that iteration and specify whether it's an odd or even number.
def odd_even():
    for i in range(1,2001):
        if i % 2 == 0:
            print "Number is", i,". The number is even."
        else:
            print "Number is", i,". The number is odd"

# Multiply:
# Create a function called 'multiply' that iterates through each value in a list (e.g. a = [2, 4, 10, 16]) 
# and returns a list where each value has been multiplied by 5.
def multiply(in_list,mult):
    out_list = []
    for i in in_list:
        out_list.append(i * mult)
    return out_list
a = [2, 4, 10, 16]

# Hacker Challenge:
# Write a function that takes the multiply function call as an argument. Your new function should return the multiplied list as a two-dimensional list.
# Each internal list should contain the 1's times the number in the original list. Here's an example:
def layered_multiples(arr):
    # your code here
    output = []
    for i in arr:
        temp_list = []
        for num in range(0,i):
            temp_list.append(1)
        output.append(temp_list)
    return output
x = layered_multiples(multiply([2,4,5],3))
print x

