import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8')
cv.imshow("blank",blank)

# paint the image with some color
blank[200:300, 300:400] = 0,255,0
cv.imshow('Green', blank)


# 2. Draw a Rectangle
cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,255,0), thickness=-1)
cv.imshow('Rectangle', blank)

# 3. Draw A circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,255), thickness=-1)
cv.imshow('Circle', blank)

# 4. Draw a line
cv.line(blank, (100,250), (300,400), (255,255,255), thickness=3)
cv.imshow('Line', blank)

# 5. Write text
cv.putText(blank, 'Hello, my name is Jason!!!', (0,225), cv.AKAZE_DESCRIPTOR_KAZE, 1.0, (255,255,255), 2)
cv.imshow('Text', blank)


if cv.waitKey(0) & 0xFF == 27:  # Wait for the Esc key
    cv.destroyAllWindows()