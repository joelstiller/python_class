# Assignment: Making and Reading from Dictionaries
# Create a dictionary containing some information about yourself. The keys should include name, age, country of birth, favorite language.

# Write a function that will print something like the following as it executes:

# My name is Anna
# My age is 101
# My country of birth is The United States
# My favorite language is Python

info = {
    "name":"John Doe",
    "age":"25",
    "country of birth":"The United States",
    "favorite language":"node.js"
}

def parse_dict(in_dict):
    for key,value in in_dict.iteritems():
        print "My {} is {}".format(key,value)

parse_dict(info)