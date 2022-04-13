# GitHub username: CtheBoyd
# Date: 4/12/2022
# Description: Two players. First player chooses an integer. Second player has to guess it.
#

print ("Enter the integer for the player to guess.")
player_1 = int(input())
print("Enter your guess.")
player_2 = int(input())
attempts = 0
while player_1 != player_2:
    attempts += 1
    if player_2 > player_1:
        print ("Too high - try again:")
        player_2 = int(input())
    elif player_2 < player_1:
        print ("Too low - try again:")
        player_2 = int(input())
if player_2 == player_1:
    attempts += 1
    print ("you guessed it in", attempts, "tries.")

