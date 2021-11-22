# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 20:30:07 2021

@author: Dell


The Drinking Game 3.0

Added=>menu driven,activity addition possible, display activity list,bug fixes
"""

import random

names = []
actions = ["dances","sings","gets slapped by person to their right",
           "gets slapped by person to their left","massages the feet of person to right(3 min)",
           "massages feet of person to left(3 min)","kisses person to their right",
           "kisses person to their left","removes their t-shirt","does 50 push-ups",
           "does 50 squats","becomes a murga for 3 min","stands on one leg for 3 min EACH",
           "gets to slap person to their right","gets to slap person to their left",
           "gets to slap person straight forward","gets slapped by person straight forward",
           "has to jump 100 times","gets slapped by everyone","gets to slap everyone"]


def intro_module():

    print("\nWelcome to The Drinking Game by Prathamesh Kulkarni!\n"
          "Enter total number of people participating and then enter the names.\n"
          "The actions are already fed up in the system and I'll be choosing random person out of you and make you do a random action.\n"
          "The rules are fairly simple for you drunkards-\n"
          "Everone has to take a sip when any name is called.\n"
          "YOU HAVE TO DO WHAT I TELL YOU TO DO!\n"
          "Press Enter everytime to display new action\n")
    
    intro = input("Press Enter key to begin: ")
    if intro != '':
        intro = ''
    
    return intro
    
    
def input_module():
    num = input("\nEnter the number of drinkers: ") 
    if num.isnumeric() == False or num == '0':
        print("Please enter valid number you moron!")
        input_module()
    else:
        print("\nEnter your names below\n")
        for i in range(int(num)):
            temp = input("Drinker " + str(i+1) + ":")
            print()
            names.append(temp)

        
        
def game():
    name = random.choice(names)
    action = random.choice(actions)
    
    to_do = name + " drinks and " + action + "!"
    to_do = to_do.capitalize()
    
    print (to_do)
    
    
def start():
    input_module()
    loop = ''
    while loop == '':
        game()
        loop = input()
            
def add_action():
    new_action = input("\nEnter the activity you wish to add: ")
    actions.append(new_action)
        
    
def menu():
    if intro_module() == '':
        while True:
            print("\nBelow are your choices:")
            print("1.Start the Game\n2.Add an activity\n3.Show activities list\n4.Exit")
            
            choice = int(input("\nEnter your choice: "))
            if choice == None:
                continue
            if choice == 4:
                print("Adios Amigos!")
                break
            elif choice == 1:
                start()
            elif choice == 2:
                add_action()
            elif choice == 3:
                print()
                print(actions)
            else:
                print("Invalid choice you moron!")
        
        
if __name__ == '__main__':
    menu()
    
