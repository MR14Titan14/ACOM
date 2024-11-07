import cv2
import numpy as np
import os
import pytesseract as tes
import easyocr
from jiwer import wer

tes.pytesseract.tesseract_cmd=(r"C:\Program Files\Tesseract-OCR\tesseract.exe")

def augmentation_ds(ds_dir):
    images = os.listdir(f"{ds_dir}")
    print(images)
    for name in images:
        image = cv2.imread(f"{ds_dir}/{name}")
        for angle in range(-20,21):
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
    with open(f'ds1.txt', 'r',encoding="utf-8") as f:
        strings = f.read().splitlines()
    with open(f'ds2_t.txt', 'w',encoding="utf-8") as f:
        for s in strings:
            for angle in range(-20,21):
                f.write(f"{s.split(':')[0]}_{angle}:{s.split(':')[1]}\n")

def test_recognition(rec_type,val_type,ds_dir):
    res=dict()
    labels=dict()
    images = os.listdir(f"{ds_dir}")
    reswriter=open(f'{ds_dir} {rec_type} {val_type}.txt', 'w', encoding="utf-8")
    with open(f'{ds_dir}.txt', 'r',encoding="utf-8") as f:
        strings = f.read().splitlines()
    for s in strings:
        labels[s.split(':')[0]]=s.split(':')[1]

    if rec_type=="straight_recognition":
        for name in images:
            img=cv2.imread(f"{ds_dir}/{name}",cv2.COLOR_BGR2GRAY)
            img=cv2.medianBlur(img,3)
            text=tes.image_to_string(img,lang="rus+eng")
            res[name[:-4]]=str(text).replace("\n","")
        print(res)
        print(labels)

    if val_type=="accuracy":
        count=0
        for i in labels.keys():
            if res[i]==labels[i]:
                count+=1
        reswriter.write(f"accuracy: {count/len(labels)}\n")
    if val_type=="wer":
        sum = 0.0
        for i in labels.keys():
            sum += float(wer(labels[i],res[i]))
        reswriter.write(f"average wer: {sum / len(labels)}\n")

    for i in labels.keys():
        reswriter.write(f'{res[i]} : {labels[i]}\n')

test_recognition("straight_recognition","wer","ds2")
#augmentation_ds("ds1")
#create_agds_txt()