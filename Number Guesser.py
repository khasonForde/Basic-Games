from random import randint
print("Would you like to play Number Guesser?")
PlayerWantsToPlay = str(input())
while PlayerWantsToPlay == "yes":
  NumberGenerated = randint(0,5)
  print("Please guess a number in the range of 0 to 5")
  try:
    PlayerGuess = int(input())
  except ValueError:
    print("You did not enter a number.")
    break
  if PlayerGuess == NumberGenerated:
    print(f"The number to be guessed was {NumberGenerated} and your number was {PlayerGuess}.")
    print("Your guess was correct! You win :)")
    print("Would you like to play Number Guesser again?")
    PlayerWantsToPlay = str(input())
  elif PlayerGuess != NumberGenerated and PlayerGuess >= 0 and PlayerGuess <= 5:
    print(f"The number to be guessed was {NumberGenerated} and your number was {PlayerGuess}.")
    print("Your guess was incorrect. Sorry you lose :(")
    print("Would you like to play Number Guesser again?")
    PlayerWantsToPlay = str(input())
  elif (PlayerGuess < 0) or (PlayerGuess > 5):
    print("Your guess was an invalid number.")
else:
  print("Have a nice day/night!")
