# Assignment: Type List
# Write a program that takes a list and prints a message for each element in the list, based on that element's data type.

# Your program input will always be a list. For each item in the list, test its data type. If the item is a string, concatenate it onto a new string. If it is a number, add it to a running sum. At the end of your program print the string, the number and an analysis of what the list contains. If it contains only one type, print that type, otherwise, print 'mixed'.

# Here are a couple of test cases. Think of some of your own, too. What kind of unexpected input could you get?

def ProcessList (in_list):
    list_type = None
    string_out = "String: "
    int_out = 0
    for key in in_list:
        if list_type == None:
            list_type = type(key)
        elif list_type == "Mixed":
            list_type = "Mixed"
        else:
            if list_type == type(key):
                list_type = type(key)
            else:
                list_type = "Mixed"
        if isinstance(key, str):
            string_out = string_out + " " + key
        if isinstance(key, int):
            int_out = int_out + key
    print list_type
    print string_out
    print "Number Total: {}".format(int_out)

a = [1,2,"a",4,5]
ProcessList(a)
b = ['magical unicorns',19,'hello',98.98,'world']
ProcessList(b)