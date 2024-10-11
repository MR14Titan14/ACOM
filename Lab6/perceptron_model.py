import keras
from keras._tf_keras.keras.datasets import mnist
from keras._tf_keras.keras.layers import Dense
from keras._tf_keras.keras.utils import to_categorical
from keras._tf_keras.keras.optimizers import Adam

batchSize=128
epochs=20
neurons=512

num_train = 60000
num_test = 10000

height, width, depth = 28, 28, 1
num_classes = 10

(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train = x_train.reshape(num_train, height * width)
x_test = x_test.reshape(num_test, height * width)
x_train = x_train.astype('float32')
x_test = x_test.astype('float32')
x_train /= 255
x_test /= 255

y_train = to_categorical(y_train, num_classes)
y_test = to_categorical(y_test, num_classes)

model = keras.Sequential()

model.add(Dense(neurons, input_shape=(784, ), activation='relu'))
model.add(Dense(neurons, activation='relu'))

model.add(Dense(10, activation='softmax'))


optimizer = Adam(learning_rate=0.001)
model.compile(optimizer=optimizer, loss='categorical_crossentropy', metrics=['accuracy'])

model.fit(x_train, y_train, epochs=epochs, batch_size=batchSize)

accuracy = model.evaluate(x_test,y_test)
print(f'Точность {accuracy[1]*100:.2f}%')

model.save("percep.keras")