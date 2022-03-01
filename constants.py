#!/usr/bin/env python3
# Author @ Kartikeya Mishra

from curses import COLOR_WHITE
from dataclasses import dataclass

@dataclass
class CONSTANT:
    START_COORDINATES = (10, 10)
    END_COORDINATES = (50, 50)
    
    CANVAS_WIDTH = 400
    CANVAS_HEIGHT = 250
    
    CLEARANCE = 5 #5mm
    
    WINDOW_NAME = "Path_Planner"
  
        
    # Internal Constants
    
    ORIGIN_POINT_OFFSET = CANVAS_HEIGHT
    COLOR_RED = (0,0,255)
    COLOR_GREEN = (0, 255, 0)
    COLOR_BLUE = (255, 0, 0)
    COLOR_WHITE = (255, 255, 255)