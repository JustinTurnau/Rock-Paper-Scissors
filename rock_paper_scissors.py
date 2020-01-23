# AI randomization source
import random

# Choices list for AI
choices = ['rock', 'paper', 'scissors']

# global
game_is_running = True

while True:
	
	#User puts in their selection here
	user_input = input("rock, paper, or scissors? ")
	
	# Only accepts correct inputs
	while user_input not in ["r", "p", "s", "rock", "paper", "scissors"]:
		user_input = input("Invalid input. Please type rock, paper, or scissors: ")
	
	# Handles use of r, p, or s inputs
	if user_input == "r":
		user_input = 'rock'
	if user_input == "p":
		user_input = 'paper'
	if user_input == "s":
		user_input = 'scissors'
	
	# AI randomization
	AI_choice = choices[random.randint(0, 2)]
	print("Your nemesis has selected: " + AI_choice)

	# Main game function
	def play_game():
		
		global game_is_running
		
		# While round is still in progress
		while game_is_running:
		
		# Check for winner
			check_winner()
			
			# Otherwise it was a tie
			if user_input == AI_choice:
				tie()

			return


	#Function that runs through all scenarios and decides who won
	def check_winner():

		check_user_win()

		check_if_AI_won()

		return
		
		
	# Function to check if user won
	def check_user_win():
		
		if 'rock' in user_input and AI_choice == "scissors":
			user_wins()
		elif 'scissors' in user_input and AI_choice == "paper":
			user_wins()
		elif 'paper' in user_input and AI_choice == "rock":
			user_wins()
			return

	# Function to check for AI victory
	def check_if_AI_won():
		if 'rock' in user_input and AI_choice == "paper":
			user_loses()
		elif 'scissors' in user_input and AI_choice == "rock":
			user_loses()
		elif 'paper' in user_input and AI_choice == "scissors":
			user_loses()
			
			return


	# Function that handles user victory
	def user_wins():
		print("You win! ")
		return

	# Function that handles user loss
	def user_loses():	
		print("You lose.")
		return

	# Function that handles tie
	def tie():
		print("Tie.")
		return
		

	# Run the main game function
	play_game()

