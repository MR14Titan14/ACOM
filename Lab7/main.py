import cv2
import os
import pytesseract as tes
import easyocr
from jiwer import wer

tes.pytesseract.tesseract_cmd=(r"C:\Program Files\Tesseract-OCR\tesseract.exe")

def test_recognition(rec_type,val_type,ds_dir):
    res=dict()
    labels=dict()
    images = os.listdir(f"{ds_dir}")
    reswriter=open(f'result.txt', 'w', encoding="utf-8")
    with open(f'{ds_dir}.txt', 'r',encoding="utf-8") as f:
        strings = f.read().splitlines()
    for s in strings:
        labels[s.split('-')[0]]=s.split('-')[1]

    if rec_type=="straight_recognition":
        for name in images:
            img=cv2.imread(f"{ds_dir}/{name}")
            text=tes.image_to_string(img,lang="rus+eng")
            res[name[:-4]]=str(text).replace("\n","")
        print(res)
        print(labels)

    if val_type=="accuracy":
        count=0
        for i in range(1,len(labels)):
            if res[f"{i}"]==labels[f"{i}"]:
                count+=1
        reswriter.write(f"accuracy: {count/len(labels)}\n")
    if val_type=="wer":
        sum = 0.0
        for i in range(1, len(labels)):
            sum += float(wer(labels[f"{i}"],res[f"{i}"]))
        reswriter.write(f"average wer: {sum / len(labels)}\n")

    for i in range(1,len(labels)):
        reswriter.write(f'{res[f"{i}"]} - {labels[f"{i}"]}\n')



test_recognition("straight_recognition","wer","ds1")