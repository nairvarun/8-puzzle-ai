# todo:
	# add proper ai part
	# add readme

# region imports
import random
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

    def print_state(state):
        print('''
                |%s|%s|%s|
                --+-+--
                |%s|%s|%s|
                --+-+--
                |%s|%s|%s|
            ''' % (state[1], state[2], state[3], state[4], state[5], state[6], state[7], state[8], state[9])
        )

    def is_solvable():
        # refer: https://www.geeksforgeeks.org/check-instance-8-puzzle-solvable/
        
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

    def get_human_move(empty_pos):
        valid_moves = Board.get_valid_moves(empty_pos)
        move = ''
        while move not in valid_moves:
            Board.print_state(Board.state)
            move = input('w = up \ns = down \na = left \nd = right \nyour move: ')
        return move

    def get_ai_move(empty_pos, mode):
        Board.print_state(Board.state)
        valid_moves = Board.get_valid_moves(empty_pos)

        if mode == 'random':
            best_move = random.choice(valid_moves)
        elif mode == 'heuristic':
            h = 0
            best_h = 0
            best_move = random.choice(valid_moves)
            for move in valid_moves:
                temp_board = Board.state.copy()
                Board.make_move(temp_board, move, empty_pos)
                for i in temp_board:
                    if temp_board[i] == Board.goal_state[i]:
                        h += 1
                if h > best_h:
                    best_h = h
                    best_move = move

        return best_move

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

    def game_loop():
        Board.gen_init_state()
    
        while Board.state != Board.goal_state:
            empty_pos = list(Board.state.keys())[list(Board.state.values()).index(' ')]
            # move = Board.get_human_move(empty_pos)
            # move = Board.get_ai_move(empty_pos, 'random')
            move = Board.get_ai_move(empty_pos, 'heuristic')
            Board.make_move(Board.state ,move, empty_pos)
        Board.print_state(Board.state)
        print('CONGRATULATIONS!!! you won!!')


if __name__ == '__main__':
    Board.game_loop()