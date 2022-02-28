#!/usr/bin/env python3
# Author @ Kartikeya Mishra

import cv2
import heapq
from dataclasses import dataclass

from constants import CONSTANT
from canvas import Canvas
from node import Node
from obstacles.circleObstacle import CircleObstacle

@dataclass
class Traversal:
    _openList: list()
    _closedList: list()
    _listSolution: list()
    
    def __init__(self):
        self.canvaArea = Canvas()
        
        objCircle = CircleObstacle((300, 185), 40)
        self.canvaArea.addObstacle(objCircle)
        
        self.canvaArea.drawObstacles()
        
        self.startNode = None
        self.endNode = None
        self.solutionNode = None
        
    def expandNodesAndPushIntoWorkspace(self, node):
        listNodes = node.createNodes()
        for subNode in listNodes:
            self.pushNode(subNode)       

   
    def pushNode(self, node):
        if node != None:
            isNodeSafe = self.canvaArea.isOutsideObstacleSpace(node)
            
            if isNodeSafe:
                isNodeInClosedList = self.isNodeInClosedList(node)
                if not isNodeInClosedList:
                    nodeInWorkspace = self.isNodeInOpenListThenUpdate(node)
                    if not nodeInWorkspace:
                        # push it to the top of the list
                        # print(node.coord," ",node.cost2come)
                        heapq.heappush(self._openList, node)
    
    # checks if the node is visted otherwise resolve it  
    def isNodeInClosedList(self, node):
        isClosed = False
        if isinstance(node, Node):
            for tempNode in self._closedList:
                if tempNode.coord == node.coord:
                    isClosed = True 
                    break
                    
        return isClosed
    
    def isNodeInOpenListThenUpdate(self, node):
        isInOpenList = False
        if isinstance(node, Node):
            for tempNode in self._openList:
                if tempNode.coord == node.coord:
                    if node.cost2come < tempNode.cost2come:
                        tempNode = node
                        
                    isInOpenList = True 
                    break
                    
        return isInOpenList
                
    def isThisGoalNode(self, nodeToCheck):
        return nodeToCheck.coord == self.endNode.coord
    
    def createNodeTree(self):
        self._openList = []
        self._closedList = []
        
        self.pushNode(self.startNode)
        lastPercent = 0 
        
        while(self._openList):
            
            # pops an element from the top of the list
            tempNode = heapq.heappop(self._openList)     
            self._closedList.append(tempNode)  
            self.canvaArea.drawNode(tempNode)
            
            cv2.waitKey(1)
             
            if(self.isThisGoalNode(tempNode)):
                self.solutionNode = tempNode
                break
            
            self.expandNodesAndPushIntoWorkspace(tempNode)
            
        else:
            print("SOLUTION NOT FOUND")
            
    def backTrack(self):
        self._listSolution = []
        tempNode = self.solutionNode
        while tempNode != None:
            self._listSolution.append(tempNode)
            tempNode = tempNode.parentNode
            
    def drawSolution(self):
        for node in self._listSolution[::-1]:
            self.canvaArea.drawNode(node, CONSTANT.COLOR_GREEN)