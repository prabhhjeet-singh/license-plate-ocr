# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 07:52:10 2020

@author: Prabhjeet
"""
import cv2, pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
image = cv2.imread('Cropped Images-Text/14.png')
resized_image = cv2.resize(image, None, fx = 2, fy = 2, interpolation = cv2.INTER_CUBIC)
gray = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5,5), 0)
#thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

#kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
#opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=1)
#invert = 255 - opening

# Perform text extraction
data = pytesseract.image_to_string(blur, lang='eng', config='--oem 3 -l eng --psm 6 ')
print(data)