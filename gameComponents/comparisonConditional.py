from gameComponents import gameVars
	# 'if' is a conditional 
	#() is not necessary with if
	# = sets the value
	# == compares values
	# you go in when using if (indenting) Indented elements are connected to the conditional
def comparisonConditional():

	if gameVars.computer_choice == gameVars.player_choice:
			print("                                         ")
			print("                   //////////////////////")
			print("                   #                    #")
			print("                   #       T-I-E !      #")
			print("                   #                    #")
			print("                   //////////////////////")
			print("                                         ")

	#elif->else if
	elif gameVars.computer_choice == "rock":
		if gameVars.player_choice == "scissors":
			print("                                         ")
			print("                   //////////////////////")
			print("                   #                    #")
			print("                   #  Y-O-U  L-O-S-E !  #")
			print("                   #                    #")
			print("                   //////////////////////")
			print("                                         ")
			#long way
			#player_lives = player_lives -1

			#simple way
			gameVars.player_lives -= 1

		else:
			print("                                         ")
			print("                   //////////////////////")
			print("                   #                    #")
			print("                   #    Y-O-U  W-I-N !  #")
			print("                   #                    #")
			print("                   //////////////////////")
			print("                                         ")
			gameVars.computer_lives -= 1

	elif gameVars.computer_choice == "paper":
		if gameVars.player_choice == "scissors":
			print("                                         ")
			print("                   //////////////////////")
			print("                   #                    #")
			print("                   #  Y-O-U  L-O-S-E !  #")
			print("                   #                    #")
			print("                   //////////////////////")
			print("                                         ")
			gameVars.player_lives -= 1
		else:
			print("                                         ")
			print("                   //////////////////////")
			print("                   #                    #")
			print("                   #    Y-O-U  W-I-N !  #")
			print("                   #                    #")
			print("                   //////////////////////")
			print("                                         ")
			gameVars.computer_lives-= 1

	elif gameVars.computer_choice == "scissors":
		if gameVars.player_choice == "paper":
			print("                                         ")
			print("                   //////////////////////")
			print("                   #                    #")
			print("                   #  Y-O-U  L-O-S-E !  #")
			print("                   #                    #")
			print("                   //////////////////////")
			print("                                         ")
			gameVars.player_lives -= 1
		else:
			print("                                         ")
			print("                   //////////////////////")
			print("                   #                    #")
			print("                   #    Y-O-U  W-I-N !  #")
			print("                   #                    #")
			print("                   //////////////////////")
			print("                                         ")
			gameVars.computer_lives -= 1