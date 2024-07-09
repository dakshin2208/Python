import random
target_value,guess_value=random.randint(1,10),0
while(target_value!=guess_value):
    guess_value=int(input("guess the number(1,10)"))

print("well guessed")
