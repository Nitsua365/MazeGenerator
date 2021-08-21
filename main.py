import cv2
from numpy import ndarray


def main():

    nodeWidthInput = int(input("enter node width: "))
    nodeHeightInput = int(input("enter node height: "))

    buffer = ndarray(shape=(nodeHeightInput, nodeWidthInput, 3), dtype=int)

    for i in range(0, len(buffer)):
        for j in range(0, len(buffer[i])):
            buffer[i][j] = [0, 0, 0]

    cv2.imwrite("out.png", buffer)


if __name__ == '__main__':
    main()

