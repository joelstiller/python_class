# Assignment: Names
# Write the following function.
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

for item in students:
    print item["first_name"] + " " + item["last_name"]
print ""
# Part II
# Now, given the following dictionary:
users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }
for key in users:
    print key
    count = 1
    for each_dict in users[key]:
        total_len = len(each_dict["first_name"]) + len(each_dict["last_name"])
        print "{} - {} {} - {}".format(count,each_dict["first_name"],each_dict["last_name"],total_len)
        count += 1