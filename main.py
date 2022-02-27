#!/usr/bin/env python3
# Author @ Kartikeya Mishra

from constants import CONSTANT
from canvas import Canvas

import cv2

from obstacles.circleObstacle import CircleObstacle

if __name__ == "__main__":

    canvaArea = Canvas()
    objCircle = CircleObstacle((300, 185), 40)
    canvaArea.addObstacle(objCircle)
    canvaArea.drawObstacles()
    print(objCircle.isOutside((260, 160)))
    print(objCircle.isOutside((263, 160)))
    cv2.waitKey(0)
