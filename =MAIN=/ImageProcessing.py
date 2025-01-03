import cv2
import numpy as np
from LineDetection import HoughTransform
from LineDetection import CannyEdgeDetection

class ImageProcessor:
    def process(self, img, lineColors):
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, lineColors[0], lineColors[1])
        edges = CannyEdgeDetection().canny_edge_detection(mask)
        lines = HoughTransform().hough_lines(edges)
        if lines is not None:
            for line in lines:
                x1, y1, x2, y2 = line[0]
                angle = np.arctan2(y2 - y1, x2 - x1) * 180 / np.pi
                return angle
        return None