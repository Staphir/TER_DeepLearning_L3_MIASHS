# from keras import Sequential
# from keras.layers import Dense
# from tensorflow.python.estimator import keras
# import tensorflow as tf
from Jeux.Shiftit.shiftit import ShiftIt


# pour le moment on choisit :
# une grille 5x5
# 10 mouvements
# 2 couleurs
max_moves = 10
colors = [0,1]
mygame = ShiftIt(5, 5)
tmp = mygame.moves
possible_moves = dict(zip(range(len(tmp)), tmp))
possible_moves_reverse = {v:k for k,v in possible_moves.items()}

print(possible_moves)

#
# def generate_game(max_moves=max_moves):
#     # generate a single game with max number of permutations number_moves
#
#
#     solution = mygame.shuffle(max_moves)
#     shuffled_grid = mygame.grid
#
#     return shuffled_grid, solution
#
#
# def generate_N_games(N=10, max_moves=max_moves):
#     solutions = []
#     for j in range(N):
#         shusolution = generate_game(max_moves=max_moves)
#         solutions.append(solution)
#
#     return solutions
#
#
# def generate_action_space(number_games=100):
#     D = []  # action space
#     states_hist = []
#     game_count = 0
#     play_game = True
#     global max_moves
#     while play_game:
#
#         scrambled_cube, solutions = generate_game(max_moves=max_moves)
#
#         state = scrambled_cube.copy()
#         for j in range(len(solutions)):
#             states_hist.append(state.copy())
#             action = solutions[j]
#             current_state = state.copy()
#             state_next = state(action)
#
#             state_next = state_next.copy()
#
#             reward = j + 1
#
#             D.append([current_state, action, reward, state_next])
#
#             state = state_next.copy()
#
#         states_hist.append(state.copy())
#
#         game_count += 1
#
#         if game_count >= number_games:
#             break
#
#     return D
#
# def generate_data(N=32):
#     while True:
#         x = []
#         y = []
#
#         D = generate_action_space(N)
#         for d in D:
#             x.append(cube2np(d[0]))
#             y.append(to_categorical(possible_moves.index((str(d[1]))), len(possible_moves)))
#
#         x = np.asarray(x)
#         x = x.reshape(x.shape[0], 18, 3, 1)
#         x = x.astype('float32')
#
#         y = np.asarray(y)
#         y = y.reshape(y.shape[0], y.shape[2])
#
#         yield (x, y)
#
#
#
#
# batch_size = 256
# num_classes = len(possible_moves)
# num_epochs = 150
# input_shape = (18, 3, 1)
#
# model = tf.keras.Sequential([
#     tf.keras.layers.Conv2D(256, kernel_size=(3, 3), activation='relu',
#                            input_shape=input_shape),
#     tf.keras.layers.MaxPooling2D(),
#     tf.keras.layers.Flatten(),
#     tf.keras.layers.Dropout(0.5),
#     tf.keras.layers.Dense(128, activation='relu'),
#     tf.keras.layers.BatchNormalization(),
#     tf.keras.layers.Dense(num_classes, activation='softmax')
# ])
#
# train_data = tf.ones(shape=(1, 18, 3, 1))
# test_data = tf.ones(shape=(1, 18, 3, 1))
#
# model.compile(optimizer='adam',
#               loss='sparse_categorical_crossentropy',
#               metrics=['accuracy'])
#
# model.summary()
#
# tbCallBack = keras.callbacks.TensorBoard(log_dir='/home/jerpint/Dropbox/rubiks/', histogram_freq=0, write_graph=True, write_images=True)
#
# model.fit(steps_per_epoch=50, epochs=num_epochs, verbose=2, validation_data=None,
#           max_queue_size=1, use_multiprocessing=False, workers=6, initial_epoch=0, train_data)
# loss, acc = model.evaluate(test_data)
#
# print("Loss {}, Accuracy {}".format(loss, acc))
#
# for j in range(num_epochs):
#
#     if (j % 10 == 0):
#         print('epoch #', j)
#     model.fit(steps_per_epoch=50,epochs=1, verbose=2, validation_data=None,
#               max_queue_size=1, use_multiprocessing=True,
#               workers=6, initial_epoch=0)  # generate_data(8)