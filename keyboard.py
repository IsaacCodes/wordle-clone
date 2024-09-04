#Updates/maintains ingame keyboard

#Stores ansi color codes for associated colors
color_dict = {
    "default" : "\x1b[0;0m",
    "gray" : "\x1b[38;5;246m",
    "green" : "\x1b[38;5;40m",
    "yellow" : "\x1b[38;5;220m",
    "red" : "\x1b[38;5;196m"
    }

#Class for indiviudal keyboard keys
class Key():
    #Single char string with a color
    def __init__(self, char):
        self.char = char
        self.color = "default"

    #Returns string with color
    def __str__(self):
        return color_dict[self.color] + self.char


#Class for the whole keyboard
class Keyboard():

    #Creates a dictionary of keys
    def __init__(self):
        self.key_dict = {letter : Key(letter) for letter in "qwertyuiopasdfghjklzxcvbnm"}

    #Returns a string formatted Keyboard
    def __str__(self):
        row1 = " "*1 + "  ".join([str(key) for key in self.key_dict.values()][:10])
        row2 = " "*2 + "  ".join([str(key) for key in self.key_dict.values()][11:19])
        row3 = " "*5 + "  ".join([str(key) for key in self.key_dict.values()][20:])

        return f"{row1}\n{row2}\n{row3}"