from ast import Constant
from time import sleep
import numpy as np
import cv2
from dataclasses import dataclass

from constants import CONSTANT

@dataclass
class Canvas:
    # Create a black image
    _EXIT_PROGRAM_KEYS = (27, 10, 32, 13, 141)
    
    def __init__(self):
        self._canvasArea = np.zeros((CONSTANT.CANVAS_HEIGHT, CONSTANT.CANVAS_WIDTH, 3), np.uint8)
        self._obstacles = []
        
    def addObstacle(self, objObstacle):
        self._obstacles.append(objObstacle)
    
    def drawObstacles(self):
        for objObstacle in self._obstacles:
            objObstacle.draw(self._canvasArea)
    
    def drawAnimatedLineTest(self):
        i = 0
        while (1):
            # press Escape or Space or Enter to exit
            k = cv2.waitKey(1) & 0xFF
            if k in Canvas._EXIT_PROGRAM_KEYS:
                break
            
            coordStart = self.getCoordinatesInWorldFrame((i, i))
            coordEnd = self.getCoordinatesInWorldFrame((i + 1, i + 1))
            cv2.line(self._canvasArea , coordStart, coordEnd, (0, 255, 0), 1)
            i += 1
            cv2.imshow(CONSTANT.WINDOW_NAME, self._canvasArea)

        cv2.destroyAllWindows()
    
