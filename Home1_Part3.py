"""
Filename: Game_Homework1_Part3
Author:Angie Lee
Date:09/01/2024
Function: A game that contain three options which are dice roll,coin flip,and card draw
"""
import random
import dice_roll
import card
import coin

#Game begins here
def game():
    while True:
        #Select a game here

        print("Select an option: ")
        print("1.Roll a dice.")
        print("2.Flip a coin.")
        print("3.Draw a card.")
        print("4.Quit.")
        # Taking user input here
        choice = input("Enter your choice here: ")
        #If user selected Dice roll game then we have 4 valid die options here
        if (choice == "1"):
            print("Choose a dice: ")
            print("1. 6 sided")
            print("2. 8 sided")
            print("3. 10 sided")
            print("4. 12 sided")
            #Taking die choice input here
            die_choice = input("Enter your choice here: ")

            if (die_choice == "1"):
                    result = dice_roll.roll(6)
            elif (die_choice == "2"):
                result = dice_roll.roll(8)
            elif (die_choice == "3"):
                result = dice_roll.roll(10)
            elif (die_choice == "4"):
                result = dice_roll.roll(12)
            else:
                print("Option invalid")

                continue
            #Output
            print(f"You rolled a {result} sided die and got{result}")
        #If they select coin flip game
        elif(choice == "2"):
            result = coin.coin_flip()
            print(f"You flipped a coin and got: {result}")

        elif(choice == "3"):
            result = card.card_draw()
            print(f"You drew: {result}.")

        #Quit option
        elif(choice == "4"):
            print("Goodbye! See you next time!")
            
        #Other options will be invalid
        else:
            print("Invalid choice. Please select a valid option.")

game()





