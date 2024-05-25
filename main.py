
import random
from replit import clear



def Game():
  print("Number Guessing Game")
  print("I'm thinking of a number between 1 and 100.")

  def guess_number(guess):
    if guess > secret_number:
      return "guess is higher"
    elif guess < secret_number:
      return "guess is lower"
    else:
      return "guess is correct"
  secret_number = random.randint(1, 100)
  
  difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if difficulty == "easy":
    attempts = 10
  elif difficulty == "hard":
    attempts = 5
  else:
    print("Invalid input.")
  
  while attempts > 0:
    print(f"You have {attempts} attempts remaing to guess the number.")
    guess = int(input("Make a guess: "))
    result = guess_number(guess)
    print(result)
    if result == "guess is correct":
      break
    attempts -= 1
  
  if attempts == 0:
    print("You've run out of guesses, you lose.")
  
  else:
    print(f"You got it! The answer was {secret_number}.")

Game()
while input("Do you want to play again? Type 'y' or 'n': ") == "y":
  clear()
  Game()
