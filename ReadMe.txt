# PathPlannerDijkstra
It uses Dijikstra's algorithm to find path given

>> When obstacle objects are drawn, they are inflated internally but not drawn on the screen.
>> Instead you will see the clearance of 5mm (= 5px in code) when nodes are traversed and see a gap.
>> Color Meaning
    - Red : obstacle
    - White : nodes traversed
    - Black : clearance from the boundary and the obstacles (in the end of traversal) / empty space
    - Green : Shortest path from start to end coordinates
>> Worst Condition of whole graph traversal can take upto 2 minutes

