import cv2 as cv
#import numpy as np
import os
from InitConfig import *
from RobotCommunicate import NetControl as nc
from CameraInput import CaptureImage as ci


os.system("cls")
print("Проект для En+ 24/25. Версия: " + version)

if(input() == "0"):
    quit("Завершение работы программы...")

cv.namedWindow(windowName, cv.WINDOW_NORMAL)
cv.imshow(windowName, ci.GetImage())
cv.waitKey(0)
cv.destroyAllWindows()

nc.MoveForward()