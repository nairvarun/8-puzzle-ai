def print_board(board):
	b = '''
	|%s|%s|%s|
	--+-+--
	|%s|%s|%s|
	--+-+--
	|%s|%s|%s|
	'''%(board[1], board[2], board[3], board[4], board[5], board[6], board[7], board[8], board[9])
	print(b)


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
		print('board[9]:', board[9])
		make_move(board)



def make_move(board):

	move = input('w = up \ns = down \na = left \nd = right \nyour move: ')

	empty_pos = list(board.keys())[list(board.values()).index(' ')]

	print('empty_pos:', empty_pos)

	valid_moves = get_valid_moves(board, empty_pos)

	if move == 'w':
		if move in valid_moves:
			board[empty_pos], board[empty_pos-3] = board[empty_pos-3], board[empty_pos]
			print_board(board)
		else:
			print("invalid move")
			print('empty_pos =', empty_pos)
			print(valid_moves)
	if move == 's':
		if move in valid_moves:
			board[empty_pos], board[empty_pos+3] = board[empty_pos+3], board[empty_pos]
			print_board(board)
		else:
			print("invalid move")
			print('empty_pos =', empty_pos)
			print(valid_moves)
	if move == 'a':
		if move in valid_moves:
			board[empty_pos], board[empty_pos-1] = board[empty_pos-1], board[empty_pos]
			print_board(board)
		else:
			print("invalid move")
			print(empty_pos-1)
			print('empty_pos =', empty_pos)
			print(valid_moves)
	if move == 'd':
		if move in valid_moves:
			board[empty_pos], board[empty_pos+1] = board[empty_pos+1], board[empty_pos]
			print_board(board)
		else:
			print("invalid move")
			print('empty_pos =', empty_pos)
			print(valid_moves)





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
    
	print_board(board)

	while True:
		make_move(board)

	
    

if __name__ == '__main__':
    main()