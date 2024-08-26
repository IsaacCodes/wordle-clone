#A Python Wordle Clone!
import random

import keyboard as _keyboard

#Startup Message
print("""
Enter a 5 letter guess that will be color coded. You will have 6 attempts to get the right word.

Gray   =  Letter not in word
Yellow =  Letter in word but incorrect position
Green  =  Letter in word and correct position
-----------------------------------------------\n\n""")

#Create word lists from their respective files
with open("wordle-allowed-guesses.txt") as f:
  guesses = f.read().split("\n")
#Creates answers variables from the wordle-answers.txt file
with open("wordle-answers.txt") as f:
  answers = f.read().split("\n")

#Main game loop
def main(start_pos):
  #A random answer from wordle-answers.txt
  answer = random.choice(answers)
  #Letters of alphabet, used for char testing
  alphabet = "abcdefghijklmnopqrstuvwxyz"
  
  #Game keyboard
  keyboard = _keyboard.Keyboard()

  rounds = 1
  while rounds <= 6:
    pass

  print(keyboard)


#Calls main according to user
while True:
  main("\033[6n") #ANSI code gets current console pos
  answer = input("\nWould you like to play again (Y/N)? ")

  if answer == "yes" or answer == "y":
    print("Ok!\n\n")
  else:
    print("Ok, shutting down.")
    break