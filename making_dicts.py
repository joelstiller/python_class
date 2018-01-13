# Assignment: Making Dictionaries
# Create a function that takes in two lists and creates a single dictionary. The first list contains keys and the second list contains the values. 
# Assume the lists will be of equal length.

# Your first function will take in two lists containing some strings. Here are two example lists:

name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar","Newthing"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llama"]

def make_dict(list1, list2):
    new_dict = {}
    if len(list1) >= len(list2):
    #list 1 is key
        for i in range(0,len(list1)):
            try:
                new_dict[list1[i]] = list2[i]
            except IndexError:
                new_dict[list1[i]] = None
    else:
        for i in range(0,len(list2)):
            try:
                new_dict[list1[i]] = list2[i]
            except IndexError:
                new_dict[list2[i]] = None
    #list 2 is key
    # your code here
    return new_dict

blah = make_dict(name,favorite_animal)
print blah