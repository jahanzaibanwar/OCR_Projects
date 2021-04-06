#!usr/bin/env python
# coding:utf-8
"""
******************************************************
Name :reading_HOCR.py                                     *
Author : Jahanzaib Anwar                             *
Email : anwar@semine.no                              * 
Time :06.04.2021 16:21                                *
Desc                                                 * 
******************************************************
"""
import bs4
xml_input = open("hand_hocr.hocr","r",encoding="utf-8")
soup = bs4.BeautifulSoup(xml_input,'lxml')
ocr_lines = soup.findAll("span", {"class": "ocr_line"})
#We will save coordinates of line and the text contained in the line in lines_structure list
lines_structure = []
for line in ocr_lines:
    line_text = line.text.replace("\n"," ").strip()
    title = line['title']
    #print(title)
    #The coordinates of the bounding box
    x1,y1,x2,y2 = map(int, title[5:title.find(";")].split())
    print(x1,y1,x2,y2,line_text)
    lines_structure.append({"x1":x1,"y1":y1,"x2":x2,"y2":y2,"text": line_text})
    lines_structure.append(title)


#print(lines_structure)