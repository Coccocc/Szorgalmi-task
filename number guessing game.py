# Author: Hegyi Dáneil 
# Neptune code: CJC6AN
# Email: rekellemail5@gmail.com
# Created: 2023-10-26
# Last Modified: 2023-10-26




import random
count = 0

def random_number_game(count):
    random_number = random.randrange(1, 100 + 1)


    while True:
        guesseed_number = int(input("Guess the number in the range of 1 - 100: "))
      
      
          
        if guesseed_number > 100 or guesseed_number < 0:
          print("Number has to be between 1 and 100")
          return random_number_game(count)  
        
        imaginary_number = guesseed_number
        

        if imaginary_number == random_number:
        
         count += 1

        
         print(f"Correct! The number was {random_number}")
         print(f"You had guessed {count} times")
         move = input("Do you want to continue? Y/N: ")
         if move == "Y":
           return random_number_game(count)
         elif move == "N":
           print("Hope you had fun! ")
           break
        
        elif imaginary_number > random_number:
         print(f" {imaginary_number} is too big. Try a smaller one")
         count += 1
        
        elif imaginary_number < random_number:
         print(f" {imaginary_number} is too small. Try a bigger one")
         count += 1

    
random_number_game(count)