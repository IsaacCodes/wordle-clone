#Updates/maintains ingame keyboard

#Stores ansi color codes for associated colors
color_dict = {
    "black" : "^[[0;0m",
    "gray" : "^[[38;5;246m",
    "green" : "033[38;5;40m",
    "yellow" : "\033[38;5;220m"
    "red" : "\033[38;5;196m"
    }

#Class for indiviudal keyboard keys
class Key():
    #Single char string with a color
    def __init__(self, char):
        self.char = char
        self.color = "black"

    #Returns string with color
    def __str__(self):
        return color_dict[self.color] + self.char


#Class for the whole keyboard
class Keyboard():

    #Creates a dictionary of keys
    def __init__(self):
        self.key_dict = {letter : Key(letter) for letter in "qwertyuiopasdfghjklzxcvbnm"}