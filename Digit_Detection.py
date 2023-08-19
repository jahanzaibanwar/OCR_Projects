#!usr/bin/env python
# coding:utf-8
"""
******************************************************
Name :Digit_Detection.py                                     *
Author : Jahanzaib Anwar                             *
                             * 
Time :17.03.2021 11:43                                *
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
## print(type(image))
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
gray_image.shape
#(h,w) = (gray_image.shape[0],gray_image.shape[1])
#width = gray_image[1]
#print (h,w)

rectKernel = cv2.getStructuringElement(cv2.MORPH_RECT, (25, 7))
# sqKernel = cv2.getStructuringElement(cv2.MORPH_RECT, (21, 21))
#
gray = cv2.GaussianBlur(gray_image, (3, 3), 0)
blackhat = cv2.morphologyEx(gray, cv2.MORPH_BLACKHAT, rectKernel)
# cv2.imshow("Blackhat", blackhat)
#
#
#
#
#
grad = cv2.Sobel(blackhat, ddepth=cv2.CV_32F, dx=1, dy=0, ksize=-1)
grad = np.absolute(grad)
(minVal, maxVal) = (np.min(grad), np.max(grad))
grad = (grad - minVal) / (maxVal - minVal)
grad = (grad * 255).astype("uint8")
# cv2.imshow("Gradient", grad)
#
#
grad = cv2.morphologyEx(grad, cv2.MORPH_CLOSE, rectKernel)
thresh = cv2.threshold(grad, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
cv2.imshow("Rect Close", thresh)
#
#
#
cv2.waitKey(0)
cv2.destroyAllWindows()


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
text = pytesseract.image_to_string(image,config='--psm 11')
#text = text.replace("\n", " ")
print(text)
#tb = TextBlob(text)
#print(tb.detect_language())
#translated= tb.translate(to="eng")
#print(translated)
bad_chars = [';', ':', '/', "*", '|']
# for i in bad_chars:
#   cleaned_text = text.replace(i, '')

# print(cleaned_text)
