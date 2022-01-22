import main
import cv2

testOBJ = main.cannyEdgeFilter()
cap= testOBJ.cap

# Check if the webcam is opened correctly
if not cap.isOpened():
    raise IOError("Cannot open webcam")

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
    canny_img = testOBJ.Canny_detector(frame)  # process the image in every frame and show to screen
    cv2.imshow('Input', canny_img)

    c = cv2.waitKey(1)
    if c == 27:
        break

cap.release()
cv2.destroyAllWindows()