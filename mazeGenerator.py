from numpy import ndarray
from random import randint
import cv2

class MazeNode:
    def __init__(self, coordinate, index):
        self.coordinate = coordinate
        self.index = index


    def __eq__(self, other):
        return self.coordinate[0] == other.coordinate[0] and \
               self.coordinate[1] == other.coordinate[1]

    def __str__(self):
        return "coordinate: (x: " + str(self.coordinate[0]) + ", y: " + str(self.coordinate[1]) + ") index: " + str(
            self.index)

    def __getitem__(self, item):
        if 2 > item >= 0:
            return self.coordinate[item]
        else:
            assert False

    def __hash__(self):
        return hash(str(self))

class MazeGenerator:
    def __init__(self, mazeWidth, mazeHeight, wallWidth, nodeDim):
        self.mazeNodeWidth = mazeWidth
        self.mazeNodeHeight = mazeHeight
        self.wallWidth = wallWidth
        self.nodeDimension = nodeDim
        self.buffer = ndarray(shape=((self.mazeNodeHeight * self.nodeDimension) + ((self.mazeNodeHeight + 1) * wallWidth), (self.mazeNodeWidth * self.nodeDimension) + ((self.mazeNodeWidth + 1) * wallWidth), 3), dtype=int)
        self.adjList = []
        self.startLoc = []
        self.endLoc = []
        self.searchStack = []
        self.visited = [False for i in range(0, len(self.adjList))]

        for i in range(0, len(self.buffer)):
            for j in range(0, len(self.buffer[i])):
                self.buffer[i][j] = [0, 0, 0]

        nodeWidthCount = self.wallWidth
        while nodeWidthCount < self.buffer.shape[0]:

            nodeHeightCount = self.wallWidth

            while nodeHeightCount < self.buffer.shape[1]:

                self.adjList.append(MazeNode([nodeWidthCount, nodeHeightCount], len(self.adjList)))

                nodeHeightCount += self.nodeDimension + self.wallWidth


            nodeWidthCount += self.nodeDimension + self.wallWidth

        # find start location
        start = end = 0

        for i in range(0, len(self.adjList)):
            if self.adjList[i][0] == self.wallWidth:
                start = i
                break

        for i in range(start, len(self.adjList)):
            if self.adjList[i][0] != self.wallWidth:
                end = i
                break

        self.startLoc = self.adjList[randint(start, end)]

        print(str(start) + " " + str(end))

        start = end = self.buffer.shape[0] - (self.nodeDimension + self.wallWidth)

        for i in range(0, len(self.adjList)):
            if self.adjList[i][0] == (self.buffer.shape[0] - (self.nodeDimension + self.wallWidth)):
                start = i
                break

        for i in range(start, len(self.adjList)):
            if self.adjList[i][0] != (self.buffer.shape[0] - (self.nodeDimension + self.wallWidth)):
                end = i
                break

        self.endLoc = self.adjList[randint(start, end)]

        print("start: " + str(self.startLoc))
        print("end: " + str(self.endLoc))


    def generateMaze(self):
        self.__DFS(self.startLoc)


    def __DFS(self, node):
        print("DFS")






    def __addEdge(self, coord1, coord2):
        print("addedge")


    def writeMaze(self, fileName):

        hasPng = fileName.endswith(".png") or fileName.endswith(".PNG")

        if not hasPng:
            fileName += ".png"

        cv2.imwrite(fileName, self.buffer)

