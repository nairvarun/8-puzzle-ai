# todo:
	# add proper ai part
	# add readme
    # is writing everything in a clss the righ tthing to do??
    # try with functional??
    # ad optimal ai (bfs?, a*?)
        # http://w01fe.com/blog/2009/01/the-hardest-eight-puzzle-instances-take-31-moves-to-solve/
        
  
# region imports
import random
import math
#endregion

class Board:

    goal_state = {
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

    state = goal_state.copy()

    closed = set({})

    # generetes the initial state of the board
    def gen_init_state():
        key, val = list(Board.state.keys()), list(Board.state.values())
        while True:
            random.shuffle(val)
            Board.state = {key[i]: val[i] for i in range(len(key))}
            # Board.state = {
            #     1: 1,
            #     2: 2,
            #     3: 3,
            #     4: 4,
            #     5: 5,
            #     6: 6,
            #     7: 7,
            #     8: ' ',
            #     9: 8
            # }
            if Board.is_solvable():
                break
        print('goal state:')
        Board.print_state(Board.goal_state)
        print('\n\n\n')

    # print the state of the board
    def print_state(state):
        print('''
                |%s|%s|%s|
                --+-+--
                |%s|%s|%s|
                --+-+--
                |%s|%s|%s|
            ''' % (state[1], state[2], state[3], state[4], state[5], state[6], state[7], state[8], state[9])
        )

    # checks if the board is solvable 
        # refer: https://www.geeksforgeeks.org/check-instance-8-puzzle-solvable/
    def is_solvable():
        
        val = list(Board.state.values())
        val.remove(' ')
        invs = 0
        for i in range(len(val)-1):
            for j in range(i+1, len(val)):
                if val[i] > val[j]:
                    invs += 1
        if invs % 2 == 0:
            return True
        else:
            return False

    # returns a tuple of all valid moves
    def get_valid_moves(empty_pos):
        if Board.state[empty_pos] == Board.state[1]:
            return ('s', 'd')
        elif Board.state[empty_pos] == Board.state[2]:
            return ('s', 'a', 'd')
        elif Board.state[empty_pos] == Board.state[3]:
            return ('s', 'a')
        elif Board.state[empty_pos] == Board.state[4]:
            return ('w', 's', 'd')
        elif Board.state[empty_pos] == Board.state[5]:
            return ('w', 's', 'a', 'd')
        elif Board.state[empty_pos] == Board.state[6]:
            return ('w', 's', 'a')
        elif Board.state[empty_pos] == Board.state[7]:
            return ('w', 'd')
        elif Board.state[empty_pos] == Board.state[8]:
            return ('w', 'a', 'd')
        elif Board.state[empty_pos] == Board.state[9]:
            return ('w', 'a')
        else:
            print('invalid move')
            Board.print_state(Board.state)

    # get move from user in case of human player
    def get_human_move(empty_pos):
        valid_moves = Board.get_valid_moves(empty_pos)
        move = ''
        while move not in valid_moves:
            Board.print_state(Board.state)
            move = input('w = up \ns = down \na = left \nd = right \nyour move: ')
        return move

    # converts the board state to a string
    def get_val_str(board):
        val = list(map(str, board.values()))
        val[val.index(' ') ] = '0'
        return ''.join(val)

    # generetes moves for the ai
    def get_ai_move(empty_pos, mode):
        Board.print_state(Board.state)
        valid_moves = Board.get_valid_moves(empty_pos)

        if mode == 'random':
            best_move = random.choice(valid_moves)
        elif mode == 'heuristic':
            best_h = math.inf
            best_move = random.choice(valid_moves)
            for move in valid_moves:
                h = 0
                temp_board = Board.state.copy()
                Board.make_move(temp_board, move, empty_pos)
                for i in temp_board:
                    if temp_board[i] != Board.goal_state[i]:
                        h += 1
                if h < best_h:
                    best_h = h
                    best_move = move
        elif mode == 'heuristic2':
            best_h = math.inf
            best_move = random.choice(valid_moves)
            for move in valid_moves:
                h = 0
                temp_board = Board.state.copy()
                temp_closed = Board.closed.copy()
                Board.make_move(temp_board, move, empty_pos)
                if Board.get_val_str(temp_board) in temp_closed:
                    continue
                else:
                    temp_closed.add(Board.get_val_str(temp_board))
                for i in temp_board:
                    if temp_board[i] != Board.goal_state[i]:
                        h += 1
                if h < best_h:
                    best_h = h
                    best_move = move
        print(best_move)
        Board.closed.add(Board.get_val_str(Board.state))
        return best_move

    # makes actual move on the board
    def make_move(board ,move, empty_pos):
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

    # game loop
    def game_loop():
        Board.gen_init_state()
    
        i = 0
        while Board.state != Board.goal_state:
            empty_pos = list(Board.state.keys())[list(Board.state.values()).index(' ')]
            # move = Board.get_human_move(empty_pos)
            # move = Board.get_ai_move(empty_pos, 'random')
            # move = Board.get_ai_move(empty_pos, 'heuristic')
            move = Board.get_ai_move(empty_pos, 'heuristic2')
            Board.make_move(Board.state ,move, empty_pos)
            i += 1
        Board.print_state(Board.state)
        print('moves: {}'.format(i))
        print('CONGRATULATIONS!!! you won!!')


if __name__ == '__main__':
    Board.game_loop()