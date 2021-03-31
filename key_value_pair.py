#!usr/bin/env python
# coding:utf-8
"""
******************************************************
Name :key_value_pair.py                                     *
Author : Jahanzaib Anwar                             *
Email : anwar@semine.no                              * 
Time :30.03.2021 10:18                                *
Desc                                                 * 
******************************************************
"""
from pytesseract import Output
from sklearn.cluster import AgglomerativeClustering
from tabulate import tabulate
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pytesseract
import argparse
import imutils
import cv2
import scipy.cluster.hierarchy as shc
from sklearn.preprocessing import normalize

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

np.random.seed(42)

image = cv2.imread("Medium.Png")
## print(type(image))
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

options = "--psm 6"
results = pytesseract.image_to_data(cv2.cvtColor(gray, cv2.COLOR_BGR2RGB), config=options, output_type=Output.DICT)
print(results.keys())
left_point =results['left']
print(left_point)
#print((results['line_num']))
#print(len(results['text']))
#print(results['block_num'])
#print(results)
coords = []
ocrText = []

for i in range(0, len(results["text"])):
    # extract the bounding box coordinates of the text region from
    # the current result
    x = results["left"][i]
    y = results["top"][i]
    w = results["width"][i]
    h = results["height"][i]
    block_numer = results['block_num'][i]
    word_nummer = results['word_num'][i]
    line_num = results['line_num'][i]
    #print(type(x))

    # extract the OCR text itself along with the confidence of the
    # text localization
    text = results["text"][i]
    #print(type(text))
   # print(text)
    conf = int(results["conf"][i])
    if 447  ==  x:
        #pass
        print(text)
     #   print(text[x])
        #print(block_numer)
       # print("On the basis of x" ,text)
        #print("wod_number of faktura word " ,word_nummer)
        #print("Line Nummber of word faktura" , line_num,text)
        #box = x
        #new_box = box+1
        #if text != '' :
         #   print(text[new_box],new_box)



        #print(text)

        #print(box,text)
        #print(x)
    if "1011985" in text:
        #print(block_numer)
        x_point = x
        #print('word_number of number',word_nummer)
        #print("Line Nummber of faktura number", line_num,text)
        #print(text)
        #print(x_point,text)
    if "Ordrenr" in text:
        pass
        #box_kunde = (x,y,w,h)
        #print("line number of order number",line_num,text)
    if "551552" in text:
        pass
        #order_number_box =(x,y,w,h)
       # print("line number of order number in numbers", line_num, text)
        #print(order_number_box, text)

    # filter out weak confidence text localizations
    if conf > 0:
        coords.append((x, y, w, h))
        ocrText.append(text)

        cv2.rectangle(gray, (x, y), (x + w, y + h), (0,29, 120), 2)

scaled_coordiantes = normalize(coords)
#print(scaled_coordiantes)
columns = ["x","y","w","h"]
#dataframe = pd.DataFrame(scaled_coordiantes, columns=columns)
#print(dataframe.head(10))
#plt.figure(figsize=(10, 7))
#plt.title("Dendrograms using Ward")
#dend = shc.dendrogram(shc.linkage(dataframe, method='ward'))
#plt.show()
#plt.show(block = True)

#print(coords)
#xCoords = [(c[0],c[1] ) for c in coords]
#print(len(coords))
#print(len(ocrText))
#print(clustering.labels_)
#print(coords)
#print(ocrText)

cv2.imshow("Image", gray)
cv2.waitKey(0)
cv2.destroyAllWindows()