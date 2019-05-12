# ===================================================================
# Shift It : Little python build of sliding game shift it
# ===================================================================
__author__  = "Martin Devreese, Maxime Dulieu, Tim Laurençon"
__version__ = "1.0"
__date__    = "06/05/2019"
# -------------------------------------------------------------------
from tkinter import (Frame, Tk, Button, Label, PhotoImage, StringVar)
import shiftit
import sys
from time import sleep
# -------------------------------------------------------------------
class GUI ():
    def __init__(self, master, height, width) :
        # self.__wd     = './TER_DeepLearning_L3_MIASHS/Code/jeux/Shiftit/'
        self.__wd     = './'
        self.__core = shiftit.ShiftIt(height, width, wd=self.__wd)
        self.__master = master
        self.__height = height
        self.__width = width
        self.__length = width * height
        self.__colors = ['orange', 'red', 'blue', 'green', 'black', 'white']
        self.__busy = False
        # ---
        self.__initialize()

    def __initialize(self) :
        self.__master.title('ShiftIt Game - TER Application')
        self.__master.resizable(False, False)
        self.__gridFrame = Frame(self.__master)
        # ---
        header = Frame(self.__master, height=100)
        Label(header, text='Shift It !', font='Helvetica 18').grid(row=0, column=0, columnspan=4, pady=10)
        Button(header, text='Solve (AI)', font='Helvetica 12', relief='groove', 
            command=self.solveAI).grid(row=1, column=0, ipadx=5, ipady=2, padx=10)        
        Button(header, text='Solve', font='Helvetica 12', relief='groove', 
            command=self.solve).grid(row=1, column=1, ipadx=5, ipady=2, padx=10)        
        Button(header, text='Reset', font='Helvetica 12', relief='groove', 
            command=self.reset).grid(row=1, column=2, ipadx=5, ipady=2, padx=10)        
        Button(header, text='Shuffle', font='Helvetica 12', relief='groove', 
            command=self.shuffle).grid(row=1, column=3, ipadx=5, ipady=2, padx=10)
        self.__successVar = StringVar()
        self.__successVar.set('True')
        Label(header, text='SUCCESS :').grid(row=2, column=1, pady=20)
        Label(header, textvariable=self.__successVar).grid(row=2, column=2)
        # ---
        self.__arrows = dict()
        self.__cellList = []
        # ---
        for i in range((self.__height+2)*(self.__width+2)) :
            x, y = i//(self.__width+2), i%(self.__width+2)

            if (x in [0, self.__height+1] or y in [0, self.__width+1]) :
                _dir, idx, key = self.get_idx_dir(x, y)

                if idx is not None :
                    _img = PhotoImage(file=f"{self.__wd}img/arrow{_dir}_flat.png")
                    _cell = Button(self.__gridFrame, height=50, width=50, 
                        image=_img, relief='flat')
                    _cell.bind('<Button-1>', self.__buttonPress)
                    # ---
                    self.__arrows[key] = [_cell, _img] # prevent garbage collection

                else : continue

            else :
                _cell = Frame(self.__gridFrame, height=50, width=50)
                _cell['bg'] = self.__colors[0]
                self.__cellList.append(_cell)

            _cell.grid(row=x, column=y, padx=3, pady=3)
        # ---
        header.grid(row=0, column=0)
        self.__gridFrame.grid(row=1, column=0, padx=50, pady=20)
        # ---
        self.__update()
        self.__master.update()

    def __update(self) :
        for i in range(self.__length) :
            x, y = i//self.__width, i%self.__width
            cell = self.__cellList[i]
            cell['bg'] = self.__colors[self.__core.list_grid[x][y]]
        self.__successVar.set(str(self.__core.state))
        self.__master.update()

    def __buttonPress(self, event=None) :
        if self.__busy : return
        else : self.__busy = True
        # ---
        _k, _w = [(k,w[0]) for k, w in self.__arrows.items() if w[0] == event.widget][0]
        self.__core.shift(_k); self.__update()
        #---
        self.__busy = False

    def get_idx_dir(self, x, y) :
        _mdir = ['Up','Down','Left','Right']
        # ---
        if (0 < x <= self.__height or 0 < y <= self.__width) :
            _dir = _mdir[0 if not x else (1 if x == self.__height+1 else (2 if not y else 3))]
            idx = (x-1)*2 if _dir in ['Left', 'Right'] else (y-1)*2+1
            key = '{}{}'.format(idx,"'" if _dir in ['Right', 'Down'] else '')
            return (_dir, idx, key)
        else : return (None, None, None)

    def shuffle(self, n=10) :
        if self.__busy : return
        else : self.__busy = True
        # ---
        self.__core.shuffle(n)
        self.__update()
        # ---
        self.__busy = False

    def reset(self) :
        if self.__busy : return
        else : self.__busy = True
        # ---
        self.__core.generate()
        self.__update()
        # ---
        self.__busy = False

    def solveAI(self) : 
        if self.__busy : return
        else : self.__busy = True
        # ---
        predicted_path = self.__core.solve_with_AI()
        self.execPath(predicted_path)
        # ---
        self.__busy = False

    def solve(self) :
        if self.__busy : return
        else : self.__busy = True
        # ---
        try : self.execPath(self.__core.path)
        except Exception : pass # prevent error showing up after closing windows while solving
        self.__core.empty_path()
        # ---
        self.__busy = False

    def execPath(self, path=[]) :
        for key in path :
            
            _arr = self.__arrows[key][0]
            _dir = ['Up', 'Down'] if int(key[0])%2 else ['Left', 'Right']
            _fileName = [f'{self.__wd}img/arrow{_dir[len(key)>1]}_{state}.png'
                        for state in ['pressed', 'flat']]
            _img_pressed = PhotoImage(file=_fileName[0])
            _img_flat = PhotoImage(file=_fileName[1])
            # ---
            _arr.config(image=_img_pressed)
            self.__master.update()
            # ---
            sleep(.1)
            self.__core.shift(key)
            self.__update()
            sleep(.1)
            # ---
            _arr.config(image=_img_flat)
            self.__master.update()
            # ---
            self.__arrows[key][1] = _img_flat # prevent garbage collection
# -------------------------------------------------------------------
if __name__ == "__main__":
    root = Tk()
    try :
        n, m = int(sys.argv[1]), int(sys.argv[2])
        mygui = GUI(root, n, m)
    except (ValueError, IndexError) :
        mygui = GUI(root, 5, 5)
    root.mainloop()
# -------------------------------------------------------------------