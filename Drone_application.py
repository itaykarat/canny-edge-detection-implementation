import main
from djitellopy import Tello
import cv2, math, time


def drone_canny_view():
    #  drone settings
    canny_detection= main.cannyEdgeFilter()
    tello = Tello()
    tello.connect()
    tello.streamon()
    frame_read = tello.get_frame_read()
    tello.takeoff()
    cap = canny_detection.cap

    while True:
        # In reality you want to display frames in a seperate thread. Otherwise
        #  they will freeze while the drone moves.
        img = frame_read.frame
        EdgeImg = canny_detection.Canny_detector(img)  # find the qrCode in the given image
        cv2.imshow("drone", EdgeImg)

        key = cv2.waitKey(1) & 0xff
        if key == 27:  # ESC
            break
        elif key == ord('w'):
            tello.move_forward(30)
        elif key == ord('s'):
            tello.move_back(30)
        elif key == ord('a'):
            tello.move_left(30)
        elif key == ord('d'):
            tello.move_right(30)
        elif key == ord('e'):
            tello.rotate_clockwise(30)
        elif key == ord('q'):
            tello.rotate_counter_clockwise(30)
        elif key == ord('r'):
            tello.move_up(30)
        elif key == ord('f'):
            tello.move_down(30)

    tello.land()
