#!usr/bin/env python
# coding:utf-8
"""
******************************************************
Name :HOCR_Extraction.py                                     *
Author : Jahanzaib Anwar                             *
Email : anwar@semine.no                              * 
Time :06.04.2021 08:49                                *
Desc                                                 * 
******************************************************
"""
import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

#image = cv2.imread("Medium.Png")

#pdf = tabula.read_pdf('test.pdf', pages = 'all',stream=True)
#pytesseract.run_tesseract('image.png', 'output', lang=None, boxes=False, config="hocr")

#print(pdf)

from pytesseract import pytesseract
pytesseract.run_tesseract("hand.jpg","hand_hocr",extension='jpg', lang=None,config="--psm 6 -c tessedit_create_hocr=1")
# "converted_image" is the output of convert utility and input to tesseract
# "output_hocr" is the name of the output hOCR file. The output file will have .hocr extension: "output_hocr.hocr"



