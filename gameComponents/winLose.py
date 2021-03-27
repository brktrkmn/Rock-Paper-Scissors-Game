from gameComponents import gameVars

# define a win / lose function and refer to it (invoke it) in your game loop
def winorlose(status):
	if status == "won":
		pre_message = "You didn't deserve to win!! "
	else:
		pre_message = "Don't waste my time,LOSER! "

	print(pre_message + 'Dare to to play and lose again?')

	choice = False

	while choice == False:
		choice = input("Y / N? ")

		if choice == "Y" or choice == "y":
			#reset the game loop and start over again
			gameVars.player_lives = gameVars.total_lives
			gameVars.computer_lives = gameVars.total_lives
		elif choice == "N" or choice == "n":
			#exit message and quit
			print("That's what I thought.. Beat it!")
			exit() 
		else: 
			print("You are not very bright, are you? Just type Y or N")
			choice = False