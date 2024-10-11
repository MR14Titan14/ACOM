import cv2
import numpy as np
from keras._tf_keras.keras.models import load_model

# Персептрон
# model = load_model('percep.keras')
#
# img = cv2.imread('4.png', cv2.IMREAD_GRAYSCALE)
#
# img = img / 255.0
#
# img = img.reshape(1, 784)
#
# predictions = model.predict(img)
# predicted_digit = np.argmax(predictions)
#
# print(f"Цифра: {predicted_digit}")

# Сверточная
model = load_model('cnn.keras')

img = cv2.imread('8.png', cv2.IMREAD_GRAYSCALE)

img = img / 255.0

img = img.reshape(1, 28, 28, 1)

predictions = model.predict(img)
predicted_digit = np.argmax(predictions)

print(f"Цифра: {predicted_digit}")
