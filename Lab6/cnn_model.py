import keras
from keras._tf_keras.keras.datasets import mnist
from keras._tf_keras.keras.layers import Dense,Conv2D,MaxPooling2D,Flatten
from keras._tf_keras.keras.utils import to_categorical
from keras._tf_keras.keras.optimizers import Adam, SGD

batchSize=128
epochs=20

num_train = 60000
num_test = 10000

num_classes = 10

# Загрузка данных MNIST и предобработка
(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train = x_train.reshape(x_train.shape[0], 28, 28, 1).astype('float32') / 255
x_test = x_test.reshape(x_test.shape[0], 28, 28, 1).astype('float32') / 255

y_train = to_categorical(y_train, num_classes)
y_test = to_categorical(y_test, num_classes)

model = keras.Sequential()

model.add(Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(28, 28, 1)))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(64, kernel_size=(3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Flatten())
model.add(Dense(128, activation='relu'))

model.add(Dense(10, activation='softmax'))

#optimizer = Adam(learning_rate=0.001)
optimizer = SGD(learning_rate=0.001)
model.compile(optimizer=optimizer, loss='categorical_crossentropy', metrics=['accuracy'])

# model.add(Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(28, 28, 1)))
# model.add(MaxPooling2D(pool_size=(2, 2)))
#
# model.add(Conv2D(64, kernel_size=(3, 3), activation='relu'))
# model.add(MaxPooling2D(pool_size=(2, 2)))
#
# model.add(Conv2D(128, kernel_size=(3, 3), activation='relu'))
# model.add(MaxPooling2D(pool_size=(2, 2)))
#
# model.add(Flatten())
# model.add(Dense(256, activation='relu'))
#
# model.add(Dense(10, activation='softmax'))
#
# optimizer = Adam(learning_rate=0.001)
# #optimizer = SGD(learning_rate=0.001)
# model.compile(optimizer=optimizer, loss='categorical_crossentropy', metrics=['accuracy'])

model.fit(x_train, y_train, epochs=epochs, batch_size=batchSize, validation_data=(x_test, y_test))

accuracy = model.evaluate(x_test,y_test)
print(f'Точность {accuracy[1]*100:.2f}%')

model.save("cnn.keras")