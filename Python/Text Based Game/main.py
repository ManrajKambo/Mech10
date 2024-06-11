# Jan 7, 2020
# Clear command
clear = "\n" * 100
# Gets the server time for the time.sleep(3) command
import time
# Generated random number between 1 and 400000
from random import randrange, uniform
Answer = randrange(1, 400000)
# Main Loop started
while True:
# Internal loop so if player presses N it just restarts the loop till they press Y
  while True:
    print(clear)
    # Player woke up
    print("You are locked inside a room and you need to get out")
    print()
# Player asked to continue
    import click
    if click.confirm("Start Game?", default=True):
      break
# Internal loop so if player presses N it just restarts the loop till they press Y
  while True:
    print(clear)
    print("You just woke up")
    print()
# Player asked to get up
    import click
    if click.confirm("Get Up?", default=True):
        break
# Internal loop so if player presses N it just restarts the loop till they press Y
  while True:
    print(clear)
# Prints random number of trees ouside the window and tells the player
    print("You see a window and there are" ,Answer, "trees outside")
    print()
    print("(HINT: You may want to remember that)")
    print()
# Player asked to look around
    import click
    if click.confirm("Look around?", default=True):
      break
# Internal loop so if player presses N it just restarts the loop till they press Y
  while True:
    print(clear)
    print("There is door")
    print()
# Player asked to open door
    import click
    if click.confirm("Open door?", default=True):
      print(clear)
# Player is told that the door is locked
      print("Door is locked")
    break
# Internal loop so if player presses N it just restarts the loop till they press Y
  while True:
    print(clear)
    print()
# Player asked to loor around
    import click
    if click.confirm("Look around?", default=True): 
      break
# Internal loop so if player presses N it just restarts the loop till they press Y
  while True:
    print(clear)
    print("Look there is a box")
    print()
# Player asked to open the box
    if click.confirm("Open box?", default=True): 
      break
# Internal loop so if player presses N it just restarts the loop till they press Y
  while True:
    print(clear)
# Asks player to enter the random generated of ammounts of trees they saw outside the window
    print("Box: How many trees were there outside")
# Player inputs the answer
    Guess = input("What is the answer? ")
# If incorrect player cant continue
    while(int(Guess)!= Answer):
      if(int(Guess) < Answer):
        print(clear)
        print("CONFIRMING...")
        time.sleep(3)
        print("Incorrect")
      else:
        print(clear)
        print("CONFIRMING...")
        time.sleep(3)
        print("Incorrect")
      Guess = input("What is the answer? ")
    import click
    break
# If correct player can continue
  print(clear)
  print("CONFIRMING...")
  time.sleep(3)
  print("Correct")
  time.sleep(3)
# Internal loop so if player presses N it just restarts the loop till they press Y
  while True:
    print(clear)
    print("You just got a key to open up the door")
    print()
# Player asked to go to the door
    import click
    if click.confirm("Go to door?", default=True):
      break
# Internal loop so if player presses N it just restarts the loop till they press Y
  while True:
    print(clear)
# Player asked to open the door
    import click
    if click.confirm("Open door?", default=True):
      break
# Internal loop so if player presses N it just restarts the loop till they press Y
  while True:
    print(clear)
    import click
# Player asked to walk outside
    if click.confirm("Walk outside?", default=True):
      break
# Success message
  print(clear)
  print("SUCCESS YOU FINALLY MADE IT OUT!!!")
# Player asked if they want to play again
  print()
  import click
  if click.confirm("Play Again? ", default=True):
# If YES the game restarts
    print("Restarting...")
    time.sleep(3)
    continue
    print(clear)
# If NO the game is done
  else:
    print(clear)
# Loop is ended
  break
# Thanks messge
print(clear)
print("DONE")
print("Thanks for playing ;)")
print()