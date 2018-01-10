# Find and Replace
# print the position of the first instance of the word "day". Then create a new string where the word "day" is replaced with the word "month".
words = "It's thanksgiving day. It's my birthday,too!"
print words.find("day",1)
print words.replace("day", "month", 1)

# Min and Max
# Print the min and max values in a list like this one: x = [2,54,-2,7,12,98]. Your code should work for any list.
x = [2,54,-2,7,12,98]
print "Min: " + str(min(x))
print "Max: " + str(max(x))

# Print the first and last values in a list like this one: x = ["hello",2,54,-2,7,12,98,"world"]. Now create a new list containing only the first and last values in the original list. Your code should work for any list.
x = ["hello",2,54,-2,7,12,98,"world"]
print "First: " + x[0]
last = len(x) - 1
print "Last: " + x[last]
y = [x[0],x[last]]
print y

# New List
# Start with a list like this one: x = [19,2,54,-2,7,12,98,32,10,-3,6]. Sort your list first. Then, split your list in half. Push the list created from the first half to position 0 of the list created from the second half. The output should be: [[-3, -2, 2, 6, 7], 10, 12, 19, 32, 54, 98]. Stick with it, this one is tough!
x = [19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()
x_length = len(x) - 1
half_length = x_length / 2
FirstHalf = []
output = []
for i in range(0, half_length):
    FirstHalf.append(x[i])
output.insert(0, FirstHalf)
for y in range(half_length, x_length):
    output.append(x[y])
print output


