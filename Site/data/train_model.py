model = Sequential()

# --- input ---
model.add(Conv2D(64, (3, 3), input_shape=input_shape[1:], activation='relu'))
model.add(Activation('relu'))

# --- hidden layers ---
model.add(Activation('relu'))
model.add(Conv2D(128, kernel_size=(3, 3), activation='relu'))
model.add(Flatten())
model.add(Dense(128, activation='tanh'))

# --- output ---
model.add(Dropout(0.5))
model.add(Dense(outputl, activation='softmax'))