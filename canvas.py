import numpy as np
import cv2
from dataclasses import dataclass

from constants import CONSTANT
from node import Node
from utility import Utility


@dataclass
class Canvas:
    def __init__(self):
        # Create a black image
        self._canvasArea = np.zeros((CONSTANT.CANVAS_HEIGHT, CONSTANT.CANVAS_WIDTH, 3), np.uint8)
        self._obstacles = []
        
    def addObstacle(self, objObstacle):
        self._obstacles.append(objObstacle)
    
    def drawObstacles(self):
        for objObstacle in self._obstacles:
            objObstacle.draw(self._canvasArea)
        cv2.waitKey(1)
            
    def drawNode(self, node, color = CONSTANT.COLOR_WHITE):
        if isinstance(node, Node) and node.parentNode is not None:
            cv2.line(self._canvasArea , 
                     Utility.getCoordinatesInWorldFrame(node.parentNode.coord), 
                     Utility.getCoordinatesInWorldFrame(node.coord), 
                     color)
            cv2.imshow(CONSTANT.WINDOW_NAME, self._canvasArea)
            # cv2.waitKey(1)
            
    def isOutsideObstacleSpace(self, node):
        isValid = True
        for objObstacle in self._obstacles:
            isValid = objObstacle.isOutside(node.coord)
            if isValid == False:
                break
            
        return isValid
    
