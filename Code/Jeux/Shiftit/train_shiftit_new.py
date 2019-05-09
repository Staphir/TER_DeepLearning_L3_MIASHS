# ===================================================================
# Shift It : A learning Method
# ===================================================================

__author__  = "Martin Devreese, Maxime Dulieu, Tim Laurençon"
__version__ = "1.0"
__date__    = "09/05/2019"
# -------------------------------------------------------------------
import pickle
from copy import deepcopy

#import Martin
# from tensorflow.keras.models import Sequential
# from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten, Conv2D, MaxPooling2D
# from tensorflow.keras.utils import to_categorical
# from shiftit import ShiftIt

#import Maxime
from Jeux.Shiftit.shiftit import ShiftIt
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense, Dropout, Activation, Flatten, Conv2D, MaxPooling2D
from tensorflow.python.keras.utils import to_categorical

# import communs
import numpy as np
import tensorflow as tf
from tensorflow import keras

# -------------------------------------------------------------------
# --- env vars ------------------------------------------------------
_use_saved_data = True
_use_random_playground = True
max_moves = 5
height, width = 5, 5
mygame = ShiftIt(height, width)
# --- prepare env ---------------------------------------------------
# config = tf.ConfigProto()
# config.gpu_options.allow_growth = True
# config.gpu_options.per_process_gpu_memory_fraction = 0.4
# session = tf.Session(config=config)
_tmp = mygame.moves
moves = dict(zip(range(len(_tmp)), _tmp))
reverse_moves = {v:k for k,v in moves.items()}
# --- define data generating methods --------------------------------
def data_generator(game_count=100) : # iterator
    # set iteration number
    _iter = 0

    while _iter < game_count :

        # get ready for use game object and path
        game, path = generate_game()
        
        # yield solution list for each game

        yield generate_game_data(game, path)

        _iter +=1
# -------------------------------------------------------------------
def generate_game() :

    if _use_random_playground :
        # generate random playground
        mygame.generate()
    else :
        # or reset to learn on exact same starting pattern
        # would be nice to try out if no result with random patterns
        mygame.reset()

    # shuffle playground and get path to success
    path_to_success = mygame.shuffle(max_moves)

    return deepcopy(mygame), path_to_success
# -------------------------------------------------------------------
def generate_game_data(game, path) :
    # grid x next_step_to_solution
    _solList = []

    # iterate over the path
    for key in path :

        # get the playground as numpy.array before applying key
        _grid = game.list_grid

        # get the solution for a given grid for training
        _label = reverse_moves[key]

        # store grid and key
        _solList.append([ _grid, _label ])

        # execute key
        game.shift(key)

    # send back each resolution step
    return _solList
# --- building model ------------------------------------------------
input_shape = (-1, height, width, 1)
outputl = len(moves)

epoch_nb = 10
batch_size = 32


if not _use_saved_data :

    # --- 80 - 20 / train - eval; no need to shuffle data ---
    train_data_gen = data_generator(10000)
    eval_data_gen = data_generator(200)

    X = [] # feature set
    y = [] # label set

    for _set in train_data_gen :
        for feature, label in _set :
            X.append(feature) # feature
            y.append(label) # label

    X = np.array(X).reshape(*input_shape)
    y = to_categorical(y)

    # --- save data to disk to skip generating them again ---
    if _use_random_playground :
        pickle_out_X = open("X.pickle", "wb")
        pickle_out_y = open("y.pickle", "wb")
    else :
        pickle_out_X = open("X_stable.pickle", "wb")
        pickle_out_y = open("y_stable.pickle", "wb")

    pickle.dump(X, pickle_out_X)
    pickle_out_X.close()
    pickle.dump(y, pickle_out_y)
    pickle_out_y.close()

else :

    # --- get data from disk ---
    if _use_random_playground : 
        pickle_in_X = open("X.pickle", "rb") # with shiftit.generate()
        pickle_in_y = open("y.pickle", "rb")
    else :
        pickle_in_X = open("X_stable.pickle", "rb") # with shiftit.reset()
        pickle_in_y = open("y_stable.pickle", "rb")
    X = pickle.load(pickle_in_X)
    y = pickle.load(pickle_in_y)



# --- create the model ---
model = Sequential()

# --- input ---
model.add(Conv2D(64, (3,3), input_shape=input_shape[1:], activation='relu'))
model.add(Activation('relu'))
# model.add(MaxPooling2D(pool_size=(2,2), dim_ordering="th"))

# --- hidden layers ---
# model.add(Conv2D(64, (3,3), input_shape=input_shape[1:], activation='relu'))
model.add(Activation('relu'))
# model.add(MaxPooling2D(pool_size=(2,2), dim_ordering="th"))

model.add(Conv2D(128, kernel_size=(3,3), activation='relu'))
model.add(Flatten())
# model.add(Conv2D(64, kernel_size=(3,3), activation='relu'))
model.add(Dense(128, activation='tanh'))

# --- output ---
model.add(Dropout(0.5))
model.add(Dense(outputl, activation='softmax'))



# --- compile and run training ---
model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])

model.fit(X, y, batch_size=batch_size, validation_split=0.1, epochs=epoch_nb)



# --- saving the model ---
# model.save('shifit_model.h5')  # creates a HDF5 file 'my_model.h5'
# model.save('shifit_model_stable.h5')  # creates a HDF5 file 'my_model.h5'