# the goal is to compare how performs the DL 
# model against random mouvements to assess
# if indeed there is a small success rate

from shiftit import ShiftIt
from random import choice

mygame = ShiftIt(5, 5)
moves = mygame.moves
nb_tries = 1000

max_moves = 20
# Assess random movements success rate

def assess_random() :
    success_nb = 0
    moves_nb = 0

    for _ in range(nb_tries) :
        mygame.generate()
        mygame.shuffle(shuffle_moves)

        for j in range(max_moves) :
            key = choice(moves)
            mygame.shift(key)

            if mygame.state : 
                success_nb +=1
                moves_nb +=j
                break
    
    success_moves_mean = moves_nb / success_nb
    return success_nb, success_moves_mean
    
def assess_AI() :
    success_nb = 0
    moves_nb = 0

    for _ in range(nb_tries) :
        mygame.generate()
        mygame.shuffle(shuffle_moves)

        _path = mygame.solve_with_AI(limit=max_moves, mod=True)

        if mygame.state : 
            success_nb +=1
            moves_nb += len(_path)

    success_moves_mean = moves_nb / success_nb
    return success_nb, success_moves_mean


for _ in range(1, 7) :
    shuffle_moves = _
    print('\n\nNumber of shuffle moves : {}'.format(_))
    _a, _b = assess_random()
    print('# --- RANDOM METHOD --- #',
        'Success rate : {}'.format(_a/nb_tries),
        'Moves mean when success : {}'.format(_b),
        sep='\n'
    )

    _a, _b = assess_AI()
    print('# --- AI METHOD --- #',
        'Success rate : {}'.format(_a/nb_tries),
        'Moves mean when success : {}'.format(_b),
        sep='\n'
    )