# ===================================================================
# Shift It : fonctional core of puzzle sliding game shift it
# ===================================================================
__author__  = "Martin Devreese, Maxime Dulieu, Tim Laurençon"
__version__ = "1.1"
__date__    = "10/05/2019"
# -------------------------------------------------------------------
import numpy as np
from random import randrange, choice
from solver import AISolver
# -------------------------------------------------------------------
class ShiftIt () :
    def __init__(self, n:int, m:int, wd='./', solver=True) :
        self.__height = n
        self.__width  = m
        self.__grid   = np.zeros((n, m), int)
        self.__path   = []
        self.__solver = AISolver(wd, self.moves) if solver else None
        self.solvedState = []
        # ---
        self.generate()
    
    def __str__(self) -> str :
        return '\n'.join(map(str, self.list_grid))

    def __repr__(self) -> str :
        rep = '<ShiftIt {}x{}>'.format
        return rep(self.height, self.width)

    def __check_success(self) -> bool :
        _seen, _adj = [], []
        tmp = self.__grid.flatten()
        unique, counts = np.unique(tmp, return_counts=True)
        _cdict = dict(zip(unique, counts))

        for idx in range(self.height * self.width) :

            x, y = idx//self.width, idx%self.width
            cc = self.__grid[x,y]

            if (x,y) in _seen : continue
            else : _seen.append((x,y))

            _adj = self.__neighbours(x,y,cc)
            
            for (i,j) in _adj :
                if (i,j) in _seen : continue
                _seen.append((i,j))

                for (ni,nj) in self.__neighbours(i,j,cc) :
                    if not (ni,nj) in _adj : 
                        _adj.append((ni,nj))

            if not len(_adj) == _cdict[cc] : return False
        
        return True

    def __neighbours(self, x:int, y:int, color:int) -> list :
        c = [[-1,0], [0,1], [1,0], [0,-1]]
        return [(x+i,y+j) for i, j in c if x+i 
            in range(self.height) and y+j in range(self.width)
            and self.__grid[x+i,y+j] == color]
 
    def __get_revKey(self, key:str) -> str :
        return key[0] if len(key)>1 else f"{key}'"

    def generate(self) : # , c:int=2) : 
        # assert c <= 10, 'No more than 10 different colors'
        # nb de cases de chaques couleurs
        
        nbcells = randrange(3, self.height*self.width-3)
        self.__path = []

        success = False

        while not success :

            self.__grid = np.zeros((self.__height, self.__width), int)

            beg = (randrange(self.height), randrange(self.width))
            _seen = [beg]

            for _ in range(nbcells) :
                cell = _seen[-1]
                n = self.__neighbours(*cell, 0)
                if not n : break
                x, y = n[randrange(len(n))]
                self.__grid[x,y] = 1
                _seen.append((x,y))

            success = self.__check_success()
        
        self.solvedState = self.__grid.copy()

    def shuffle(self, n:int) -> list:
        success = True

        while success :

            for _ in range(n) :

                key = choice(self.moves)
                self.shift(key)

            success = self.__check_success()

        return self.__path

    def shift(self, key:str) :
        """
        row -> even; col -> odd
        """
        vec = int(key[0])%2; idx = int(key[0])//2
        grid, _dir = (np.rot90(self.__grid,-1), (1,-1)) if vec else (self.__grid, (-1,1))
        grid[idx] = np.roll(grid[idx], _dir[len(key)>1])
        self.__grid = np.rot90(grid) if vec else grid

        self.__path = [self.__get_revKey(key), *self.__path]
        # self.__path = self.path[::-1].append(self.__get_revKey(key))[::-1]

    def empty_path(self) :
        self.__path = []

    def reset(self) :
        self.empty_path()
        self.__grid = self.solvedState

    def solve_with_AI(self, limit=20, mod=False) :
        if self.__solver is None : return []
        _path = []
        # _limit = limit_factor*len(self.__path)

        _tmp = (self.__path, self.__grid)

        # limit number of moves if lost - expected to happend (a lot)
        for _ in range(limit) :
            
            # If success, break move generation
            if self.__check_success() : break

            # get grid layout
            _grid = self.list_grid

            # Predict move according to built neural network
            _predicted_move = self.__solver.predict(_grid)

            # add the predicted move to the path
            _path.append(_predicted_move)


            # Execute key to generate next grid
            self.shift(_predicted_move)

        if not mod : self.__path, self.__grid = _tmp

        # _sep = f"\n{15*'-'}\n"
        # print(f'Number of moves predicted : {len(_path)}\nMove number limit {limit}', sep=_sep, end=_sep)
        return _path

    @property
    def list_grid(self) : return self.__grid.tolist()
    @property
    def np_grid(self) : return self.__grid
    @property
    def height(self) : return self.__height
    @property
    def width(self) : return self.__width
    @property
    def path(self) : return self.__path
    @property
    def state(self) : return self.__check_success()
    @property
    def moves(self) : 
        return sorted(["{}{}".format(key, "'" if i%2 else '') for i, key in 
            enumerate([*list(range(0, self.height*2, 2))*2, *list(range(1, self.width*2, 2))*2])])
# -------------------------------------------------------------------
def adjacent(x1, y1, x2, y2) : # unused
    return x1-x2 in [-1,1] != y1-y2 in [-1,1]
# -------------------------------------------------------------------
if __name__ == "__main__":
    print(f"Example of use with 3x5 playground :\n{36*'-'}")
    mygame = ShiftIt(3,5) 
    _sep = f"\n{'-'*15}\n"
    mygame.generate()
    print("# Solved state :", mygame, sep=_sep, end=_sep)
    path_to_success = mygame.shuffle(10)
    print("# Scrambled state :", mygame, sep=_sep, end=_sep)
    moves = mygame.moves
    print(f"# POSSIBLE MOVES : {moves}", f"# PATH = {path_to_success}", sep=_sep, end=_sep)
    for key in path_to_success : mygame.shift(key)
    print("# After PATH application :", mygame, sep=_sep, end=_sep)
# -------------------------------------------------------------------