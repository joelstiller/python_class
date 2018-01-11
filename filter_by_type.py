# Write a program that, given some value, tests that value for its type. Here's what you should do for each type:

# Integer
# If the integer is greater than or equal to 100, print "That's a big number!" If the integer is less than 100, print "That's a small number"

# String
# If the string is greater than or equal to 50 characters print "Long sentence." If the string is shorter than 50 characters print "Short sentence."

# List
# If the length of the list is greater than or equal to 10 print "Big list!" If the list has fewer than 10 values print "Short list."

def WhatIsThis(x):
    if isinstance(x, int):
        if x >= 100:
            print "That's a big number!"
        else:
            print "That's a small number"
    elif isinstance(x, str):
        length = len(x)
        if length >= 50:
            print "Long sentence."
        else:
            print "Short sentence."
    elif isinstance(x, list):
        length = len(x)
        if length >= 10:
            print "Big list!"
        else:
            print "Short List."

WhatIsThis(45)
WhatIsThis(100)
WhatIsThis(455)
WhatIsThis(0)
WhatIsThis(-23)
WhatIsThis("Rubber baby buggy bumpers")
WhatIsThis("Experience is simply the name we give our mistakes")
WhatIsThis("Tell me and I forget. Teach me and I remember. Involve me and I learn.")
WhatIsThis("")
WhatIsThis([1,7,4,21])
WhatIsThis([3,5,7,34,3,2,113,65,8,89])
WhatIsThis([4,34,22,68,9,13,3,5,7,9,2,12,45,923])
WhatIsThis([])
WhatIsThis(['name','address','phone number','social security number'])