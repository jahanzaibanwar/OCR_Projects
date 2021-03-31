#!usr/bin/env python
# coding:utf-8
"""
******************************************************
Name :first_oc.py                                     *
Author : Jahanzaib Anwar                             *
Email : anwar@semine.no                              * 
Time :16.03.2021 14:26                                *
Desc                                                 * 
******************************************************
"""
import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
## Uncomment If we want to execute from command line

# ap = argparse.ArgumentParser()
# ap.add_argument("-i", "--image", required=True,
#	help="path to input image to be OCR'd")
# args = vars(ap.parse_args())

image = cv2.imread("whole_foods.png")
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
text = pytesseract.image_to_string(image)
print(text)
