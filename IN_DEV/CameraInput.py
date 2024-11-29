import cv2 as cv
import AdvancedUI as aui

camera = cv.VideoCapture(1)
cv.namedWindow("CameraTest")


# Тест Камеры
def CameraTest():
    while True:
        ret, image = camera.read() # Читаем камеру
        
        if not ret:
            print("ОШИБКА: Камера не распознана")
            break

        cv.imshow("CameraTest", image)

        cv.waitKey(0)

# Захват Image с камеры
def CameraCapture():
    ret, image = camera.read()
    if not ret:
        print("ОШИБКА: Камера не распознана.")
        raise RuntimeWarning("Camera")

    return ImageProcess(image)


# Постобработка Image
def ImageProcess(sorceImage):
    brightness = -10
    contrast = 1.2

    sorceImage = cv.cvtColor(sorceImage, cv.COLOR_RGB2HSV)  
    return cv.addWeighted(sorceImage, contrast, 0, brightness, 0) 


aui.ShowImage(CameraCapture())

camera.release() # Запускаем камеру (?)
cv.destroyAllWindows()