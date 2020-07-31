import random

print ("Number Guessing game!!")

# random number between 1 and 9
number = random.randint(1, 9)
# number of chances given to the user
chances = 0
 # print(number)

# while loop to count the number of chances
while chances < 5 : 
    # enter a number between 1 and 9
   # print ("Guess a number between 1 and 9 : ")
    guess = int(input("Guess a number between 1 and 9 : "))
    print (number)
# compare the numbers
    if guess == number : 
# if the number is guessed correct then show this message
        print ("CONGRATULATIONS! You have guessed the correct number!!")
        break
    elif guess < number : 
        print ("You have guessed a number lower than the correct number. Please guess higher than ", guess)
    else : 
        print ("Your guess has exceeded the correct number. Please guess lower than ", guess)

# increase the value of chances by 1
chances += 1

# check if the user has guessed the correct number in the given chances.
if not chances < 5 : 
    print ("You LOSE!! The number is ", number)