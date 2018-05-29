import random

Guesses = 0
num = random.randint(1,1000)		#Sets the range for the computer to make the randnum.

name = input("Hello! What is your name?: ")

print ("Hello " + name + ". You have 8 guesses to guess my number between 1 and 1000. Good luck!")

while Guesses < 8:				#Sets guess to a num of choice.
	guess = input("Take a guess: ")
	guess = int(guess)

	Guesses = Guesses + 1 		#Increases guesses the next subtracts guesses from guessesleft
	guessesleft = 8 - Guesses	#So that you can know how many guesses you have

	if guess < num:
		guessesleft = str(guessesleft)						#Prints if your guess was too low and the number of guesses left
		print ("Your guess was too low you have " + guessesleft + " guesses left.")

	if guess > num:
		guessesleft = str(guessesleft)						#Prints if your guess was too high and the number of guesses left
		print ("Your guess was too high you have " + guessesleft + " guesses left.")

	if guess == num:			#If the guess is correct it breaks and continues forward.
		break

if guess != num:		#After either all guesses or a break it will asses this if true that means you ran out of guesses
		print ("You have failed! I was thinking of the number " + str(num) + ".")

if guess == num:		#If this is true it means you got the question right.
	print ("Congratulations! The number " + str(num) + " is correct!")



