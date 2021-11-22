# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 11:48:12 2021

@author: Dell

The Drinking Game 4.0

Added=> saving performed actions into text file, viewing the saved file,various bug fixes
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
          "The actions are already fed up in the system and I'll be choosing random person"
          " out of you and \nmake you do a random action.\n"
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
        print("\nPlease enter valid number you moron!")
        input_module()
    else:
        name_module(num)
        
def name_module(num):
    print("\nEnter your names below:\n")
    i=0
    for i in range(int(num)):
        temp = input("Drinker " + str(i+1) + ":")
        if temp.isalpha():
            print()
            names.append(temp)
            i=i+1
        else:                       #bug yet to be fixed
            print("Please enter valid name you moron!")
            names.clear()
            input_module()
                  
        
def game():
    name = random.choice(names)
    action = random.choice(actions)
    
    to_do = name + " drinks and " + action + "!"
    to_do = to_do.capitalize()
    
    print (to_do)
    writing_file(to_do)
    
    
    
def writing_file(to_do):
    f=open('Drinking Game Log.txt','a')
    f.write(''.join(to_do))
    f.write('\n')
    f.close()


def read_file():
    f = open('Drinking Game Log.txt','r')
    contents=f.read()
    print(contents)
    f.close()
    
def start():
    input_module()
    loop = ''
    while loop == '':
        game()
        loop = input()
    print("\nPerformed Game has been saved in 'Drinking Game Log.txt'! ")
            
def add_action():
    new_action = input("\nEnter the activity you wish to add: ")
    if new_action.isalpha() == False:
        print("\nThat's not an activity you moron!")
        add_action()
    else:
        actions.append(new_action)
        print("Activity successfully added!")
    
 
def menu():
    if intro_module() == '':
        while True:
            print("\nBelow are your choices:")
            print("1.Start the Game\n2.Add an activity\n3.Show activities list")
            print("4.Show Game Log\n5.Exit")
            
            choice = input("\nEnter your choice: ")
            if choice == None:
                continue
            if choice.isalpha():
                print("\nEnter a valid number you moron!")
            elif int(choice) == 5:
                print("\nAdios Amigos!")
                break
            elif int(choice) == 1:
                start()
            elif int(choice) == 2:
                add_action()
            elif int(choice) == 3:
                print()
                print(actions)
            elif int(choice) == 4:
                read_file()
            else:
                print("\nInvalid choice you moron!")
        
        
if __name__ == '__main__':
    menu()
    
