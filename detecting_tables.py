#!usr/bin/env python
# coding:utf-8
"""
******************************************************
Name :detecting_tables.py                                     *
Author : Jahanzaib Anwar                             *
Email : anwar@semine.no                              * 
Time :29.03.2021 21:30                                *
Desc                                                 * 
******************************************************
"""
import cv2

image = cv2.imread("Medium.Png")
## print(type(image))
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#scale_percent = 50

#calculate the 50 percent of original dimensions
#width = int(gray.shape[1] * scale_percent / 100)
#height = int(gray.shape[0] * scale_percent / 100)

# dsize
#dsize = (width, height)

# resize image
#gray = cv2.resize(gray, dsize)






BLUR_KERNEL_SIZE = (17, 17)
STD_DEV_X_DIRECTION = 0
STD_DEV_Y_DIRECTION = 0
blurred = cv2.GaussianBlur(gray, BLUR_KERNEL_SIZE, STD_DEV_X_DIRECTION, STD_DEV_Y_DIRECTION)
cv2.imshow("Blurred", blurred)



MAX_COLOR_VAL = 255
BLOCK_SIZE = 15
SUBTRACT_FROM_MEAN = -2
img_bin = cv2.adaptiveThreshold( blurred, MAX_COLOR_VAL, cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,BLOCK_SIZE,SUBTRACT_FROM_MEAN)
cv2.imshow("img_bin", img_bin)

vertical = horizontal = img_bin.copy()
image_width, image_height = horizontal.shape
SCALE = 5

horizontal_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (int(image_width / SCALE), 1))
horizontally_opened = cv2.morphologyEx(img_bin, cv2.MORPH_OPEN, horizontal_kernel) # Horizontal Lines

vertical_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, int(image_height / SCALE)))
vertically_opened = cv2.morphologyEx(img_bin, cv2.MORPH_OPEN, vertical_kernel) #Vertical Lines

horizontally_dilated = cv2.dilate(horizontally_opened, cv2.getStructuringElement(cv2.MORPH_RECT, (40, 1)))
vertically_dilated = cv2.dilate(vertically_opened, cv2.getStructuringElement(cv2.MORPH_RECT, (1, 60)))


cv2.imshow("horizontally_opened", horizontally_opened )
cv2.imshow("Verticall Lines", vertically_opened)
cv2.imshow("h_dialated", horizontally_dilated)
cv2.imshow("Verticall dialated", vertically_dilated)

mask = horizontally_dilated + vertically_dilated
contours, heirarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)# Getting dtype=int32 check
#contours = contours.dtype("uint8")
#print(contours)

MIN_TABLE_AREA = 1e5
contours = [c for c in contours if cv2.contourArea(c) > MIN_TABLE_AREA]
#print(contours)
perimeter_lengths = [cv2.arcLength(c, True) for c in contours]
print(perimeter_lengths)
epsilons = [0.1 * p for p in perimeter_lengths]
print(epsilons)

approx_polys = [cv2.approxPolyDP(c, e, True) for c, e in zip(contours, epsilons)]
print(approx_polys)
bounding_rects = [cv2.boundingRect(a) for a in approx_polys]

images = [gray[y:y + h, x:x + w] for x, y, w, h in bounding_rects]
print(images)
cv2.imshow("horizontally_opened", images[0] )
#print(bounding_rects)

cv2.waitKey(0)
cv2.destroyAllWindows()



