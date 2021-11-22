# -*- coding: utf-8 -*-
"""
Created on Sat Jul 17 12:23:21 2021

@author: Dell

The Drinking Game 5.0

Added=> removing activity,asking whether to save or not,menu entry to delete game log,
        bug fixes
"""


import random
import os


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
        print("\nPlease enter valid number you moron!")
        input_module()
    else:
        name_module(num)

        
def name_module(num):
    print("\nEnter your names below:\n")
    i=0
    for i in range(int(num)):
        temp = input("Drinker " + str(i+1) + ":")
        temp=temp.strip()
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
    if os.path.exists("Drinking Game Log.txt"):
        f = open('Drinking Game Log.txt','r')
        contents=f.read()
        print(contents)
        f.close()
    else:
        print("\nGame Log doesn't exist!")

    
def start():
    input_module()
    loop = ''
    while loop == '':
        game()
        loop = input()
    print("\nPerformed Game has been saved in 'Drinking Game Log.txt'! ")
    save_module()
 
           
def add_action():
    new_action = input("\nEnter the activity you wish to add: ")
    if new_action.isalpha() == False:
        print("\nThat's not an activity you moron!")
        add_action()
    else:
        actions.append(new_action.lower())
        print("Activity added successfully!")
        

def remove_action():
    del_action = input("\nEnter the activity you wish to delete: ")
    del_action = del_action.lower()
    if del_action in actions:
        actions.remove(del_action)
        print("Activity removed successfully!")
    else:
        print("\nThis activity doesn't exist you moron!")


def save_module():
    ask = input("Do you want to delete the saved Game Log? (y/n) : ")        
    if ask.lower().strip() == 'y':
        if os.path.exists("Drinking Game Log.txt"):
            os.remove("Drinking Game Log.txt")
            print("\nGame Log deleted successfully!")
        else:
            print("\nThe file does not exist!")
    elif ask.lower().strip() == 'n':
        print("\nNo changes made to the Game Log!")
    else:
        print("\nWhat are you entering you moron!")
        save_module()
        
def menu():
    if intro_module() == '':
        while True:
            print("\nBelow are your choices:")
            print("1.Start the Game\n2.Show activities list\n3.Add an activity")
            print("4.Remove an activity\n5.Show Game Log\n6.Delete Game Log")
            print("7.Exit")
            
            choice = input("\nEnter your choice: ")
            choice=choice.strip()
            if choice == None:
                continue
            if choice.isalpha():
                print("\nEnter a valid number you moron!")
            elif int(choice) == 7:
                print("\nAdios Amigos!")
                break
            elif int(choice) == 1:
                start()
            elif int(choice) == 2:
                print()
                print(actions)
            elif int(choice) == 3:
                add_action()
            elif int(choice) == 4:
                print()
                print(actions)
                remove_action()
            elif int(choice) == 5:
                read_file()
            elif int(choice) == 6:
                save_module()
            else:
                print("\nInvalid choice you moron!")
        
        
if __name__ == '__main__':
    menu()
    
