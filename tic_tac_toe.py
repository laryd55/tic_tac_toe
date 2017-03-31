__author__ = 'Hillary'
def display_board(board):
	print('+---+---+----+')
	print('|   |   |    |')
	print('| '+board[7]+' | '+board[8]+' | '+board[9]+'  |')
	print('|   '+'|   |    |')
	print('+---+---+----+')
	print('|   |   |    |')
	print('| '+board[4]+' | '+board[5]+' | '+board[6]+'  |')
	print('|   '+'|   |    |')
	print('+---+---+----+')
	print('|   |   |    |')
	print('| '+board[1]+' | '+board[2]+' | '+board[3]+'  |')
	print('|   '+'|   |    |')
	print('+---+---+----+')
def mark_choice():
	marker=''
	while not (marker == 'O' or marker == 'X'):
		marker=input('Please choose O or X to start the game!> ').upper()
		if marker == 'X':
			 return 'X','O'
		elif marker=='O':
			return 'O','X'
def place_marker(board, marker, pos):
	board[pos] = marker
def player_pos(board):
	pos = ' '
	while pos not in '1 2 3 4 5 6 7 8 9'.split() or not space_check(board, int(pos)):
		pos = input('Choose your next position: (1-9) ')

	return int(pos)
def player_name():
	global player1
	global player2
	player1= input('Player 1 please enter your name: ')
	player2= input('Player 2 please enter your name: ')
def player_choice():
	global player1
	global player2
	import random
	if random.randint(0,1)== 0:
		return player1
	else:
		return player2

def win_check(board,mark):
	return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
	(board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
	(board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
	(board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
	(board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
	(board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
	(board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
	(board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal
space_check=lambda board,pos:" "
def full_board_check(board):
	for i in range(1,10):
		if space_check(board, i):
			return False
	return True
replay=lambda : input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')
def play():
	print('Welcome to Tic Tac Toe!')
	while True:
		# Reset the board
		theboard = [' '] * 10
		player1_marker, player2_marker = mark_choice()
		player_name()
		turn = player_choice()
		print(str(turn) + ' will go first.')
		game_on = True

		while game_on:
			if turn == player1:
				# Player1's turn.

				display_board(theboard)
				position = player_pos(theboard)
				place_marker(theboard, player1_marker, int(position))

				if win_check(theboard, player1_marker):
					display_board(theboard)
					print('Congratulations!'+str(player1)+ ' You have won the game!')
					game_on = False
				else:
					if full_board_check(theboard):
						display_board(theboard)
						print('The game is a draw!')
						break
					else:
						turn = player2

			else:
				# Player2's turn.

				display_board(theboard)
				position = player_pos(theboard)
				place_marker(theboard, player2_marker, int(position))

				if win_check(theboard, player2_marker):
					display_board(theboard)
					print(player2+' has won!')
					game_on = False
				else:
					if full_board_check(theboard):
						display_board(theboard)
						print('The game is a tie!')
						break
					else:
						turn = player1

		if not replay():
			break

play()


