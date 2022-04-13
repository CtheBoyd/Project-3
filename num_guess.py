# GitHub username: CtheBoyd
# Date: 4/12/2022
# Description: Two players. First player chooses an integer. Second player has to guess it.
#

print("Enter the integer for the player to guess.")
num1 = int(input())
print("Enter your guess.")
num2 = int(input())
num3 = 1
while num1 != num2:
    num3 += 1
    if num2 > num1:
        print("Too high - try again:")
        num2 = int(input())
    elif num2 < num1:
         print("Too low - try again:")
         num2 = int(input())
if num3 == 1:
    print("you guessed it in 1 try.")
else:
    print("you guessed it in", num3 ,"tries.")

