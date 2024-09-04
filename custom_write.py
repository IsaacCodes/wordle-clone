
console_line = 0

#Custom print which saves console lines
def cprint(*args, **kwargs):
  global console_line
  msg = []
  sep = " "
  #Gets separator
  for kwarg, val in kwargs.iteritems():
    if kwarg == "sep":
      sep = str(val)

  #Gets all string arguments
  for arg in args:
    msg.append(str(arg))
    msg.append(sep)

  #Prepares final message and tracks line count
  str_msg = "".join(msg)
  console_line += str_msg.count("\n") + 1

  print(str_msg)


def cinput(message: str):
  global console_line
  console_line += 1
  return input(message)


def move_cursor_to(pos: int):
  global console_line
  console_line = pos
  print("\033{pos}G")

def clear_below():
  print("\033[0J")