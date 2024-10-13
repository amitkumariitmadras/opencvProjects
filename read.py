import cv2 as cv

# # Load the image
# img = cv.imread('/Users/amit/Desktop/AadharCode/openCVProjects/Resources/Photos/cat_large.jpg')

# if img is None:
#     print("Error: Could not load image. Check the file path.")
# else:
#     cv.imshow("Cat", img)


#reading video data either takes interger arguments or path of the video
capture = cv.VideoCapture('/Users/amit/Desktop/AadharCode/openCVProjects/Resources/Videos/dog.mp4')

while True:
    # Read a frame from the video
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)



    # Break the loop if the video ends
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()


    #     # Wait for a key event
    #     # Press 'q' or Esc (ASCII 27) to exit
    # if cv.waitKey(0) & 0xFF == 27:  # Wait for the Esc key
    #     cv.destroyAllWindows()