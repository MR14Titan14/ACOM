import cv2
import numpy as np
import os
import pytesseract as tes
from jiwer import wer
from collections import Counter
import re
import easyocr

tes.pytesseract.tesseract_cmd = (r"C:\Program Files\Tesseract-OCR\tesseract.exe")

# h, w, c = img.shape
# boxes = tes.image_to_boxes(img)
# for b in boxes.splitlines():
#     b = b.split(' ')
#     img = cv2.rectangle(img, (int(b[1]), h - int(b[2])), (int(b[3]), h - int(b[4])), (0, 255, 0), 2)

def augmentation_ds(ds_dir):
    images = os.listdir(f"{ds_dir}")
    print(images)
    for name in images:
        image = cv2.imread(f"{ds_dir}/{name}")
        for angle in range(-20, 21):
            # Получение размеров изображения
            (h, w) = image.shape[:2]

            # Определение центра изображения
            center = (w // 2, h // 2)

            # Создание матрицы поворота
            M = cv2.getRotationMatrix2D(center, angle, 1.0)

            # Вычисление новой ширины и высоты, чтобы избежать обрезки
            cos = np.abs(M[0, 0])
            sin = np.abs(M[0, 1])

            # Новые размеры
            new_w = int((h * sin) + (w * cos))
            new_h = int((h * cos) + (w * sin))

            # Корректировка матрицы поворота для смещения центра
            M[0, 2] += new_w / 2 - center[0]
            M[1, 2] += new_h / 2 - center[1]

            # Поворот изображения с новыми размерами
            rotated_image = cv2.warpAffine(image, M, (new_w, new_h))

            cv2.imwrite(f"{name[:-4]}_{angle}.jpg", rotated_image)


def create_agds_txt():
    with open(f'ds1.txt', 'r', encoding="utf-8") as f:
        strings = f.read().splitlines()
    with open(f'ds2_t.txt', 'w', encoding="utf-8") as f:
        for s in strings:
            for angle in range(-20, 21):
                f.write(f"{s.split(':')[0]}_{angle}:{s.split(':')[1]}\n")


def test_recognition(rec_type, val_type, ds_dir):
    res = dict()
    labels = dict()
    images = os.listdir(f"{ds_dir}")
    reswriter = open(f'{ds_dir} {rec_type} {val_type}.txt', 'w', encoding="utf-8")
    with open(f'{ds_dir}.txt', 'r', encoding="utf-8") as f:
        strings = f.read().splitlines()
    for s in strings:
        labels[s.split(':')[0]] = s.split(':')[1]

    if rec_type == "straight_recognition":
        for name in images:
            img = cv2.imread(f"{ds_dir}/{name}", cv2.COLOR_BGR2GRAY)
            img = cv2.medianBlur(img, 3)
            text = tes.image_to_string(img, lang="rus+eng")
            res[name[:-4]] = str(text).replace("\n", "")

    if rec_type == "augmented_recognition":
        for name in images:
            responses = []
            img = cv2.imread(f"{ds_dir}/{name}", cv2.COLOR_BGR2GRAY)
            img = cv2.medianBlur(img, 3)
            for angle in range(-20, 21):
                # Получение размеров изображения
                (h, w) = img.shape[:2]

                # Определение центра изображения
                center = (w // 2, h // 2)

                # Создание матрицы поворота
                M = cv2.getRotationMatrix2D(center, angle, 1.0)

                # Вычисление новой ширины и высоты, чтобы избежать обрезки
                cos = np.abs(M[0, 0])
                sin = np.abs(M[0, 1])

                # Новые размеры
                new_w = int((h * sin) + (w * cos))
                new_h = int((h * cos) + (w * sin))

                # Корректировка матрицы поворота для смещения центра
                M[0, 2] += new_w / 2 - center[0]
                M[1, 2] += new_h / 2 - center[1]

                # Поворот изображения с новыми размерами
                rotated_image = cv2.warpAffine(img, M, (new_w, new_h))
                text = tes.image_to_string(rotated_image, lang="rus+eng")
                responses.append(text)
            counted = Counter(responses)
            if '' in counted:
                del counted['']
            # print(counted)
            most_common, _ = counted.most_common()[0]
            # print(most_common)
            res[name[:-4]] = str(most_common).replace("\n", "")

    if rec_type == "with_post_recognition":
        for name in images:
            img = cv2.imread(f"{ds_dir}/{name}", cv2.COLOR_BGR2GRAY)
            img = cv2.medianBlur(img, 3)
            text = tes.image_to_string(img, lang="rus+eng")
            reg=re.compile('[^a-zA-Zа-яА-Я ]')
            text = str(text).replace("\n", "")
            res[name[:-4]] = reg.sub('',text.lower())

    if rec_type == "easyOCR":
        reader = easyocr.Reader(['en','ru'],gpu=True)
        for name in images:
            result=reader.readtext(f"{ds_dir}/{name}",detail=0,paragraph=True)
            reg = re.compile('[^a-zA-Zа-яА-Я ]')
            text = str(result[0]).replace("\n", "")
            res[name[:-4]] = reg.sub('', text)


    if val_type == "accuracy":
        count = 0
        for i in labels.keys():
            if res[i].lower() == labels[i].lower():
                count += 1
        reswriter.write(f"accuracy: {count / len(labels)}\n")
    if val_type == "wer":
        sum = 0.0
        for i in labels.keys():
            sum += float(wer(labels[i], res[i]))
        reswriter.write(f"average wer: {sum / len(labels)}\n")

    for i in labels.keys():
        reswriter.write(f'{res[i]} : {labels[i]}\n')

# augmentation_ds("ds1")
# create_agds_txt()
# test_recognition("straight_recognition","wer","ds2")
# test_recognition("augmented_recognition","wer","ds1")
# test_recognition("with_post_recognition","wer","ds2")
test_recognition("easyOCR","wer","ds2")
