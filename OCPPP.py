# -*- coding: utf-8 -*-
"""
Created on May 24 2021

@author: Wei-Yu Chen
#Purpose: Calculate NAI matrix for matlab LP solver then plot the result from the LP solver
#Ref:
@INPROCEEDINGS{7743548,
  author={Bochkarev, Stanislav and Smith, Stephen L.},
  booktitle={2016 IEEE International Conference on Automation Science and Engineering (CASE)},
  title={On minimizing turns in robot coverage path planning},
  year={2016},
  volume={},
  number={},
  pages={1237-1242},
  doi={10.1109/COASE.2016.7743548}}
@misc{https://doi.org/10.48550/arxiv.2109.08185,
  doi = {10.48550/ARXIV.2109.08185},
  url = {https://arxiv.org/abs/2109.08185},
  author = {Ramesh, Megnath and Imeson, Frank and Fidan, Baris and Smith, Stephen L.},
  title = {Optimal Partitioning of Non-Convex Environments for Minimum Turn Coverage Planning},
  publisher = {arXiv},
  year = {2021},
  copyright = {arXiv.org perpetual, non-exclusive license}}

"""
import csv

import numpy as np
from scipy.io import savemat
import matplotlib.pyplot as plt


# right first then down
class Grid:
    def __init__(self, start, end, unpassable):
        self.squares = []
        self.grid_num = (end[1] - start[1] + 1) * (end[0] - start[0] + 1) - len(unpassable)
        self.naiH = []
        self.naiV = []

    # generate NAI matrix for horizontal and vertical graph
    def findNAI(self):
        counter = 0
        for i in range(start[0], end[0] + 1):
            for j in range(start[1], end[1] + 1):
                if [i, j] not in unpassable:
                    point = Square([i, j], end, unpassable, counter)
                    self.squares.append(point)
                    naiH_row = []
                    naiV_row = []
                    for k in range(self.grid_num):
                        if point.right:
                            if counter == k:
                                naiH_row.append(1)
                            else:
                                naiH_row.append(0)
                        else:
                            naiH_row.append(0)
                        if point.down:
                            if counter == k:
                                naiV_row.append(1)
                            else:
                                naiV_row.append(0)
                        else:
                            naiV_row.append(0)
                    counter += 1
                    self.naiH.append(naiH_row)
                    self.naiV.append(naiV_row)

    # export matrix as matlab .mat file
    def exportArrays(self):
        nai = dict()
        nai['NAIH'] = np.array(self.naiH)
        nai['NAIV'] = np.array(self.naiV)
        savemat('NAI.mat', nai)

    # plot a scatter plot from matlab generated results xh.csv
    def plot_csv(self, file):
        f = open(file)
        mat = csv.reader(f)
        xh = []
        connection = []
        plt.gca().invert_yaxis()
        for i in mat:
            for j in i:
                xh.append(int(j))
        for i in self.squares:
            if xh[i.number]:
                connection.append([[i.coord[0], i.coord[0] + 1], [i.coord[1], i.coord[1]]])
            else:
                connection.append([[i.coord[0], i.coord[0]], [i.coord[1], i.coord[1] + 1]])
        for i in connection:
            plt.plot(i[1], i[0], color='r')
            plt.scatter(i[1], i[0], color='b')
        plt.show()


class Square:
    def __init__(self, coord, end, unpassable, number):
        self.coord = coord
        self.number = number
        self.right = None
        self.down = None
        self.orientation = 1
        self.connection_num = 0
        if self.coord[0] + 1 <= end[0] and ([self.coord[0] + 1, self.coord[1]]) not in unpassable:
            self.down = [self.coord[0] + 1, self.coord[1]]
        if self.coord[1] + 1 <= end[1] and ([self.coord[0], self.coord[1] + 1]) not in unpassable:
            self.right = [self.coord[0], self.coord[1] + 1]


start = [0, 0]
end = [9, 9]
unpassable = [[1, 4], [2, 4], [3, 4], [1, 5], [2, 5], [3, 5], [5, 7], [5, 8], [6, 7], [6, 8]]
# unpassable = [[5, 7], [5, 8], [6, 7], [6, 8]]
mode = 0
g = Grid(start, end, unpassable)
if mode:
    g.findNAI()
    g.exportArrays()
else:
    g.findNAI()
    g.plot_csv('xh.csv')
