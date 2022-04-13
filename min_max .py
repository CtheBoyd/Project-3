# Author: Christopher Boyd
# GitHub username: CtheBoyd
# Date: 4/12/2022
# Description: Returns max/min on user chosen, at random, number of user inputs.
#
input_1 = int(input(("How many integerts would you like to enter?\n")))
print("Please enter" + " " + str(input_1) + " " + "integers.")
min = 1.7976931348623157e+308
max = -1.7976931348623157e+308
for input_2 in range(0, input_1):
    input_2 = int(input())
    if input_2 < min:
       min = input_2
    if input_2 > max:
        max = input_2
print("min:", min)
print("max:", max)






