# GitHub username: CtheBoyd
# Date: 4/12/2022
# Description: Returns max/min on user chosen, at random, number of user inputs.
#

print ("Enter the integer for the player to guess.")
x = int(input())
print("Enter your guess.")
y = int(input())
if y < x:
    z = False
    print ("too low - try again:")
elif y > x:
    z = False
    print ("too high - try again:")

elif y == x:
    z = True
    print ("You guessed it in", total, "tries.")
