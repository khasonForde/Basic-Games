from random import randint

def DiceRoll():
  DiceRoll= randint(1,6)
  print(f"Your dice roll is {DiceRoll}.")


def DoubleRoll():
  print("Enter the keyword \"roll\" to roll the dice")
  playerInput1 = input()
  if playerInput1 == "roll":
    DiceRoll1 = randint(1,6)
    print(f"Your first dice roll is {DiceRoll1}.")
  else:
    while playerInput1 != "roll":
      print("Invalid Input. please enter the keyword \"roll\" to roll the dice.")
      playerInput1 = input()
      if playerInput1 == "roll":
        DiceRoll1 = randint(1,6)
        print(f"Your first dice roll is {DiceRoll1}.")
  print("Enter the keyword \"roll\" to roll the dice")
  playerInput2 = input()
  if playerInput2 == "roll":
    DiceRoll2 = randint(1,6)
    print(f"Your dice roll is {DiceRoll2}.")
  else:
      while playerInput2 != "roll":
        print("Invalid Input. please enter the keyword \"roll\" to roll the dice.")
        playerInput2 = input()
        if playerInput2 == "roll":
          DiceRoll2 = randint(1,6)
          print(f"Your first dice roll is {DiceRoll1}.")
  if DiceRoll1 == DiceRoll2:
    print(f"Your dice rolls matched! You win :)")
  else:
    print("Your dice rolls did not match. You lose :(")

print ("Would you like to play the dice rolling simulator?")
PlayerWantsToPlay = input()
while PlayerWantsToPlay == "yes":
  print("Select 1 to play the dice rolling simulator or select 2 to play the double dice rolling simulator.")
  playerSelection = input()
  if playerSelection == "1":
    DiceRoll()
    print("Would you like to play again?")
    PlayerWantsToPlay = input()
  elif playerSelection == "2":
    DoubleRoll()
    print("Would you like to play again?")
    PlayerWantsToPlay = input()
else:
  print("Have a nice day/night!")