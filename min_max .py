# Author: Christopher Boyd
# GitHub username: CtheBoyd
# Date: 4/12/2022
# Description: Returns max/min on user chosen, at random, number of user inputs.
#
print ("How many integers would you like to enter")
x = int(input())
print("please enter",x, " integers" )
min = 1.7976931348623157e+308
max = 0
for i in range(0, x):
    y = int(input())
    if y < min:
       min = y
    if y > max:
        max = y
print("min:", min)
print("max:", max)






