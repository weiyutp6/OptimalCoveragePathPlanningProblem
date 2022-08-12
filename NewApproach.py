import argparse
import yaml

from scipy.io import savemat

from OCPPP import Grid


def rowDist(a, b):
    return abs(a[0] - b[0])


def columnDist(a, b):
    return abs(a[1] - b[1])


def lineDirection(a, b):
    dirA = a[1][1] - a[0][1]
    dirB = b[1][1] - b[0][1]
    if dirA * dirB > 0:
        return 1
    else:
        return 0


class SingleDir(Grid):
    def __init__(self, start=[], end=[], unpassable=[], csv_file=None, threshold=0):
        super().__init__(start, end, unpassable, csv_file, threshold)
        self.h_lines = []
        self.cost = []
        self.section = []

    def createLineSegment(self):
        full_lines = []
        for i in range(self.start[0], self.end[0] + 1):
            line = []
            for j in range(self.start[1] + 1, self.end[1] + 1):
                if [i, j] not in self.unpassable:
                    line.append([i, j])
                elif line:
                    if [i, j] in self.unpassable or j == self.end[1]:
                        full_lines.append(line)
                        line = []
        for i in full_lines:
            self.h_lines.append([i[0], i[-1]])
                        
        # for i in self.h_lines:
        #     print(i)

    def costFunc(self, i, j):
        row_cost = (rowDist(self.start, self.end) - rowDist(i[1], j[0]))  * 10
        column_cost = 10 * lineDirection(i, j)
        return row_cost + column_cost

    def defineGTSPCost(self):
        target_lines = self.h_lines
        output = dict()
        counter = 0
        for i in target_lines:
            self.gtsp_set.append(i)
            self.gtsp_set.append([i[-1], i[0]])
            counter += 1
            output[str(counter)] = self.gtsp_set[-1]
            counter += 1
            output[str(counter)] = self.gtsp_set[-2]
        savemat('line_segment.mat', output)
        for i in self.gtsp_set:
            row = []
            for j in self.gtsp_set:
                # for horizontal orientation reward rows that are far apart but encourage columns that are close
                row.append(self.costFunc(i, j))
            # print(row)
            self.cost.append(row)
        for i in range(1, int(len(self.cost) / 2) + 1):
            row = [i, 2 * i - 1, 2 * i, -1]
            self.section.append(row)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--printSeq")
    parser.add_argument("--csvFile")
    parser.add_argument("--tourFile")
    args = parser.parse_args()

    printSeq = 0
    if args.printSeq:
        printSeq = args.printSeq
    csvFile = ""
    if args.csvFile:
        csvFile = args.csvFile

    with open('param.yaml', 'r') as file:
        param = yaml.safe_load(file)

    obj = SingleDir(csv_file=csvFile, threshold=param["threshold"])
    obj.createLineSegment()
    obj.defineGTSPCost()
    obj.createGTSPFile(csvFile.replace(".csv", "") + "linear")
    if printSeq:
        obj.printSeq("GLKH-1.1/" + "linear" + csvFile + ".*.tour")
