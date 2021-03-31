#!usr/bin/env python
# coding:utf-8
"""
******************************************************
Name :localizing_text.py                                     *
Author : Jahanzaib Anwar                             *
Email : anwar@semine.no                              * 
Time :22.03.2021 18:04                                *
Desc                                                 * 
******************************************************
"""
import cv2
import pytesseract
from pytesseract import Output
from imutils.contours import sort_contours
import imutils
import sys
import numpy as np
from textblob import TextBlob

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

image = cv2.imread("Medium.Png")
rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
results = pytesseract.image_to_data(rgb, output_type=Output.DICT)
print(results.keys())

for i in range(0, len(results["text"])):
    # extract the bounding box coordinates of the text region from
    # the current result
    x = results["left"][i]
    y = results["top"][i]
    w = results["width"][i]
    h = results["height"][i]

    # extract the OCR text itself along with the confidence of the
    # text localization
    text = results["text"][i]
    conf = int(results["conf"][i])

    # filter out weak confidence text localizations
    if conf > 40:
        # display the confidence and text to our terminal
        print("Confidence: {}".format(conf))
        print("Text: {}".format(text))
        print(x, y, (x + w, y + h))

        print("")

        # strip out non-ASCII text so we can draw the text on the image
        # using OpenCV, then draw a bounding box around the text along
        # with the text itself

        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
    # cv2.putText(image, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
    #	1.2, (0, 0, 255), 3)

# show the output image
cv2.imshow("Image", image)
cv2.waitKey(0)
