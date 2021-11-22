# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 20:30:07 2021

@author: Dell


The Drinking Game 2.0

Added=> standalone program with classes
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
    intro = ''

    print("\nWelcome to The Drinking Game by Prathamesh Kulkarni!\n"
          "Enter total number of people participating and then enter the names.\n"
          "The actions are already fed up in the system and I'll be choosing random person"
          " out of you and \nmake you do a random action.\n"
          "The rules are fairly simple for you drunkards-\n"
          "Everone has to take a sip when any name is called.\n"
          "YOU HAVE TO DO WHAT I TELL YOU TO DO!\n"
          "Press Enter everytime to display new action\n")
    
    intro = input("Press Enter to start the game: ")
    
    return intro
    
    
def input_module():
    num = int(input("\nEnter the number of drinkers: "))    
    print("\nEnter your names below\n")
    for i in range(num):
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
    if intro_module() == '':
        input_module()
        loop = ''
        while loop == '':
            game()
            loop = input()
            
  
        
        
if __name__ == '__main__':
    start()