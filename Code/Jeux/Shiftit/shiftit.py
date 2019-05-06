# ===================================================================
# Shift It : Little python build of sliding game shift it
# ===================================================================
__author__  = "Martin Devreese"
__version__ = "1.0"
__date__    = "06/05/2019"
# -------------------------------------------------------------------
import numpy as np
from random import randrange, choice
# -------------------------------------------------------------------
class ShiftIt () :
    def __init__(self, n:int, m:int) :
        self.__height = n
        self.__width  = m
        self.__grid   = np.zeros((n, m), int)
        self.__path   = []
        # ---
        self.generate()
    
    def __str__(self) :
        return '\n'.join(map(str, self.grid))

    def __repr__(self) :
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
 
    def __get_revKey(self, key:str) :
        return key[0] if len(key)>1 else f"{key}'"

    def generate(self) : #c:int) : 
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

    def shuffle(self, n:int) :
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

    def empty_path(self) :
        self.__path = []

    @property
    def grid(self, use_np=False) : return self.__grid if use_np else self.__grid.tolist()
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
    mygame = ShiftIt(3,5); _sep = f"\n{'-'*15}\n"
    mygame.generate()
    print("# Solved state :", mygame, sep=_sep, end=_sep)
    path_to_success = mygame.shuffle(10)
    print("# Scrambled state :", mygame, sep=_sep, end=_sep)
    moves = mygame.moves
    print(f"# MOVES : {moves}", f"# PATH = {path_to_success}", sep=_sep, end=_sep)
    for key in path_to_success : mygame.shift(key)
    print("# After PATH application :", mygame, sep=_sep, end=_sep)
# -------------------------------------------------------------------