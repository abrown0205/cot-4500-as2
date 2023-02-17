import numpy as np


def nevillesMethod(xPoints, yPoints, x):
    matrix = np.zeros((len(xPoints), len(yPoints)))
    for i in range(len(xPoints)):
        matrix[i][0] = yPoints[i]

    for i in range(1, len(xPoints)):
        for j in range(1, i+1):
            term1 = (x - xPoints[i-j]) * matrix[i][j-1]
            term2 = (x - xPoints[i]) * matrix[i-1][j-1]

            denom = xPoints[i] - xPoints[i-j]

            matrix[i][j] = (term1 - term2) / denom

    return matrix


def newtonsForwardMethod(xPoints, yPoints):
    length = len(xPoints)
    matrix = np.zeros((length, length))

    for i in range(length):
        matrix[i][0] = yPoints[i]

    for i in range(1, length):
        for j in range(1, i+1):
            num = matrix[i][j-1] - matrix[i-1][j-1]
            denom = xPoints[i] - xPoints[i-j]
            matrix[i][j] = num / denom

    return matrix

def getApproxResult(matrix, xPoints, val):
    reoccuringXSpan = 1
    reoccuringPxResult = matrix[0][0]

    for i in range(1, len(xPoints)):
        coefficient = matrix[i][i]
        reoccuringXSpan *= (val - xPoints[i-1])
        mult = coefficient * reoccuringXSpan
        reoccuringPxResult += mult

    return reoccuringPxResult

def applyDivDif(matrix):
    size = len(matrix)
    for i in range(2, size):
        for j in range(2, i+2):
            if j >= len(matrix[i]) or matrix[i][j] != 0:
                continue

            left = matrix[i][j-1]
            diagLeft = matrix[i-1][j-1]

            num = left - diagLeft
            if (i == 4 and j == 4) or (j == 5):
                denom = matrix[i][0] - matrix[0][0]
            else:
                denom = matrix[i][0] - matrix[i-2][0]


            matrix[i][j] = num / denom
    return matrix

def hermiteInterpolation(xPoints, yPoints, derivs):
    numPoints = len(xPoints)
    matrix = np.zeros((2*numPoints, numPoints+3))

    counter = 0
    for i in range(0, 2*numPoints, 2):
        matrix[i][0] = xPoints[counter]
        matrix[i+1][0] = xPoints[counter]
        counter += 1

    counter = 0
    for i in range(0, 2*numPoints, 2):
        matrix[i][1] = yPoints[counter]
        matrix[i+1][1] = yPoints[counter]
        counter += 1

    counter = 0
    for i in range(1, 2*numPoints, 2):
        matrix[i][2] = derivs[counter]
        counter += 1

    return applyDivDif(matrix)

def cubicSplineInterpolation():


if __name__ == "__main__":
    np.set_printoptions(precision=7, suppress=True, linewidth=100)

    # Question 1
    xPoints = [3.6,   3.8,   3.9]
    yPoints = [1.675, 1.436, 1.318]
    approx = 3.7

    val1 = nevillesMethod(xPoints, yPoints, approx)[len(xPoints)-1][len(yPoints)-1]
    print(val1)
    print()

    # Question 2
    xPoints = [7.2, 7.4, 7.5, 7.6]
    yPoints = [23.5492, 25.3913, 26.8224, 27.4589]

    matrix2 = newtonsForwardMethod(xPoints, yPoints)
    print("[", end="")
    for i in range(1, len(xPoints)):
        if i != len(xPoints)-1:
            print(matrix2[i][i], end=", ")
        else:
            print(matrix2[i][i], end="]\n")
    print()


    # Question 3
    approx = 7.3
    print(getApproxResult(matrix2, xPoints, approx))
    print()

    # Question 4
    xPoints = [3.6, 3.8, 3.9]
    yPoints = [1.675, 1.436, 1.318]
    derivs  = [-1.195, -1.188, -1.182]
    print(hermiteInterpolation(xPoints, yPoints, derivs))
    print()

    # Question 5
    xPoints = [2, 5, 8, 10]
    yPoints = [3, 5, 7, 9]
