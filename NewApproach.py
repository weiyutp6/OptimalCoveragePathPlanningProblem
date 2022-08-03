import csv

import numpy as np
from scipy.io import savemat
import matplotlib.pyplot as plt

from OCPPP import Grid


def squareDistancePoints(a, b):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2


class SingleDir(Grid):
    def __init__(self, start=[], end=[], unpassable=[], csv_file=None, threshold=0, orientation="horizontal"):
        super().__init__(start, end, unpassable, csv_file, threshold)
        self.h_lines = []
        self.v_lines = []
        self.orientation = orientation
        self.cost = []
        self.section = []

    def createLineSegment(self):
        for i in range(self.start[0], self.end[0] + 1):
            line = [[i, 0]]
            for j in range(self.start[1] + 1, self.end[1] + 1):
                if [i, j] not in self.unpassable:
                    if [i, j + 1] in self.unpassable or j == self.end[1]:
                        line.append([i, j])
                        self.h_lines.append(line)
                    if [i, j - 1] in self.unpassable:
                        line = [[i, j]]
                    if [i, j + 1] in self.unpassable and [i, j - 1] in self.unpassable:
                        self.h_lines.append([[i, j], [i, j]])

        for i in range(self.start[1], self.end[1] + 1):
            line = [[0, i]]
            for j in range(self.start[0] + 1, self.end[0] + 1):
                if [j, i] not in self.unpassable:
                    if [j + 1, i] in self.unpassable or j == self.end[0]:
                        line.append([j, i])
                        self.v_lines.append(line)
                    if [j - 1, i] in self.unpassable:
                        line = [[j, i]]
                    if [j + 1, i] in self.unpassable and [j - 1, i] in self.unpassable:
                        self.v_lines.append([[j, i], [j, i]])
        # for i in self.v_lines:
        #     print(i)

    def defineGTSPCost(self):
        if self.orientation == "horizontal":
            target_lines = self.h_lines
        else:
            target_lines = self.v_lines
        for i in target_lines:
            self.gtsp_set.append(i)
            self.gtsp_set.append([i[-1], i[0]])
        for i in self.gtsp_set:
            row = []
            for j in self.gtsp_set:
                row.append(squareDistancePoints(i[1], j[0])*20)
            print(row)
            self.cost.append(row)
        # mat = np.matrix(self.cost)
        # np.savetxt('edge_weight_section.txt', mat, fmt='%d')
        for i in range(1, int(len(self.cost) / 2) + 1):
            row = [i, 2 * i - 1, 2 * i, -1]
            self.section.append(row)
        # mat = np.matrix(self.section)
        # np.savetxt('set_section.txt', mat, fmt='%d')


obj = SingleDir(csv_file="20220728DredgerMap_Gaussain_1.csv", threshold=0)
obj.createLineSegment()
obj.defineGTSPCost()
obj.createGTSPFile()
