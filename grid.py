from random import random
from enum import Flag, auto

#import logging

#logging.basicConfig(level=logging.INFO)
land,water = "Land","Water"

class Grid:
    grid = []
    def __init__(self,rows,columns):
        assert rows>8
        assert columns>8
        row = [Cell() for i in range(rows)]
        self.grid.append(list(row) for j in range(columns))
    def print(self):
        for cell in self.grid:
            type = ("L" if self.cell.type == land else "W")+" "
            print()

class Facilities(Flag):
    Factory = auto()
    Port = auto()
    HQ = 0o10

class Cell:
    def __init__(self):
        self.type = land if random() < 0.6 else water
        self.number_of_units = 0
        self.facilities = 0

g = Grid(9,9)
g.print()