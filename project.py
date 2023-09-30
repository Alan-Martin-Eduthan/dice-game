import random

def roll():
    min=1
    max=6
    roll=random.randint(min,max)
    return roll

while True:
    player=input("enter a number between 2 and 4")
    if player.isdigit():
        player=int(player)
        if(2<=player<=4):
            break
        else:
            print("Must be between 2 and 4")
    else:
        print("Enter a digit dude")
player_score=[0 for i in range(player)]
max_score=50
while max(player_score)<max_score:
    for player_indx in range(player):
        print("\nPlayer number",player_indx+1,"turn just started!\n")
        current_score=0
        while True:
            should_roll=input("would you like to roll")
            if should_roll.lower()!='y':
                break
            value=roll()
            if value==1:
                print("You rolled a 1! turn done")
                current_score=0
                break
            else:
                current_score+=value
                print("you rolled a:",value)
            print("Your current score is:",current_score)
        player_score[player_indx]+=current_score
        print("Your total score:",player_score[player_indx])

