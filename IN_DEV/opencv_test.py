import cv2

NAME = "test2.png"

windowName = "Фото"
windowNameR = "R канал"
windowNameG = "G канал"

lowR = (0,0,180)
highR = (90,90,255)

lowG = (0,255,0)
highG = (200,255,200)

def readImage():
    return cv2.imread(NAME)

def viewImage(image, name_of_window):
    cv2.namedWindow(name_of_window, cv2.WINDOW_NORMAL)
    cv2.imshow(name_of_window, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def findRed(image):
    return cv2.inRange(image, lowR, highR)
def findGreen(image):
    return cv2.inRange(image, lowG, highG)


def oldFindObject():
    moments = cv2.moments(findGreen(readImage()), 1) # получим моменты 
    x_moment = moments['m01']
    y_moment = moments['m10']
    area = moments['m00']
    x = int(x_moment / area) # Получим координаты x,y 
    y = int(y_moment / area) # и выведем текст на изображение
    cv2.putText(image, "Red!", (x,y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)

    return image

def FindObject():
    image = readImage()
       
    M = cv2.moments(findGreen(readImage()))
    if M['m00'] != 0:
        x = int(M['m10']/M['m00'])
        y = int(M['m01']/M['m00'])
        cv2.putText(image, "CENTER!", (x-80, y),
        cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 0), 5)
    print(f"x: {x} y: {y}")
    return image

    
#MAIN
viewImage(readImage(), windowName)
viewImage(FindObject(), windowName)
viewImage(findRed(readImage()), windowName)
viewImage(findGreen(readImage()), windowName)

