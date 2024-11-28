# pip install pytesseract opencv-python 
import cv2
import pytesseract
import numpy as np
from PIL import Image

#read image
def ocr_core(image):
    text=pytesseract.image_to_string(image,config=' --oem 1 --psm 11 ',lang='eng',nice=-1)
    return text

image=cv2.imread('image6.png') #image path


#resize the image
new_size=(1500,800)
resized_image=cv2.resize(image,new_size)
# cv2.imshow('resize.png',resized_image)
# cv2.waitKey(20000000)

#convert image to inverted image
inverted_image=cv2.bitwise_not(resized_image)
# cv2.imwrite("inverted.png",inverted_image)


#conert inverted image to gray image
gray_image = cv2.cvtColor(inverted_image, cv2.COLOR_BGR2GRAY)
#cv2.imwrite("gray.png",gray_image)
# cv2.imshow('gray.png',gray_image)
# cv2.waitKey(2000000)


#thresholding
# _,thresh_image=cv2.threshold(gray_image,70,240,cv2.THRESH_BINARY)
# cv2.imshow('thresh.png',thresh_image)
# cv2.waitKey(2000000)


#print text
print(ocr_core(gray_image))

