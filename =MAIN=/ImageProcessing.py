import cv2 as cv
import numpy as np
from abc import ABC, abstractmethod


class LineStrategy(ABC):
    @abstractmethod
    def findPointsOfLine(self):
        pass

    def addWeights(self, edges):
        return cv.erode(cv.dilate(edges, None), None)


class HoughLine(LineStrategy):
    def findPointsOfLine(self, mask):
        edges = cv.Canny(mask, 50, 200)
        edges = self.addWeights(edges) #!!!
        print(edges)
        lines = cv.HoughLinesP(edges, rho=1, theta=np.pi/180, threshold=20, minLineLength=10, maxLineGap=8)
        print(lines)

        for i in range(0, len(lines)):
            l = lines[i][0]
            cv.line(mask, (l[0], l[1]), (l[2], l[3]), (255, 10, 150),
                    thickness=1,
                    lineType=cv.LINE_AA)
        cv.imshow("LINES", mask)
        cv.waitKey(0)

        return lines


class ImageProcessor:
    strategy = HoughLine()

    def __init__(self, line, robot, led):
        self.lineL, self.lineU = line
        self.robotL, self.robotU = robot
        self.ledL, self.ledU = led


    def getMask(self, img):
        print(self.lineL)
        print(self.lineU)
        mask = cv.inRange(img, self.lineL, self.lineU)
        cv.imshow("MASK", mask)
        cv.waitKey(0)
        cv.imshow("IMG", img)
        cv.waitKey(0)

    def rotateImage(self, img, rounds):
        for i in range(rounds):
            img = cv.rotate(img, cv.ROTATE_90_CLOCKWISE)
        return img

    def findRobot(self, img):
        robotC = self.findCenter(img, self.robotL, self.robotU)
        robotF = self.findCenter(img, self.ledL, self.ledU)

        return robotC, robotF

    def findCenter(self, img, low, up):
        mask = cv.inRange(img, low, up)

        center = [ np.average(i) for i in np.where(mask >= 255) ]

        return center


    def findLines(self, img):
        mask = self.getMask(img)
        return self.strategy.findPointsOfLine(mask)
# class HoughTransform:
#     def hough_lines(self, edges):
#         lines = cv.HoughLinesP(edges, rho=1, theta=np.pi/180, threshold=20, minLineLength=10, maxLineGap=5)
#         if lines is not None:
#             return lines
#         return None

# class CannyEdgeDetection:
#     def canny_edge_detection(self, mask):
#         edges = cv.Canny(mask, 50, 200)
#         return edges