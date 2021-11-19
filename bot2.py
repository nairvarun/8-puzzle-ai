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
        k = list(Board.state.keys())
        v = list(Board.state.values())
        while True:
            random.shuffle(v)
            Board.state = {k[i]: v[i] for i in range(len(k))}
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
            return {'s', 'd'}
        elif Board.state[empty_pos] == Board.state[2]:
            return {'s', 'a', 'd'}
        elif Board.state[empty_pos] == Board.state[3]:
            return {'s', 'a'}
        elif Board.state[empty_pos] == Board.state[4]:
            return {'w', 's', 'd'}
        elif Board.state[empty_pos] == Board.state[5]:
            return {'w', 's', 'a', 'd'}
        elif Board.state[empty_pos] == Board.state[6]:
            return {'w', 's', 'a'}
        elif Board.state[empty_pos] == Board.state[7]:
            return {'w', 'd'}
        elif Board.state[empty_pos] == Board.state[8]:
            return {'w', 'a', 'd'}
        elif Board.state[empty_pos] == Board.state[9]:
            return {'w', 'a'}
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

    def make_move(move, empty_pos):
        if move == 'w':
            Board.state[empty_pos], Board.state[empty_pos-3] = Board.state[empty_pos-3], Board.state[empty_pos]
        elif move == 's':
            Board.state[empty_pos], Board.state[empty_pos+3] = Board.state[empty_pos+3], Board.state[empty_pos]
        elif move == 'a':
            Board.state[empty_pos], Board.state[empty_pos-1] = Board.state[empty_pos-1], Board.state[empty_pos]
        elif move == 'd':
            Board.state[empty_pos], Board.state[empty_pos+1] = Board.state[empty_pos+1], Board.state[empty_pos]
        else:
            print("invalid move")

    def game_loop():
        while Board.state != Board.goal_state:

            empty_pos = list(Board.state.keys())[list(Board.state.values()).index(' ')]

            # region for humans: 
            move = Board.get_human_move(empty_pos)
            # endregion
		

            # region for ai:

            # random move.
            # move = get_ai_move_random(board, empty_pos)
            
            # unsing only heuristic function. 
            # move = get_ai_move_heuristic_func(board, goal_state, empty_pos)

            # endregion

            Board.make_move(move, empty_pos)

        Board.print_state(Board.state)
        print('CONGRATULATIONS!!! you won!!')


Board.gen_init_state()
Board.game_loop()