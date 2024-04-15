import time
import random

import dialogueoptions
import intro
from classes import *
# from playername import Playername
from intro import *
from abilitycheck import ability_check
from dialogueoptions import *



# Main function in which the game runs

def dialogue():
    question_num = 1
    for key in dialogueoptions.startingposition:
        print(key)
        for i in options[question_num-1]:
            print(i)
    answer = input("Enter: A, B or C: ")
    answer = answer.upper()

    if answer == "A":
        for key in dialogueoptions.barposition:
            print(key)
            for i in bar_options[question_num-1]:
                print(i)
        baranswer = input("Enter: A or B: ")
        baranswer = baranswer.upper()

        if baranswer == "A":
            print("You order a Drink.")
            time.sleep(2)
            print("The Innkeeper brings you some ale.")
            time.sleep(2)
            for key in dialogueoptions.innkeeper:
                print(key)
                for i in innkeeper_options[question_num - 1]:
                    print(i)
            innkeeperanswer = input("Enter: A or B: ")
            innkeeperanswer = innkeeperanswer.upper()

            if innkeeperanswer == "A":
                print("You seem familiar.")
                time.sleep(1)
                print("I have seen someone like you perform in Anm a couple of years ago")
                time.sleep(1)
                print("Wait a minute.")
                time.sleep(1)
                print("No it cant be!")
                time.sleep(1)
                print("The Innkeeper gets on top of the counter")
                time.sleep(1)
                print("Ladies, Gentlemen and all sorts of Beings!")
                time.sleep(1)
                print("He points towards you.")
                time.sleep(1)
                print("This is the famous " + Playername.player_name)
                time.sleep(1)
                print("The Guests look at you and begin to cheer")
                time.sleep(1)
                for key in dialogueoptions.perform:
                    print(key)
                    for i in perform_options[question_num - 1]:
                        print(i)
                perform_answer = input("Enter: A or B: ")
                perform_answer = perform_answer.upper()

                if perform_answer == "A":
                    print("You get towards the hastily cleared stage in the Inn.")
                    # time.sleep(1)
                    if ability_check() < 14:
                        print("Charisma check failed!")
                    time.sleep(1)
                    for key in dialogueoptions.performance:
                        print(key)
                        for p in performance_answers[question_num - 1]:
                            print(p)
                    stageanswer = input("What are you going to do?")
                    stageanswer = performance_answers.upper()

            else:
                print("No way!")
                # time.sleep(1)
                print("The Innkeeper gets on top of the counter")
                # time.sleep(1)
                print("Ladies, Gentlemen and all sorts of Beings!")
                # time.sleep(1)
                print("He points towards you.")
                # time.sleep(1)
                print("This is the famous " + Playername.player_name)
                # time.sleep(1)
                print("The Guests look at you and begin to cheer")
                # time.sleep(1)
                for key in dialogueoptions.perform:
                    print(key)
                    for i in perform_options[question_num - 1]:
                        print(i)
                perform_answer = input("Enter: A or B: ")
                perform_answer = perform_answer.upper()

                if perform_answer == "A":
                    print("You get towards the hastily cleared stage in the Inn.")
                    # # time.sleep(1)
                    # if Player.Charisma < 14:
                    #     print("Charisma check failed!")
                    # time.sleep(1)
                    # for key in performance:
                    #     print(key)
                    #     for p in performance_answers[question_num - 1]:
                    #         print(p)
                    #
                    # stageanswer = input("What are you going to do?")
                    # stageanswer = performance_answers.upper()
                    print("YOu have reached the end.")
                    return




        else:
            return dialogue()


    if answer == "B":
        print("You see nothing of interest.")
        time.sleep(2)
        return dialogue()

    if answer == "C":
        print("YOu take smoke out of your Pipe.")
        time.sleep(2)
        return dialogue()

    else:
        return dialogue()
# ----------------------

def play_again():
    response = input("Do you want to play again?: (yes/no)")
    response = response.lower()

    if response == "yes":
        return True
    else:
        return False

# ----------------------



options = [["A. Go to the Bar.", "B. Look around you.", "C. Smoke your Pipe."]]
bar_options = [["A. Order a Drink", "B. Walk away"]]
innkeeper_options = [["A. No why do you ask?", "B. Well Yes of course i am " + Playername.player_name]]
perform_options = [["A. Of course no Problem", "B. Pardon me but another time"]]
# performance_answers =[["A. Perform a Lullaby", "B. Cause a Distraction and leave"]]
if Player.Charisma >= 14:
    performance_answers = [["A. Perform a Lullaby", "B. Cause a Distraction and leave", "C. Hidden third answer"]]
else:
    performance_answers = [["A. Perform a Lullaby", "B. Cause a Distraction and leave"]]



# new_game()
intro.new_game()
time.sleep(3)
dialogue()

while play_again():
    intro.new_game()
    time.sleep(3)
    dialogue()
print("bye!")
