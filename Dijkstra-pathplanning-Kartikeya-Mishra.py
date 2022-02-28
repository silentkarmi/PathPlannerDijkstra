#!/usr/bin/env python3
# Author @ Kartikeya Mishra

import cv2
from traversal import Traversal
from node import Node


if __name__ == "__main__":
    
    while (1):
        startXCoord = int(input("\nStart X Coordinate:"))
        startYCoord = int(input("Start Y Coordinate:"))
        
        startCoord = (startXCoord, startYCoord) 
        objTraversal = Traversal()
        objTraversal.startNode = Node(startCoord, None)
        if Node.isCoordValid(startCoord) and \
            objTraversal.canvaArea.isOutsideObstacleSpace(objTraversal.startNode):
                
            endXCoord = int(input("End X Coordinate:"))
            endYCoord = int(input("End Y Coordinate:"))
        
            endCoord = (endXCoord, endYCoord)
            objTraversal.endNode = Node(endCoord, None)
            
            if Node.isCoordValid(endCoord) and \
            objTraversal.canvaArea.isOutsideObstacleSpace(objTraversal.endNode):
                objTraversal.createNodeTree()
                objTraversal.backTrack()
                objTraversal.drawSolution()
                cv2.waitKey(0)
                quit()
            else:
                print("Invalid End Coordinates. Try Again.\n")
        else:
            print("Invalid Start Coordinates. Try Again.\n")
    
    
    
    
