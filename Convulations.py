import cv2
import argparse
import numpy as np


# create VideoCapture object
cap = cv2.VideoCapture(0)
if (cap.isOpened() == False):
    print('Error while trying to open video. Plese check again...')
# get the frame width and height
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
# define codec and create VideoWriter object
out = cv2.VideoWriter('out_videos/marketing_out.avi', cv2.VideoWriter_fourcc('M','J','P','G'), 30, (frame_width, frame_height))

# read until end of video
while(cap.isOpened()):
    # capture each frame of the video
    ret, frame = cap.read()
    if ret == True:
        # add gaussian blurring to frame
        frame_1 = cv2.GaussianBlur(frame, (15, 15), 0)
        frame_2 =cv2.bitwise_not(frame)
        # save video frame
        out.write(frame_1)
        # display frame
        cv2.imshow('Blurred', frame_1)
        cv2.imshow('Normal',frame)
        cv2.imshow('Inverted', frame_2)

        # press `q` to exit
        if cv2.waitKey(27) & 0xFF == ord('q'):
            break
    # if no frame found
    else:
        break
# release VideoCapture()
cap.release()
# close all frames and video windows
cv2.destroyAllWindows()




