import cv2 as cv

img = cv.imread('/Users/amit/Desktop/AadharCode/openCVProjects/Resources/Photos/cats.jpg')
cv.imshow('Cats', img)

# Averaging of surrounding windows kernel
average = cv.blur(img, (3,3))
cv.imshow('Average Blur', average)

# Gaussian Blur according to weighted: 0 is standard deviation in the x direction
gauss = cv.GaussianBlur(img, (3,3), 0)
cv.imshow('Gaussian Blur', gauss)

# Median Blur: i
median = cv.medianBlur(img, 3)
cv.imshow('Median Blur', median)

# Bilateral- retains the edges while implying blurring, 10: diameter
bilateral = cv.bilateralFilter(img, 10 , 35, 25)
cv.imshow('Bilateral', bilateral)

cv.waitKey(0)