name = input("Enter your name : ")
print("welcome", name, "to this adventure.!")

answer = input("You are on a dirt road, it has come to an end and you can go left or right. Which way would you link to go? ").lower()

if answer == "left":
    answer = input("you come to a river, you can walk around it or swim accross? Type walk to walk and swim to swim across: ").lower()
    if answer == 'walk':
        print("you walked for many miles, ran out of water and you lost the game.")
    elif answer == 'swim':
        print("You swam across and were eaten by an alligator.")
    else:
        print("Not valid option. you lose.")

elif answer == "right":
    answer = input("You come to a bridge. it looks wobbly, do you want to cross it or head back? (cross/back) : ").lower()
    if answer == 'back':
        print("You go back and lose.")
    elif answer == 'cross':
        answer = input("You cross the bridge and meet a stranger, Do you talk them (yes/no)?").lower()
        if answer == 'yes':
            print("You talk to the stranger and they give you gold, you win!")
        elif answer == 'no':
            print("You ignore the stranger and they are offended and you lose.")
        else:
            print("Not valid option. you lose.")
    else:
        print("Not valid option. you lose.")

else:
    print("Not valid option. you lose.")

print(f"Thank you for trying {name}.")