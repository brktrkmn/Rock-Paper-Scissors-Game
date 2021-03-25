# []==> this is an array
# name = [value1, value2, value3]
# an array is a special type of container that can hold multiple items
# arrays are indexed (their contentsare assigned a number)
# the index always starts at 0

# Import packages to extend Python (just like we exten Sublime, Atom, VSCode)
from random import randint
# re-import our game variables
from gameComponents import gameVars

# define a win / lose function and refer to it (invoke it) in your game loop
def winorlose(status):
	if status == "won":
		pre_message = "You are the huuugest winner ever! "
	else:
		pre_message = "You done trumped it, loser! "

	print(pre_message + 'Would you like to play again?')

	choice = False

	while choice == False:
		choice = input("Y / N? ")

		if choice == "Y" or choice == "y":
			#reset the game loop and start over again
			gameVars.player_lives = gameVars.total_lives
			gameVars.computer_lives = gameVars.total_lives
		elif choice == "N" or choice == "n":
			#exit message and quit
			print("You chose to quit! Better luck next time!")
			exit() 
		else: 
			print("Make a valid choice - Y or N")
			choice = False

while gameVars.player_choice is False: 
	print("=======================*/ RPS GAME */=========================")
	print("Computer Lives:", gameVars.computer_lives, "/", gameVars.total_lives)
	print("Player Lives", gameVars.player_lives, "/", gameVars.total_lives)
	print("==============================================================")
	print("Choose your weapon! Or type quit to exit\n")
	gameVars.player_choice = input("Choose rock, paper, or scissors: \n")

	if gameVars.player_choice == "quit":
		print("You chose to quit")
		exit()

	# this will be the AI choice -> a random pick from the choices array
	gameVars.computer_choice = gameVars.choices[randint(0, 2)]

	#player_choice now equals TRUE -> it has value

	print("user chose " + gameVars.player_choice)
	print("computer chose: " + gameVars.computer_choice)

	# 'if' is a conditional 
	#() is not necessary with if
	# = sets the value
	# == compares values
	# you go in when using if (indenting) Indented elements are connected to the conditional

	if gameVars.computer_choice == gameVars.player_choice:
		print("tie")

	#elif->else if
	elif gameVars.computer_choice == "rock":
		if gameVars.player_choice == "scissors":
			print("you lose!")
			#long way
			#player_lives = player_lives -1

			#simple way
			gameVars.player_lives -= 1

		else:
			print("you win!")
			gameVars.computer_lives -= 1

	elif gameVars.computer_choice == "paper":
		if gameVars.player_choice == "scissors":
			print("you lose!")
			gameVars.player_lives -= 1
		else:
			print("you win!")
			gameVars.computer_lives-= 1

	elif gameVars.computer_choice == "scissors":
		if gameVars.player_choice == "paper":
			print("you lose!")
			gameVars.player_lives -= 1
		else:
			print("you win!")
			gameVars.computer_lives -= 1

	if gameVars.player_lives == 0:
		winorlose("lose")

	if gameVars.computer_lives == 0:
		winorlose("won") 

	print ("Player lives:", gameVars.player_lives)
	print ("Computer lives", gameVars.computer_lives)		

	# make thr loop keep running, by setting player_choice back to False
	# unset, so that our loop condition will evaluate to True
	gameVars.player_choice = False



# player_choice == False   ==(is)


	# Version 1, to explain array indexing
	#player_choice = choices[1]
	# it is the same thing ->player_choice = "paper"
	#print("index 1 in the choice array is " + player_choice + ", which is paper")

	

	












