import random

level_hard = 5
level_easy = 10 


def random_number_generator():
  return random.randint(1,101)
  


def start_game():
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  difficulty = input("Choose a difficulty. Type 'easy or 'hard': ")
  if difficulty == "easy":
    easy_game(random_number_generator())
  elif difficulty == "hard":
    hard_game(random_number_generator())
    
  

def easy_game(easy_rand_number):
    global level_easy
    while level_easy > 0:
      print(f"You have {level_easy} attempts remaining to guess the number.")
      guess = int(input("Make a guess: "))
      if guess == easy_rand_number:
        print(f"You won. The guess was {easy_rand_number}")
        break
      elif guess > easy_rand_number:
        level_easy -=1
        print("Guess is too high")
      elif guess < easy_rand_number:
        level_easy -=1
        print("Guess is too low")
      elif level_easy ==0:
        print( "Game over you ran out of lives!")

def hard_game(hard_rand_number):
  global level_hard
  print(hard_rand_number)
  while level_hard != 0:
    print(f"You have {level_hard} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess == hard_rand_number:
      print(f"You won! The answer was {hard_rand_number}")
      break
    elif guess > hard_rand_number:
      level_hard -=1
      print("Guess is too high")
    elif guess < hard_rand_number:
      level_hard -=1
      print("Guess is too low")
    elif level_hard ==0:
       print("Game over you ran out of lives!")




start_game()
