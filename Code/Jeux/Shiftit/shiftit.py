import numpy as np
from random import randrange
# -------------------------------------------------------------------
class ShiftIt () :
    def __init__(self, n:int, m:int) :
        self.__height  = n
        self.__width   = m
        self.__grid    = np.zeros((n, m), int)
    
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

    def generate(self,) : #c:int) : 
        # assert c <= 10, 'No more than 10 different colors'
        # nb de cases de chaques couleurs
        nbcells = randrange(3, self.height*self.width-3)

        success = False

        while not success :

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
            if not success : 
                self.__grid = np.zeros((self.height, self.width), int)

    def shuffle(self, n:int) :
        success = True
        path = []

        while success :

            for _ in range(n) :
                idx = randrange(self.width + self.height)
                key = '{}{}'.format(idx, "'" if randrange(2) else '')
                self.shift(key); path.append(key[0] if len(key)>1 else f"{key}'")

            success = self.__check_success()
        
        return path[::-1]

    def shift(self, key:str) :
        """
        row -> even; col -> odd
        """
        vec = int(key[0])%2; idx = int(key[0])//2
        grid = np.rot90(self.__grid,-1) if vec else self.__grid
        grid[idx] = np.roll(grid[idx], -1 if len(key)>1 else 1)
        self.__grid = np.rot90(grid) if vec else grid

    @property
    def grid(self) : return self.__grid.tolist()
    @property
    def height(self) : return self.__height
    @property
    def width(self) : return self.__width
# -------------------------------------------------------------------
def adjacent(x1, y1, x2, y2) : # unused
    return x1-x2 in [-1,1] != y1-y2 in [-1,1]
# -------------------------------------------------------------------
if __name__ == "__main__":
    mygame = ShiftIt(5,5)
    # ---
    print(f"{mygame}\n{'-'*15}")
    mygame.generate()
    print(f"{mygame}\n{'-'*15}")
    # ---
    path_to_success = mygame.shuffle(10)
    # ---
    print(f"{mygame}\n{'-'*15}")
    print(f"# PATH : {path_to_success}\n{'-'*15}")
    # ---
    for key in path_to_success :
        mygame.shift(key)
        # print(f"{mygame}\n{'-'*15}")
    # ---
    print(f"{mygame}\n{'-'*15}")

# -------------------------------------------------------------------