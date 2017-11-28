"""
Author: Connor Sean Rodgers
Class: Spawn Points
"""
"""
========================================================================================================================
Spawn Point Class

boolPointOccupied: Variable to track if the individual spawn point is occupied or not

========================================================================================================================
"""
class spawnPoint():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.boolPointOccupied = False
