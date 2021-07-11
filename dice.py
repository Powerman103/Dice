from random import randint

score = 0

i = 0
while i < 25:
    i += 1
    dice_number = randint(1,6)
    number_chosen = int(input("Which number from 1-6 will you guess?"))

    if dice_number == number_chosen:
        print("Good job guessing it right!")
        score += 5
        
    else:
        print("The dice number was", dice_number, "you imbicile")
        


print("Good job on your score of", score, "!")




 

        
        
