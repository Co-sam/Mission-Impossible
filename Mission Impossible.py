'''
Samiksha Manoj Kumar
Dec 17/ 2025
'''

locations = {'Nuclear Facility':{'The Base':'You have decided to listen to agent Swara and enter the base but you get spotted by the camera and is killed instantly along with your fellow agents!!!' ,'Security panel': 'You have decided to listen to agent Sam and went to the security panel room.','Core room':'You have decided to listen to neither of them and went to the reactor/ core room.'}}#locations
#Locations - info
win_with_luck = {1:'The locker has a bomb in it and since you opened it, you triggered the bomb!!!',2:'You find the chip in the locker but agent Swara kills you behind your back and you die as you realize that he is a traitor',3: 'You find the chip but as you take it, you accidently trigger an alarm.'}
# Unlucky wheel

import random# random is imported
x = random.randint(1,3)# Value 1 random - changes from 1,2,3 randomly
y = random.randint(1,2)# Value 2 random - changes from 1,2 randomly
luck = random.randint(1,3)


print('Welcome To Mission Impossible.')#Intro to the game
print("\nYou will be in my story and choose it's fate....") # Description of how the game works
print("Remember every choice has its own consequences....") # Warnings


name = input('\nBefore we begin, please enter your name: ') # Name of the user - the protagonist of this story
print('\nAgent '+name+" you are assigned to steal a pen drive from Russia's most guarded nuclear facility.")# Their target


# Their mission into - what they should do
print('This drive holds the core info about nuclear weapons.')
print("Your team members are agent Sam and agent Swara. You have 4 hrs time to finish this mission.")
# asking the user if they still wants to play the game / accepting the mission
confirmation = input("Your mission, should you choose to accept it - yes or no: ")


if confirmation == 'yes' or confirmation == 'Yes': # if user wants to play the game
    print("\nAs always, should you or any member of your IMF team be caught or killed, the Secretary will disavow any knowledge of your actions.\nThis message will self-destruct in five seconds....") # Rules/ precautions
    print("\n1 hr later.....") # description of the story
    print("Agent "+name+",you have now entered the entrance of Russian airport. Russia's intelligence found out your mission and they're searching for you in the airport.\nThe gates of the airport is closed except for one but you NEED to answer a puzzle to escape through that door with your fellow agents.")#Exposition


    riddle = input("\nRiddle: What is always in front of you but can’t be seen: ") # User needs to answer the riddle to survive
    riddle = riddle.lower()

    if riddle == 'future': # Riddle is right / player survived challenge 1


        print('\nYou have won the riddle and have escaped through the door....but the danger is yet to begin.')#Congrats / the game is going to get harder sign
        print("You have a choice, would you like to go to the nuclear facility without any preparations or kidnap one of russian's trusted agent to gain more information about the nuclear facility\n- Enter 1 for the first option and 2 for the second.")# Confusing / making the user believe something - more description
        print('Remember, there is only 2 more hrs left before the chip gets shipped to another country....')#Foreshadowing
        choice1 = input('Enter your choice: ') # Where the player wants to go next - nuclear facility, agent's house


        if choice1 != '1' and choice1 != '2': # If both choices aren't chosen:
            print('\nYou have not entered a valid answer, so your choice will be decided randomly....')
            choice1 = y # assigning a random value
            print('Your choice has been decided to option ',choice1) # displaying user's choice


        if choice1 == '1' or choice1 == 1:
            print('You have decided to go to nuclear facility.') # displaying where the user is going if random value is 1
        else:
            print("You have decided to go to the agent's house.") # displaying where the user is going if random value is 2


        if choice1 == '1': # story is now in nuclear facility
            #Description
            print("\nYou have now entered into Russia's nuclear facility...but you have no idea about the pen drive's location.")
            print("You can go check the base of the nuclear's facility, or go towards the security panel room, or visit the reactor/core area.")
            print("Agent Sam: Agent "+name+" I think we should visit the security panel room to gain more info about how this nuclear facility works...")
            print("Agent Swara: NO!!!, Let's check the base because if I were an agent of Russia, I would hide it somewhere where you will least except it...")
            print("Enter 1 for the base, 2 for the security panel room and 3 for the reactor/core area.")

            choice2 = input('Enter your choice: ')#location choice - where the user wants to go


            if choice2 != '1' and choice2 != '2' and choice2 != '3':# If user enter an invalid input
                print("\nYou have not chose a valid choice, thus your choice will be determined randomly.")#display what next
                choice2 = x#Random value chose
                print("You have chose option: ")
                print(choice2)#Display what choice is chosen randomly


            if choice2 == '1' or choice2 == 1:# User wants to get to the base
                print('\n'+locations['Nuclear Facility']['The Base'])
                print('Mission over.')# Game over


            elif choice2 == '2' or choice2 == 2:# User wants to get to Security panel room
                print('\n'+locations['Nuclear Facility']['Security panel'])# description
                print('You hear someone stop behind you and a click sound but before you turn around, you get shot in the head.')# someone killed the user
                print("You fall down instantly and spot the killer standing next to you, it's Agent Swara.....")# Agent swara is killed
                print('Mission over.')# Game over


            elif choice2 == '3' or choice2 == 3: # User want to go to the nuclear facility

                print('\n'+locations['Nuclear Facility']['Core room'])# location description
                print('You wander around the room looking for the chip and find a locker......')#User find the locker
                print('To open the locker, you need to answer a riddle....')# Instructions

                puzzle = input('Riddle: Until I am measured, I am not known. Yet how you miss me, when I have flown. What am I: ')# A question to open the locker
                puzzle = puzzle.lower()
                if puzzle == 'time': # Riddle answer right - user survives
                    print('\nYou have opened the locker successfully!!!')
                    winner = luck
                    if winner == 1:# possible outcome 1
                        print(win_with_luck[winner])# player dead
                        print('Mission over.')#Game ove
                    elif winner == 2:# possible outcome 2
                        print(win_with_luck[winner])#player dead
                        print('The bomb kills you and your fellow agents.')#display info who died
                        print('Mission over.')# Game over
                    else:#possible outcome 3
                        print(win_with_luck[winner])#Player finds the chips
                        print('To escape through the nearby exit door, you need to answer a final riddle.')#attemts to escape
                        final_q = input("Riddle: Built for a king, my body guards him in death, not in life. I stand tall, pointing to the skies, yet I am not alive. What am I: ")# Last puzzle
                        final_q = final_q.lower()
                        if final_q == 'pyramid':# answered right
                            print('\nYou escape with you fellow agents successfully as you answer the puzzle right!!!')# escapes
                            print('Mission Accomplished.')# win the game
                        else:# answered wrong
                            print('\nYour answer is wrong and the guards from the nuclear facility kill you.')# guards find the user and kill the player
                            print('Mission over.')#g Game over

                else:# answered the final riddle wong
                    print('The guards arrive because you guessed the riddle wrong and shoot you.')#Guards find the player and kill him/her
                    print('Mission over.')# Game over


        if choice1 == '2' or choice1 == 2: # Player is now in the agent's house
            print('\nYou are now in the entrance of the house of a famous agent of Russia. This house is surrounded by guards and you need to find the correct pass code to enter.\nRemember the code is a 1 digit number.') # description
            clue = int(input('Clue: I am an odd number. Take away a letter and I become even. What number am I: ')) # Riddle clue
            if clue == 7: # if riddle is answered right
                print('\nYou have entered the code successfully and fooled the guards, but you forgot one thing.') # User enters agent house
                print('Your 2 hrs timer is up....') # time out
                print('Mission over')


            else:# If riddle is answered wrong
                print("\nYou have answered the riddle wrong....., so the guards shoot you with their guns.")# user dies
                print("Mission Over.")#game over


    else: # Riddle wrong / Player died
        print('\nYou have answered it wrong and have triggered an alarm....')# Conclusion
        print("Russia's intelligence found you..... you and your fellow agents are killed instantly!!!")#User died
        print("Mission over.")# Game over


elif confirmation == 'no' or confirmation == 'No': # If user doesn't want to play the game
    print("\nGood luck with your life. Mission ended.") # prints goodbye


else:# Restart the game -> if the user answers random things
    print('\nError, you have not answered yes or no. Please restart the game to play again.') # instructs the user to restart the game


# Okay this game seems fun, let's try out and see how it works - clue: this game is impossible to win so try your best!!!!

