#A Python Wordle Clone!
import random

import custom_write as cw
import keyboard as keyboard_py

#Startup Message
cw.cprint("""
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
  keyboard = keyboard_py.Keyboard()
  guess_log = ""

  round = 1
  while round <= 6:
    #Sets cursor pos, clears screen below, reprints
    cw.move_cursor_to(start_pos)
    cw.clear_below()
    cw.cprint(f"{keyboard}\n{guess_log}")

    guess = cw.cinput("").lower()
    guess_log += guess

    round += 1

  cw.cprint(keyboard)


#Calls main according to user
while True:
  main()

  break
  #start_pos = int("\033[6n".split("\x1b")[0].split(";")[0])
  #main(start_pos)
  answer = cw.cinput("\nWould you like to play again (Y/N)? ")

  if answer == "yes" or answer == "y":
    cw.cprint("Ok!\n\n")
  else:
    cw.cprint("Ok, shutting down.")
    break