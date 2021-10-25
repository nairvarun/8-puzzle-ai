def print_board(board):
	b = '''
	|%s|%s|%s|
	--+-+--
	|%s|%s|%s|
	--+-+--
	|%s|%s|%s|
	'''%(board[1], board[2], board[3], board[4], board[5], board[6], board[7], board[8], board[9])
	print(b)

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
		9: ' ',
		'temp': ''
	}
    
	print_board(board)
    

if __name__ == '__main__':
    main()