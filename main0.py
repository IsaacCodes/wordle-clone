#A Python Wordle Clone!
import random

#Returns colored (green, yellow, or red) string (using 256 colors)
def color(msg, type):
  if type == "green":
    #\003(esc)[38 (foreground);5 (placeholder);40 (color code)m (color func)
    return f"\033[38;5;40m{msg}\033[0;0m"
  if type == "yellow":
    #\003(esc)[38 (foreground);5 (placeholder);220 (color code) (color func)
    return f"\033[38;5;220m{msg}\033[0;0m"
  if type == "gray" or type == "grey":
    #\003(esc)[38 (foreground);5 (placeholder);246 (color code)m (color func)
    return f"\033[38;5;246m{msg}\033[0;0m"
  if type == "red":
    #\003(esc)[38 (foreground);5 (placeholder);196 (color code)m (color func)
    return f"\033[38;5;196m{msg}\033[0;0m"
  #If none of the above worked,
  return msg

  

#Startup messgaes/intructions
print("\nHello Wordle!\n")
print("Enter a 5 letter guess that will be color coded. You will have 6 attempts to get the right word.")
print("""
  Green  =  Letter in word & correct position
  Yellow =  Letter in word but incorrect position
  Gray   =  Letter not in word""")
print("-------------------------------\n\n")


#Creates guesses variables from the wordle-allowed-guesses.txt file
with open("wordle-allowed-guesses.txt") as f:
  guesses = f.read()
  guesses_l = guesses.split("\n")
#Creates answers variables from the wordle-answers.txt file
with open("wordle-answers.txt") as f:
  answers = f.read()
  answers_l = answers.split("\n")

#Keyboard printer, prints the keyboard
def keyboardPrint(keyboard, rounds):
  #Saving or updating mode
  row1 = " " + "".join(keyboard).split("a")[0]
  row2 = "  a" + "".join(keyboard).split("a")[1].split("z")[0]
  row3 = "     z" + "".join(keyboard).split("z")[1]

  if rounds == 0:
    print(f"\033[s{row1}\n{row2}\n{row3}\n")
  else:
    print(f"\033[u{row1}\n{row2}\n{row3}\n\033[{rounds}B")

  keyboardPrint(keyboard, rounds)


#The main game function
def main(start_pos):
  #A random answer from wordle-answers.txt
  answer = random.choice(answers_l)
  #Letters of alphabet, used for char testing
  letters = "abcdefghijklmnopqrstuvwxyz"
  #Used in error checking
  error = False
  #Variable for amount of rounds
  rounds = 0
  #Keyboard at the top of the screen which displays what letters have and havent been used
  keyboard = ["q  ", "w  ", "e  ", "r  ", "t  ", "y  ", "u  ", "i  ", "o  ", "p  ", "a  ", "s  ", "d  ","f  ", "g  ", "h  ", "j  ", "k  ", "l  ", "z  ", "x  ", "c  ","v  ", "b  ", "n  ", "m  "]  
  keyboardPrint(keyboard, rounds)
  

  #Updates (changes) the keyboard colors
  def keyboardUpdate(keyboard, letter, clr): 
    #n, clr = letter iterations through guess, color
    for x in range(len(keyboard)):
      
      contains = False
      if letter == "m":
        if letter == keyboard[x][0]:
          contains = True
        elif keyboard[x].count(letter) == 3:
          contains = True
      elif letter in keyboard[x]:
        contains = True

      #alr = already, 
      if clr == "green":
        if contains:
          keyboard[x] = f"{color(letter, 'green')}  "
          break
          
      elif clr == "yellow":
        if contains and "40" not in keyboard[x]:
          keyboard[x] = f"{color(letter, 'yellow')}  "
          break
          
      else: #clr == "gray"
        if contains and "40" not in keyboard[x] and "220" not in keyboard[x]:
          keyboard[x] = f"{color(letter, 'gray')}  "
          break

  
  rounds = 1
  while rounds <= 6:
    
    #Takes input
    guess = input("").lower()

    #Removes error message and invalid word after typing a new word
    recovery = False
    if error:
      error = False
      print("\033[1F\033[0K\r")
      print("\033[2F\033[0K\r")
      print("\033[2F\033[0K\r")
      recovery = True

    
    #Dev tool used to find the answer
    if guess == "[devpin]":
      print(f"\033[u\033[2FAnswer: '{answer}' (Dev Enabled)\033[{rounds+4}B")
      #For reasons unknown to me, when trying to clear a line using the previous print statement, nothing would happen.
      print("\033[0K\033[1F")
      continue

    #Checks for invalid characters
    invalid_char = False
    for char in guess:
      if char not in letters: 
        invalid_char = True

    #If non A-Z character is entered (Error)
    if invalid_char:
      error = True
      if recovery:
        print(f"\033[1F{guess}")
      print(color("Input can only contain letters (A-Z).", "red"))

    #If word isn't 5 chars (Error)
    elif len(guess) != 5:
      error = True
      if recovery:
        print(f"\033[1F{guess}")
      print(color("Guess must be 5 letters long.", "red"))

    #If guess is not in guesses or answers
    elif guess not in guesses and guess not in answers: 
      error = True
      if recovery:
        print(f"\033[1F{guess}")
      print(color("Guess must be a valid wordle word.", "red"))
      
    #If you guess the word
    elif guess == answer:
      print(f"\033[1F{color(answer, 'green')}")

      #Updates keyboard
      for letter in guess:
        keyboardUpdate(keyboard, letter, "green")
      
      #Keyboard printer
      keyboardPrint(keyboard, rounds)

      print("")
      if rounds == 1:
        print(f"Wow! You won in only 1 guess!")
      else:
        print(f"You won in {rounds} guesses!")
      return
      

    #If there are no errors, but you didnt guess the word
    else:
      #Letters correspond to how many times a letter in a guess has been set to green/yellow because that letter is in the answer
      alphabet = {
      "a" : 0, "b" : 0, "c" : 0, "d" : 0, "e" : 0, "f" : 0,
      "g" : 0, "h" : 0, "i" : 0, "j" : 0, "k" : 0, "l" : 0, 
      "m" : 0, "n" : 0, "o" : 0, "p" : 0, "q" : 0, "r" : 0,
      "s" : 0, "t" : 0, "u" : 0, "v" : 0, "w" : 0, "x" : 0,
      "y" : 0, "z" : 0
      }

      #Color coded results list (each item is a letter)
      result = ["", "", "", "", ""]

      #Loops through and matches green colors
      for n in range(0, 5):
        if guess[n] == answer[n]:
          result[n] = color(guess[n], "green")
          alphabet[guess[n]] += 1

          #Changes the keyboard colors
          keyboardUpdate(keyboard, guess[n], "green")

      #Loops through again, this time looking for yellow/gray
      for n in range(0, 5):
        #If there are less greens/yellows registered than letter count answer word and the old color isnt green, set color to yellow
        if alphabet[guess[n]] < answer.count(guess[n]) and "40" not in result[n]:
          result[n] = color(guess[n], "yellow")
          alphabet[guess[n]] += 1

          #Changes the keyboard colors
          keyboardUpdate(keyboard, guess[n], "yellow")

          
        #If there is not color set, and other color checks failed, set color to gray
        elif result[n] == "":
          result[n] = color(guess[n], "gray")
          
          #Changes the keyboard colors
          keyboardUpdate(keyboard, guess[n], "gray")

            
      #Prints the result
      result = "".join(result)
      #\033 (esc)[1(up 1 previous line)F (Cursor Previous Line func)
      print(f"\033[1F{result}")

      #Keyboard printer
      keyboardPrint(keyboard, rounds)

      #Goes onto the next guess
      rounds += 1

  #If all guesses have been unsucessfully attempted:
  print(f"You lost :(. The word was {answer}.")

  
#Runs the main loop and asks user if they want to play multiple again, if yes then restart, if not then shut down.
play_again = True
while play_again:
  main("\033[6n")
  answer = input("\nWould you like to play again (Y/N)? ")
  if answer == "yes" or answer == "y":
    print("Ok!\n\n")
  else:
    print("Ok, shutting down.")
    play_again = False