# Random password generator
# code 100% written by me
# My social media:
# x.com/ismatronics
# github.com/ismatronics
# instagram.com/ismatronics
# youtube.com/@ismatronics

print("Code written by ismatronics")
print("")

# import is used to import the random library
import random

# in the instruction below we declare a variable called character where all the possible characters are stored
character = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "!", "#", "$", "%", "&", "(", ")", "*", "+"]

# in the instruction below we ask the user how many characters he wants in his password
print("How many characters do you want in your password? ")
print(" ")

# in the instruction below we declare a variable called number where the user will input the number of characters he wants in his password
number = int(input())
# in the instruction below we use an if statement to check if the user has entered a valid number
if number < 6:
    print("You can't have a password with less than 6 characters")
elif number > 50:
    print("You can't have a password with more than 50 characters")
else:
    print("Your password is: ")
    # in the instruction below we use a for loop to generate a random password
    for i in range(number):
        print(character[random.randint(1, 71)], end="")