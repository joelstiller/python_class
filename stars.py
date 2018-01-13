# Assignment: Stars
# Write the following functions.

# Part I
# Create a function called draw_stars() that takes a list of numbers and prints out *.
# Part II
# Modify the function above. Allow a list containing integers and strings to be passed to the draw_stars() function. When a string is passed, instead of displaying *,
# display the first letter of the string according to the example below. You may use the .lower() string method for this part.

def make_stars(in_list):
    for item in in_list:
        if isinstance(item, int):
            out = None
            for num in range(0,item):
                if out is None:
                    out = "*"
                else:
                    out += "*"
        elif isinstance(item,str):
            out = None
            str_len = len(item)
            set_character = item[:1].lower()
            for num in range(0,str_len):
                if out is None:
                    out = set_character
                else:
                    out += set_character
        print out
a = [3,"Tom",10,7,"Bob",4,"Samewfwf"]
make_stars(a)