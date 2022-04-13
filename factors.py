# GitHub username: CtheBoyd
# Date: 4/12/2022
# Description: Returns the factors of a user provided positive integer.
#
x = int(input("Please enter a positive integer: "))
print ("The factors of", x, "are:")
for y in range(1, x+1):
     if x % y == 0:
         print(y)





