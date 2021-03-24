# Import packages to extend Python (just like we exten Sublime, Atom, VSCode)
from random import randint

# []==> this is an array
# name = [value1, value2, value3]
# an array is a special type of container that can hold multiple items
# arrays are indexed (their contentsare assigned a number)
# the index always starts at 0
choices = ["rock", "paper", "scissors"]

player_lives = 3
computer_lives = 3
total_lives = 3

#True or false Boolean data types
#essentially, boolean are equivalent to a on or off switch, 1 or 0 
player_choice = False

#define a win or lose function
def winorlose(status):
	#version 1 of function
	#print("Inside winorlose function; status is:", status)
	print("You", status, "! Would you like to play again?")
	choice = input("Y / N? ")

	if choice == "N" or choice == "n":
		print("You chose to quit! Better luck next time!")
		exit() 
	elif choice == "Y" or choice == "y":
		#reset the player lives and computer lives
		# and reset player choice to False, so our loop restarts
		global player_lives
		global computer_lives
		global total_lives
		player_lives = total_lives
		computer_lives = total_lives
	else: 
		print("Make a valid choice -Y or N")
		#this might generate a bug that we need to fix later
		choice = input("Y /N")

# player_choice == False   ==(is)
while player_choice is False: 
	print("=======================*/ RPS GAME */=========================")
	print("Computer Lives:", computer_lives, "/", total_lives)
	print("Player Lives", player_lives, "/", total_lives)
	print("==============================================================")

	# Version 1, to explain array indexing
	#player_choice = choices[1]
	# it is the same thing ->player_choice = "paper"

	#print("index 1 in the choice array is " + player_choice + ", which is paper")

	player_choice = input("Choose rock, paper, or scissors: \n")
	#player_choice now equals TRUE -> it has value

	print("user chose " + player_choice)

	# this will be the AI choice -> a random pick from the choices array
	computer_choice = choices[randint(0, 2)]

	print("computer chose: " + computer_choice)

	# 'if' is a conditional 
	#() is not necessary with if
	# = sets the value
	# == compares values
	# you go in when using if (indenting) Indented elements are connected to the conditional

	if computer_choice == player_choice:
		print("tie")

	#elif->else if
	elif computer_choice == "rock":
		if player_choice == "scissors":
			print("you lose!")
			#long way
			#player_lives = player_lives -1

			#simple way
			player_lives -= 1

		else:
			print("you win!")
			computer_lives -= 1

	elif computer_choice == "paper":
		if player_choice == "scissors":
			print("you lose!")
			player_lives -= 1
		else:
			print("you win!")
			computer_lives-= 1

	elif computer_choice == "scissors":
		if player_choice == "paper":
			print("you lose!")
			player_lives -= 1
		else:
			print("you win!")
			computer_lives -= 1

	if player_lives == 0:
		winorlose("lose")

	if computer_lives == 0:
		winorlose("won") 

	print ("Player lives:", player_lives)
	print ("Computer lives", computer_lives)		

	# make thr loop keep running, by setting player_choice back to False
	# unset, so that our loop condition will evaluate to True
	player_choice = False







