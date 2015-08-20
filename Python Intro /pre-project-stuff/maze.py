"""This is a-maze-ing Maze. You start it by calling the main function.
Exiting the program is always an option with 'exit'."""

def main():
   print("Welcome to the A-Maze-ing Maze! I dare you to escape!")

   currentRoom = room0()

   while currentRoom != exit:
      currentRoom = currentRoom()

   currentRoom()


# description: A description of the current room
# doors: dictionary with door:location sets
def process_user_movement(description, doors):
   """This is the process_user_movement function that will
      handle a user's input.
   """
   # Print the description of the current room
   print(description)

   # Print the available doors
   print("You see doors to the ", end="")
   print(*list(doors.keys()), sep=", ")

   # Prompt the for what doors they want
   choice = ""

   # Do things based on their response
   while choice.lower() != "exit":
      choice = input("Which way you would like to go? >> ")

      # Valid response: Go to the correct location
      if choice.lower() in doors:
         return doors[choice.lower()]
      elif choice.lower() == "exit":
         print("Too tough for you, eh? Good-bye, then.")
         return exit
      # Invalid response: Ask them again
      else:
         print("I'm sorry, I didn't understand.")


def room0():
   # description
   description = "This room is very small. You barely fit here. You're like Alice in that crazy-tiny-room thing."
   # doors
   # where those doors Go
   doors = {"east":room1, "south":room3}

   return process_user_movement(description, doors)

def room1():
   # description
   description = "This room is HUGE, but there are tiny doors on all sides."
   # doors
   # where those doors Go
   doors = {"east":room1, "south":room3,"west":room2, "north":room4, "up":ceiling, "down":basement}

   return process_user_movement(description, doors)

def room2():
   pass

def room3():
   pass

def room4():
   pass

def ceiling():
   description = "You find yourself in an attic. There are spiders EVERYWHERE. It's impressive, really. What do they eat?"
   doors = {"down":room1}
   return process_user_movement(description,doors)

def basement():
   print("You've stumbled into the crypt of the maze. There are skeletons here. You're about to come on. WHAHAHAHAHA")


if __name__ == '__main__':
   main()

