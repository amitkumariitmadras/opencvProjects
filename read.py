import cv2 as cv

# Load the image
img = cv.imread('/Users/amit/Desktop/AadharCode/openCVProjects/Resources/Photos/cat_large.jpg')

if img is None:
    print("Error: Could not load image. Check the file path.")
else:
    cv.imshow("Cat", img)

    # Wait for a key event
    # Press 'q' or Esc (ASCII 27) to exit
    if cv.waitKey(0) & 0xFF == 27:  # Wait for the Esc key
        cv.destroyAllWindows()