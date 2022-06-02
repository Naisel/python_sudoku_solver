import numpy as np

grid = [[4, 0, 5, 0, 0, 2, 3, 0, 8],
        [0, 6, 0, 1, 8, 0, 4, 0, 9],
        [9, 0, 8, 3, 7, 0, 5, 0, 1],
        [0, 0, 0, 4, 9, 6, 0, 0, 0],
        [3, 9, 6, 0, 1, 0, 7, 0, 5],
        [0, 8, 0, 0, 0, 0, 1, 0, 6],
        [5, 4, 9, 0, 0, 0, 0, 0, 3],
        [0, 0, 0, 0, 4, 9, 2, 5, 0],
        [0, 0, 2, 0, 3, 0, 0, 0, 0]]


def possible(row, coloum, number):
    global grid

    #for checking possibility in rows
    for i in range(0, 9):
        if grid[i][coloum] == number:
            return False

    #for checking possibility in coloums
    for i in range(0, 9):
        if grid[row][i] == number:
            return False


    #for checking possibility in 3-3 matrix
    x0 = (row // 3)*3
    y0 = (coloum // 3)*3
    for i in range(0, 3):
        for j in range(0, 3):
            if grid[x0+i][y0+j] == number:
                return False

    return True



def solve():
    global grid

    for row in range(0, 9):
        for coloum in range(0, 9):
            if grid[row][coloum] == 0:
                for number in range(1, 10):
                    if possible(row, coloum, number):
                        grid[row][coloum] = number
                        solve()
                        grid[row][coloum] = 0
                return
    print(np.matrix(grid))
    input("press enter for more solution")

solve()