# GitHub username: CtheBoyd
# Date: 4/12/2022
# Description: Returns the factors of a user provided positive integer.
#

input_1 = int(input("Please enter a positive integer: "))
print ("The factors of", input_1, "are:")
for num in range(1, input_1 +1):
     if input_1 % num == 0:
         print(num)





