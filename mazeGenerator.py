from numpy import ndarray
from random import randint
import cv2

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

        for i in range(0, len(self.buffer)):
            for j in range(0, len(self.buffer[i])):
                self.buffer[i][j] = [0, 0, 0]

        nodeWidthCount = self.wallWidth
        while nodeWidthCount < self.buffer.shape[0]:

            nodeHeightCount = self.wallWidth

            while nodeHeightCount < self.buffer.shape[1]:

                self.adjList.append([nodeWidthCount, nodeHeightCount])


                nodeHeightCount += self.nodeDimension + self.wallWidth


            nodeWidthCount += self.nodeDimension + self.wallWidth

        print(self.buffer.shape)
        print(self.adjList)

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
        print("DFS")


    def __DFS(self):
        print("DFS")



    def __addEdge(self, coord1, coord2):
        print("addedge")


    def writeMaze(self, fileName):

        hasPng = fileName.endswith(".png") or fileName.endswith(".PNG")

        if not hasPng:
            fileName += ".png"

        cv2.imwrite(fileName, self.buffer)

