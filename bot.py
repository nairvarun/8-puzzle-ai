# todo:
	# add ai part
	# add readme
	# find good license and add it

# region imports
import random
#endregion

# region function definitions

# prints game board.


def print_board(board):
	b = '''
	|%s|%s|%s|
	--+-+--
	|%s|%s|%s|
	--+-+--
	|%s|%s|%s|
	''' % (board[1], board[2], board[3], board[4], board[5], board[6], board[7], board[8], board[9])
	print(b)

# returns list of valid moves.


def get_valid_moves(board, empty_pos):
	if board[empty_pos] == board[1]:
		return ('s', 'd')
	elif board[empty_pos] == board[2]:
		return ('s', 'a', 'd')
	elif board[empty_pos] == board[3]:
		return ('s', 'a')
	elif board[empty_pos] == board[4]:
		return ('w', 's', 'd')
	elif board[empty_pos] == board[5]:
		return ('w', 's', 'a', 'd')
	elif board[empty_pos] == board[6]:
		return ('w', 's', 'a')
	elif board[empty_pos] == board[7]:
		return ('w', 'd')
	elif board[empty_pos] == board[8]:
		return ('w', 'a', 'd')
	elif board[empty_pos] == board[9]:
		return ('w', 'a')
	else:
		print('invalid move')
		print_board(board)

# if entered move is valid, makes move.


def make_move(board):
	empty_pos = list(board.keys())[list(board.values()).index(' ')]
	valid_moves = get_valid_moves(board, empty_pos)

	print_board(board)
	move = input('w = up \ns = down \na = left \nd = right \nyour move: ')

	if move == 'w':
		if move in valid_moves:
			board[empty_pos], board[empty_pos-3] = board[empty_pos-3], board[empty_pos]
		else:
			print("invalid move")
	elif move == 's':
		if move in valid_moves:
			board[empty_pos], board[empty_pos+3] = board[empty_pos+3], board[empty_pos]
		else:
			print("invalid move")
	elif move == 'a':
		if move in valid_moves:
			board[empty_pos], board[empty_pos-1] = board[empty_pos-1], board[empty_pos]
		else:
			print("invalid move")
	elif move == 'd':
		if move in valid_moves:
			board[empty_pos], board[empty_pos+1] = board[empty_pos+1], board[empty_pos]
		else:
			print("invalid move")
	else:
		print("invalid move")

# game loop


def start_game(board):

	# dictionary 'goal_state' represents the main 8 puzzle board
	goal_state = board

	#shuffles the board for the initial state
	k = list(board.keys())
	v = list(board.values())
	random.shuffle(v)

	# assigns the shuffled values to the board
	board = {k[i]: v[i] for i in range(len(k))}

	print('========================')
	print('initial state:')
	print_board(board)
	print('goal state:')
	print_board(goal_state)
	print('========================')

	# board = {
	# 1: 1,
	# 2: 2,
	# 3: 3,
	# 4: 4,
	# 5: 5,
	# 6: 6,
	# 7: 7,
	# 8: ' ',
	# 9: 8
	# }

	while board != goal_state:
		make_move(board)

	print_board(board)
	print('CONGRATULATIONS!!! you won!!')

# main function


def main():

	# dictionary 'board' represents the main 8 puzzle board
	board = {
		1: 1,
		2: 2,
		3: 3,
		4: 4,
		5: 5,
		6: 6,
		7: 7,
		8: 8,
		9: ' '
	}

	# starts the game
	start_game(board)

#endregion


if __name__ == '__main__':
    main()
