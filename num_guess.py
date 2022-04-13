# GitHub username: CtheBoyd
# Date: 4/12/2022
# Description: Two players. First player chooses an integer. Second player has to guess it.
#
#player_1 = x
#player_2 = y
#attempts = z
print ("Enter the integer for the player to guess.")
x = int(input())
print("Enter your guess.")
y = int(input())
z = 0
while x != y:
    z += 1
    if y > x:
        print ("Too high - try again:")
        y = int(input())
    elif y < x:
        print ("Too low - try again:")
        y = int(input())
if y == x:
    z += 1
    print ("you guessed it in", z, "tries.")

