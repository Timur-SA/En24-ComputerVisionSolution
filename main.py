import cv2 as cv
import numpy as np
import os

from InitConfig import *


os.system("cls")
print("Проект для En+ 24/25. Версия: " + version)
print("Путь к исходному изображению: " + sourceImage)

if(input() == "0"):
    quit("Завершение работы программы...")

cv.namedWindow(windowName, cv.WINDOW_NORMAL)
cv.imshow(windowName, cv.imread(sourceImage))
cv.waitKey(0)
cv.destroyAllWindows()