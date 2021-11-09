# todo:
	# add proper ai part
	# add readme

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


# check whether the generated initial state is solvable.
def is_solvable(board):
	val = list(board.values())
	val.remove(' ')
	inv = 0
	for i in range(len(val)-1):
		for j in range(i+1, len(val)):
			if val[i] > val[j]:
				inv += 1
	if inv % 2 == 0:
		return True
	else:
		return False


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


# returns a random move for the ai.
def get_ai_move_random(board, empty_pos):
	print_board(board)
	valid_moves = get_valid_moves(board, empty_pos)
	best_move = random.choice(valid_moves)
	return best_move


# returns the best move it finds using just a simple heuristic function for the ai.
def get_ai_move_heuristic_func(board, goal_state, empty_pos):
	print_board(board)

	valid_moves = get_valid_moves(board, empty_pos)
	
	best_h = 0
	best_move = random.choice(valid_moves)

	for move in valid_moves:
		temp_board = board.copy()
		make_move(move, temp_board, empty_pos)
		# print_board(temp_board)
		h = 0
		# print('move:', move)
		for i in temp_board:
			if temp_board[i] == goal_state[i]:
				h += 1
		# print('h:', h)
		# print('best_h:', best_h)
		if h > best_h:
			best_h = h
			best_move = move
		# print('best_h:', best_h)
		# print('best_move:', best_move)

	# print('final best_h:', best_h)
	# print('final best_move:', best_move)
	return best_move


# returns the move that the human player wants to make if it is a valid move.
def get_human_move(board, empty_pos):
	print_board(board)
	valid_moves = get_valid_moves(board, empty_pos)

	move = input('w = up \ns = down \na = left \nd = right \nyour move: ')

	if 	move in valid_moves:
		return move
	else:
		return None


# makes move.
def make_move(move, board, empty_pos):
	if move == 'w':
		board[empty_pos], board[empty_pos-3] = board[empty_pos-3], board[empty_pos]
	elif move == 's':
		board[empty_pos], board[empty_pos+3] = board[empty_pos+3], board[empty_pos]
	elif move == 'a':
		board[empty_pos], board[empty_pos-1] = board[empty_pos-1], board[empty_pos]
	elif move == 'd':
		board[empty_pos], board[empty_pos+1] = board[empty_pos+1], board[empty_pos]
	else:
		print("invalid move")


# game loop.
def start_game(board):

	# dictionary 'goal_state' represents the main 8 puzzle board.
	goal_state = board

	#shuffles the board for the initial state.
	k = list(board.keys())
	v = list(board.values())

	while True:
		# print('generated unsolvable board')
		random.shuffle(v)
		# assigns the shuffled values to the board.
		board = {k[i]: v[i] for i in range(len(k))}
		# breaks out of the loop if the generated initial state is solvable.
		if is_solvable(board) == True:
			break

	print('========================')
	print('initial state:')
	print_board(board)
	# print(board)
	print('goal state:')
	print_board(goal_state)
	# print(goal_state)
	print('========================')

	# board = {
	# 	1: 1,
	# 	2: 2,
	# 	3: 3,
	# 	4: 4,
	# 	5: 5,
	# 	6: 6,
	# 	7: 7,
	# 	8: ' ',
	# 	9: 8
	# }

	while board != goal_state:

		empty_pos = list(board.keys())[list(board.values()).index(' ')]

		# region for humans: 

		while True:
			move = get_human_move(board, empty_pos)
			if move != None:
				break


		# endregion
		
		# region for ai:

		# random move.
		# move = get_ai_move_random(board, empty_pos)
		
		# unsing only heuristic function. 
		# move = get_ai_move_heuristic_func(board, goal_state, empty_pos)

		# endregion

		make_move(move, board, empty_pos)

	print_board(board)
	print('CONGRATULATIONS!!! you won!!')

# main function.
def main():

	# dictionary 'board' represents the main 8 puzzle board.
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

	# starts the game.
	start_game(board)

#endregion


if __name__ == '__main__':
    main()
