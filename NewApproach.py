import csv

import numpy as np
from scipy.io import savemat
import matplotlib.pyplot as plt

from OCPPP import Grid

class SingleDir(Grid):
    def __init__(self):
        h_lines = []
        v_lines = []
    def createLineSegment(self):
        for i in range(self.start[0], self.end[0] + 1):
            line = [[i, 0]]
            endl = []
            for j in range(self.start[1], self.end[1] + 1):
                if [i,j] not in self.unpassable:

