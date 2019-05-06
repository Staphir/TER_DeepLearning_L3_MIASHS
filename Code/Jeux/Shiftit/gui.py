from tkinter import (Frame, Tk, Button, Label, PhotoImage)
import shiftit
from time import sleep
# -------------------------------------------------------------------
class GUI ():
    def __init__(self, master, height, width) :
        self.__core = shiftit.ShiftIt(height, width)
        self.__master = master
        self.__height = height
        self.__width = width
        self.__length = width * height
        self.__colors = ['yellow', 'red', 'blue', 'green', 'black', 'white']
        self.path_to_success = []
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
        # ---
        self.__arrows = dict()
        self.__cellList = []
        self.__imgCache = []
        # ---
        for i in range((self.__height+2)*(self.__width+2)) :
            x, y = i//(self.__width+2), i%(self.__width+2)

            if (x in [0, self.__height+1] or y in [0, self.__width+1]) :
                _dir, idx, key = self.get_idx_dir(x, y)

                if idx is not None :
                    # _img = ImageTk.PhotoImage(Image.open(
                    #     f"./img/arrow{_dir}_flat.png").resize((48,48), Image.ANTIALIAS))
                    _img = PhotoImage(file=f"./img/arrow{_dir}_flat.png")
                    _cell = Button(self.__gridFrame, height=50, width=50, 
                        image=_img, relief='flat')
                    _cell.bind('<Button-1>', self.__buttonPress)
                    # ---
                    self.__arrows[key] = _cell
                    self.__imgCache.append(_img) # prevent garbage collection

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
            cell['bg'] = self.__colors[self.__core.grid[x][y]]

    def __buttonPress(self, event=None) :
        _k, _w = [(k,w) for k, w in self.__arrows.items() if w == event.widget][0]
        self.__core.shift(_k); self.__update()

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
        self.path_to_success = self.__core.shuffle(n)
        self.__update()

    def reset(self) :
        self.__core.generate()
        self.path_to_success = []
        self.__update()

    def solveAI(self) : 
        pass

    def solve(self) :
        self.execPath(self.path_to_success)

    def execPath(self, path=[]) :
        for key in path :
            
            _arr = self.__arrows[key]
            _dir = ['Up', 'Down'] if int(key[0])%2 else ['Left', 'Right']
            _fileName = [f'./img/arrow{_dir[len(key)>1]}_{state}.png' for state in ['pressed', 'flat']]
            _img_pressed = PhotoImage(file=_fileName[0])
            _img_flat = PhotoImage(file=_fileName[1])
            # ---
            _arr.config(image=_img_pressed)
            self.__master.update()
            # ---
            sleep(0.1)
            self.__core.shift(key)
            self.__update()
            sleep(0.1)
            # ---
            _arr.config(image=_img_flat)
            self.__master.update()
            # ---
            self.__imgCache.extend([_img_flat, _img_pressed]) # keeps growing, not very cool
        
        self.path_to_success = []
# -------------------------------------------------------------------
if __name__ == "__main__":
    root = Tk()
    mygui = GUI(root, 3, 5)
    root.mainloop()
# -------------------------------------------------------------------