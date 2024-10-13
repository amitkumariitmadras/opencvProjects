# to check out edges
import cv2 as cv
import numpy as np

img = cv.imread('/Users/amit/Desktop/AadharCode/openCVProjects/Resources/Photos/park.jpg')
cv.imshow('Park', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Laplacian Method
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap)) # image type uint8
cv.imshow('Laplacian', lap)

# Sobel Method
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)
combined_sobel = cv.bitwise_or(sobelx, sobely)

cv.imshow('Sobel X', sobelx)
cv.imshow('Sobel Y', sobely)
cv.imshow('Combined Sobel', combined_sobel)

canny = cv.Canny(gray, 150, 175)
cv.imshow('Canny', canny)
cv.waitKey(0)