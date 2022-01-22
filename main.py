import numpy as np
import os
import cv2
import matplotlib.pyplot as plt

"""
The Canny edge detection algorithm is composed of 5 steps:
1.Noise reduction;
2.Gradient calculation;
3.Non-maximum suppression;
4.Double threshold;
5.Edge Tracking by Hysteresis.
"""

class cannyEdgeFilter():

    def __init__(self):
        self.cap= cv2.VideoCapture(0) # default cap is webcam stream
        self.cap.set(3,640)

    def Canny_detector(self,img):
        # apply filters to reduce noise
        img = self.change_to_gray_scale(img)
        # cv2.imshow('img after grayscale',img)

        img = self.apply_gaussian_blur(img)
        # cv2.imshow('img after gaussian blur',img)

        # Calculating the gradients -> find the points where theres a big contrast change in the pixels
        gx,img = self.calculate_x_gradient(img)
        gy,img = self.calculate_y_gradient(img)




        # get magnitude and angle with gradients in x and y axis
        mag, ang,img = self.calculate_magnitude_and_angle(img, gx, gy)
        # cv2.imshow('img after sobel',img)

        # set some boundary for the noise - if p_weak will be smaller than we will expect more noise
        p_weak = 0.4
        p_strong = 1

        # setting the minimum and maximum thresholds
        # for double thresholding
        mag_max = np.max(mag)


        weak_th = mag_max * p_weak   # if we change p_weak to bigger value we decrease sensitivity
        strong_th = mag_max * p_strong+ 100
        weak_ids,strong_ids,ids,img=self.get_direction(img,ang,mag)
        mag,img=self.double_threshold(img, mag, weak_th, strong_th, ids)
        return img




    def get_direction(self,img,ang,mag):
        # getting the dimensions of the input image
        height, width = img.shape
        # Looping through every pixel of the grayscale gaussian blurred image(=matrix)
        for i_x in range(width):
            for i_y in range(height):

                grad_ang = ang[i_y, i_x]
                grad_ang = abs(grad_ang - 180) if abs(grad_ang) > 180 else abs(grad_ang)

                # selecting the neighbours of the target pixel
                # according to the gradient direction
                # In the x axis direction
                if grad_ang <= 22.5:
                    neighb_1_x, neighb_1_y = i_x - 1, i_y
                    neighb_2_x, neighb_2_y = i_x + 1, i_y

                # top right (diagonal-1) direction
                elif grad_ang > 22.5 and grad_ang <= (22.5 + 45):
                    neighb_1_x, neighb_1_y = i_x - 1, i_y - 1
                    neighb_2_x, neighb_2_y = i_x + 1, i_y + 1

                # In y-axis direction
                elif grad_ang > (22.5 + 45) and grad_ang <= (22.5 + 90):
                    neighb_1_x, neighb_1_y = i_x, i_y - 1
                    neighb_2_x, neighb_2_y = i_x, i_y + 1

                # top left (diagonal-2) direction
                elif grad_ang > (22.5 + 90) and grad_ang <= (22.5 + 135):
                    neighb_1_x, neighb_1_y = i_x - 1, i_y + 1
                    neighb_2_x, neighb_2_y = i_x + 1, i_y - 1

                # Now it restarts the cycle
                elif grad_ang > (22.5 + 135) and grad_ang <= (22.5 + 180):
                    neighb_1_x, neighb_1_y = i_x - 1, i_y
                    neighb_2_x, neighb_2_y = i_x + 1, i_y

                # Non-maximum suppression step
                if width > neighb_1_x >= 0 and height > neighb_1_y >= 0:
                    if mag[i_y, i_x] < mag[neighb_1_y, neighb_1_x]:
                        mag[i_y, i_x] = 0
                        continue

                if width > neighb_2_x >= 0 and height > neighb_2_y >= 0:
                    if mag[i_y, i_x] < mag[neighb_2_y, neighb_2_x]:
                        mag[i_y, i_x] = 0

        weak_ids = np.zeros_like(img)
        strong_ids = np.zeros_like(img)
        ids = np.zeros_like(img)
        return weak_ids,strong_ids,ids,img


    def double_threshold(self,img, mag, weak_th, strong_th, ids):
        # double thresholding step
        height, width = img.shape
        for i_x in range(width):
            for i_y in range(height):

                grad_mag = mag[i_y, i_x]

                if grad_mag < weak_th:
                    mag[i_y, i_x] = 0
                elif strong_th > grad_mag >= weak_th:
                    ids[i_y, i_x] = 1
                else:
                    ids[i_y, i_x] = 2

        # finally returning the magnitude of
        # gradients of edges

        return mag,img

    def change_to_gray_scale(self,img):
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # conversion of image to grayscale
        # cv2.imshow('gray scale',img)
        # cv2.waitKey()
        return img


    def apply_gaussian_blur(self,img):
        img = cv2.GaussianBlur(img, (5, 5), 1.4)  # Noise reduction step with GaussianBlur
        # cv2.imshow('gaussian blur',img)
        # cv2.waitKey()
        return img


    def calculate_x_gradient(self,img):
        gx = cv2.Sobel(np.float32(img), cv2.CV_64F, 1, 0, 3)
        return gx,img


    def calculate_y_gradient(self,img):
        gy = cv2.Sobel(np.float32(img), cv2.CV_64F, 0, 1, 3)
        return gy,img


    def calculate_magnitude_and_angle(self,img, gx, gy):
        mag, ang = cv2.cartToPolar(gx, gy, angleInDegrees=True)  # mag= sqrt(pow(gx,2)+pow(gy,2))
        img=cv2.addWeighted(gx,0.5,gy,0.5,0)
        return mag, ang,img



# manual run for a specific image
testOBJ = cannyEdgeFilter()
frame = cv2.imread('assets/dvirSurf.jpg')
canny_img = testOBJ.Canny_detector(frame)
cv2.imshow("output", canny_img)
# cv2.imshow("input", frame)
cv2.waitKey()

