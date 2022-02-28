import imp
from time import sleep
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
    
    # def drawAnimatedLineTest(self):
    #     i = 0
    #     while (1):
    #         # press Escape or Space or Enter to exit
    #         k = cv2.waitKey(1) & 0xFF
    #         if k in Canvas._EXIT_PROGRAM_KEYS:
    #             break
            
    #         coordStart = self.getCoordinatesInWorldFrame((i, i))
    #         coordEnd = self.getCoordinatesInWorldFrame((i + 1, i + 1))
    #         cv2.line(self._canvasArea , coordStart, coordEnd, (0, 255, 0), 1)
    #         i += 1
    #         cv2.imshow(CONSTANT.WINDOW_NAME, self._canvasArea)

    #     cv2.destroyAllWindows()
    
