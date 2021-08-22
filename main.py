
from mazeGenerator import MazeGenerator

def main():

    mazeNodeWidthInput = int(input("enter node width: "))
    mazeNodeHeightInput = int(input("enter node height: "))
    mazeWallWidth = int(input("enter wall width: "))
    mazeNodeSize = int(input("enter maze node size: "))
    mazeOutputFileName = input("enter output file name: ")

    mazeGen = MazeGenerator(mazeNodeWidthInput, mazeNodeHeightInput, mazeWallWidth, mazeNodeSize)

    mazeGen.writeMaze(mazeOutputFileName)


if __name__ == '__main__':
    main()

