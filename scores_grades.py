import random
# Assignment: Scores and Grades
# Write a function that generates ten scores between 60 and 100. 
# Each time a score is generated, your function should display what the grade is for a particular score. 
# Here is the grade table:
# Score: 60 - 69; Grade - D
# Score: 70 - 79; Grade - C
# Score: 80 - 89; Grade - B
# Score: 90 - 100; Grade - A
def grades():
    print "Scores and Grades"
    for i in range(0,10):
        random_num = random.randint(60,100)
        if random_num < 70:
            print "Score: {}; Your grade is {}".format(random_num,"D")
        elif random_num < 80:
            print "Score: {}; Your grade is {}".format(random_num,"C")
        elif random_num < 90:
            print "Score: {}; Your grade is {}".format(random_num,"B")
        else:
            print "Score: {}; Your grade is {}".format(random_num,"A")
    print "End of Program. Bye!"
grades()            
