#!/usr/bin/env python3
# Author @ Kartikeya Mishra

from dataclasses import dataclass

@dataclass
class CONSTANT:
    START_COORDINATES = (0, 0)
    END_COORDINATES = (400, 250)
    
    CANVAS_WIDTH = 400
    CANVAS_HEIGHT = 250
    
    
    # Internal Constants
    
    ORIGIN_POINT_OFFSET = CANVAS_HEIGHT