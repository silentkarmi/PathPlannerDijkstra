#!/usr/bin/env python3
# Author @ Kartikeya Mishra

import cv2
from traversal import Traversal
from node import Node
import time

if __name__ == "__main__":
    
    while (1):
        startXCoord = 5 #int(input("\nStart X Coordinate:"))
        startYCoord = 5 #int(input("Start Y Coordinate:"))
        
        startCoord = (startXCoord, startYCoord) 
        objTraversal = Traversal()
        objTraversal.startNode = Node(startCoord, None)
        # if Node.isCoordValid(startCoord) and \
        #     objTraversal.canvaArea.isOutsideObstacleSpace(objTraversal.startNode):
                
        endXCoord = 395 #int(input("End X Coordinate:"))
        endYCoord = 245 #int(input("End Y Coordinate:"))
    
        endCoord = (endXCoord, endYCoord)
        objTraversal.endNode = Node(endCoord, None)
        
        # if Node.isCoordValid(endCoord) and \
        # objTraversal.canvaArea.isOutsideObstacleSpace(objTraversal.endNode):
        
        start_time = time.time()
        objTraversal.canvaArea.drawObstacles()
        objTraversal.createNodeTree()
        objTraversal.backTrack()
        objTraversal.drawSolution()
        print("--- %s seconds for finding and drawing the solution ---" % (time.time() - start_time))
        cv2.waitKey(0)
        quit()
        #     else:
        #         print("Invalid End Coordinates. Try Again.\n")
        # else:
        #     print("Invalid Start Coordinates. Try Again.\n")
    
    
    
    
