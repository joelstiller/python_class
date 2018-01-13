# Assignment: Coin Tosses
# Write a function that simulates tossing a coin 5,000 times. Your function should print how many times the head/tail appears.
# Starting the program...
# Attempt #1: Throwing a coin... It's a head! ... Got 1 head(s) so far and 0 tail(s) so far
import random
def toss_coins():
    head_count = 0
    tail_count = 0
    for i in range(0,5000):
        a = random.random()
        rounded = round(a)
        if rounded == 0:
            head_count = head_count + 1
            print "Attempt #{}: Throwing a coin... It's a head! ... Got {} head(s) so far and {} tail(s) so far.".format(i,head_count,tail_count)
        else:
            tail_count = tail_count + 1
            print "Attempt #{}: Throwing a coin... It's a head! ... Got {} head(s) so far and {} tail(s) so far.".format(i,head_count,tail_count)            

toss_coins()