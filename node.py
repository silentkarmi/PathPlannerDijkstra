#!/usr/bin/env python3
# Author @ Kartikeya Mishra

from dataclasses import dataclass

@dataclass
class Node:
    ACTION_SET = [(1,0), (-1,0), (0,1), (0,-1), (1,1), (-1,1), (1,-1), (-1,-1)]
    
    _coord: tuple()
    cost2come: 0
    
    @staticmethod
    def actionCost(coord):
        x, y = coord
        
        # if x and y are non-zero that means its a diagonal traversal
        if x and y:
            return 1.4
        else:
            return 1
    
    def __init__(self, coord, parent):
        self._coord = coord
        self.parentNode = parent
        
    def createNodes(self):
        nodes = []
        for action in Node.ACTION_SET:
            nodes.append(self._createNode(action))
            
        return nodes
    
    def _createNode(self, action):
        res = tuple(map(sum, zip(self._coord, action)))
        objNode = Node(res, self)
        return objNode
    