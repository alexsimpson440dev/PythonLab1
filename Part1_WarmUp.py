#imports random module
import random
#creates class Number that does nothing for practice
class Number():
    def __init__(self, num):
        self.num = int(num)

#variable that sets a random number to the number class
randomNumber = Number(random.randint(0, 10))

#input for the user to guess that number
userGuess = int(input("Guess a random number between 0 and 10: "))
#string to call if the number is not right
inputString = "You did not guess correctly! Guess again: "
#variable to set the number of guesses the user takes
numberOfGuesses = 1

#if the user is right it will print so with the number of guesses
if userGuess == randomNumber.num:
    print("Your guessed correctly!")
    print('Number of Guesses: ', numberOfGuesses)
#while loop if the user is wrong. will add to interval variable and find out if the user is too high or too low
#then allows user to guess again
while userGuess != randomNumber.num:
    numberOfGuesses += 1
    if userGuess > randomNumber.num:
        print("Too High")
    else:
        print("Too Low")
    userGuess = int(input(inputString))
#prints when the user gets it right and then the number of guesses it took
print("Your guessed correctly!")
print('Number of Guesses: ', numberOfGuesses)




