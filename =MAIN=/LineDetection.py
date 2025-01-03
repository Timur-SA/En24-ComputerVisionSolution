import numpy as np
import cv2 as cv

class HoughTransform:
    def hough_lines(self, edges):
        lines = cv.HoughLinesP(edges, rho=1, theta=np.pi/180, threshold=20, minLineLength=10, maxLineGap=5)
        if lines is not None:
            return lines
        return None
    
class CannyEdgeDetection:
    def canny_edge_detection(self, mask):
        edges = cv.Canny(mask, 50, 200)
        return edges