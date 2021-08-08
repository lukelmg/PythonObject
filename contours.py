import cv2
import numpy as np
import time

cap = cv2.VideoCapture('flower2.mp4');

while True:
    time.sleep(0.025)
    _, frame = cap.read()
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    lower_blue = np.array([200,200,200])
    higher_blue = np.array([255, 255, 255])
    mask = cv2.inRange(rgb, lower_blue, higher_blue)

    cv2.imshow("Frame", frame)
    cv2.imshow("Mask", mask)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()