# ===================================================================
# Shift It : Little python build of sliding game shift it AI Solver
# ===================================================================
__author__  = "Martin Devreese, Maxime Dulieu, Tim Laurençon"
__version__ = "1.0"
__date__    = "06/05/2019"
# -------------------------------------------------------------------
from tensorflow.keras.models import load_model
import numpy as np
# -------------------------------------------------------------------
class AISolver () :
    def __init__(self, wd, moves) :
        # self.__modelfile = f"{wd}/models/shiftit_model.h5"
        self.__modelfile = f"{wd}/models/shiftit_model_1.h5"
        self.__model = load_model(self.__modelfile)
        self.__moves = dict(zip(range(len(moves)), moves))
        # self.__reverse_moves = {v:k for k,v in self.__moves.items()}
        # ---
        self.__model.compile(loss="categorical_crossentropy", 
            optimizer="adam", metrics=["accuracy"])
        # self.__model.compile(loss='binary_crossentropy',
        #       optimizer='rmsprop', metrics=['accuracy'])

    def predict(self, grid) :
        _w, _h = len(grid[0]), len(grid)
        _in = np.array(grid).reshape(-1, _h, _w, 1)
        _out = self.__model.predict([_in])
        _idx = np.where(_out == np.amax(_out))[1][0]
        return self.__moves[_idx]
# -------------------------------------------------------------------