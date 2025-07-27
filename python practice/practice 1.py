# import random
# from re import match

# secret_number = random.randint(1, 10)

    
# while secret_number:      
        
#         guess = int(input("Guess a number between 1 and 10: "))

#         match guess:     
                        
#             case _ if guess == secret_number:
#                 print("Congratulations! You guessed it!")
#                 break 
#             case _ if guess < secret_number:
#                 print("Nope, your guess is a bit low. Give it another shot!")
#             case _ if guess > secret_number:
#                 print("Oops, your guess is a bit high")
#             case _:
#                 print("Invalid input, please enter a number between 1 and 10")  
                           
# play_again = input("Do you want to play again? (yes/no): ").lower()
# if play_again not in ("yes", "y"):
#     print("Thanks for playing")

rows = 5

for i in range(1, rows + 1):
  # Outer loop controls the number of rows
  for j in range(1, i + 1):
    # Inner loop prints asterisks for each row
    print("*", end="")
  print()     