# []==> this is an array
# name = [value1, value2, value3]
# an array is a special type of container that can hold multiple items
# arrays are indexed (their contentsare assigned a number)
# the index always starts at 0

# Import packages to extend Python (just like we exten Sublime, Atom, VSCode)
from random import randint
# re-import our game variables
from gameComponents import gameVars, winLose, comparisonConditional

while gameVars.player_choice is False: 
	print("=======================*/ RPS GAME */=========================")
	print("The Mighty One Lives:", gameVars.computer_lives, "/", gameVars.total_lives)
	print("Puny human Lives", gameVars.player_lives, "/", gameVars.total_lives)
	print("==============================================================")
	print("Come on, choose.. Don't waste my time! Or type 'quit' to be gone!\n")
	gameVars.player_choice = input("Choose rock, paper, or scissors: \n")

	if gameVars.player_choice == "quit":
		print("That's what I thougt!")
		exit()

	# this will be the AI choice -> a random pick from the choices array
	gameVars.computer_choice = gameVars.choices[randint(0, 2)]

	#player_choice now equals TRUE -> it has value

	comparisonConditional.comparisonConditional()

	print("puny human chose " + gameVars.player_choice)
	print("The Mighty One chose: " + gameVars.computer_choice)

	if gameVars.player_lives == 0:
		winLose.winorlose("lose")

	if gameVars.computer_lives == 0:
		winLose.winorlose("won") 

	print ("The Mighty One lives:", gameVars.player_lives)
	print ("puny human lives", gameVars.computer_lives)		

	# make thr loop keep running, by setting player_choice back to False
	# unset, so that our loop condition will evaluate to True
	gameVars.player_choice = False



# player_choice == False   ==(is)


	# Version 1, to explain array indexing
	#player_choice = choices[1]
	# it is the same thing ->player_choice = "paper"
	#print("index 1 in the choice array is " + player_choice + ", which is paper")

	

	












