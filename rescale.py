import cv2 as cv


def rescaleFrame(frame, scale=0.75):
    # Get original dimensions
    width = frame.shape[1]
    height = frame.shape[0]

    # Calculate new dimensions
    new_width = int(width * scale)
    new_height = int(height * scale)

    # Rescale frame
    return cv.resize(frame, (new_width, new_height), interpolation=cv.INTER_AREA)



# reading video data either takes interger arguments or path of the video
capture = cv.VideoCapture('/Users/amit/Desktop/AadharCode/openCVProjects/Resources/Videos/dog.mp4')

# Load the image
img = cv.imread('/Users/amit/Desktop/AadharCode/openCVProjects/Resources/Photos/cat_large.jpg')

if img is None:
    print("Error: Could not load image. Check the file path.")
else:
    cv.imshow("Cat", img)

# Rescale the image
scaled_img = rescaleFrame(img, scale=0.2)


# Display the resized image
cv.imshow("Rescaled Cat", scaled_img)

while True:
    # Read a frame from the video
    isTrue, frame = capture.read()
    # cv.imshow('Video', frame)
    # Rescale frame
    scaled_frame = rescaleFrame(frame)
    # cv.imshow('Rescaled Video', scaled_frame)


    # Break the loop if the video ends
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()



