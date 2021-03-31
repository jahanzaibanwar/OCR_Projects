#!usr/bin/env python
# coding:utf-8
"""
******************************************************
Name :image_processing.py                                     *
Author : Jahanzaib Anwar                             *
Email : anwar@semine.no                              * 
Time :17.03.2021 16:33                                *
Desc                                                 * 
******************************************************
"""
import cv2
import pytesseract
from pytesseract import Output
import imutils
from textblob import TextBlob

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

image = cv2.imread("challenging_example.png")
## print(type(image))
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
## Threshold the image
thresh = cv2.threshold(gray,0,255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]

print(thresh)
print(len(thresh))
#cv2.imshow("original", image)
cv2.imshow("gray", gray)
cv2.imshow("Otsu", thresh)
cv2.waitKey(0)

#results = pytesseract.image_to_osd(image, output_type=Output.DICT)
#print(results)

# print("[INFO] detected orientation: {}".format( results["orientation"]))
# print("[INFO] rotate by {} degrees to correct".format(results["rotate"]))


## Rotate the image to correct the orientation
# rotated = imutils.rotate_bound(image,angle=results["rotate"])
## Displaying The images
# cv2.imshow("Original", image)
# cv2.imshow("Output", rotated)
# cv2.waitKey(0)

## Add config = digits if we only want digits
text = pytesseract.image_to_string(image,config="--psm 8")
#text = text.replace("\n", " ")
print(text)