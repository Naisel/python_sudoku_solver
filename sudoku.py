import numpy as np

temp = ["405002308",
        "060180409",
        "908370501", 
        "000496000",
        "396010705",
        "080000106",
        "549000003",
        "000049250",
        "002030000"]

grid = list(map(list, temp))
for i in range(0,9):
    grid[i] = list(map(int, grid[i]))
print(np.matrix(grid))


# def possible(row, coloum, number):
#     global grid

#     #for checking possibility in rows
#     for i in range(0, 9):
#         if grid[i][coloum] == number:
#             return False

#     #for checking possibility in coloums
#     for i in range(0, 9):
#         if grid[row][i] == number:
#             return False


#     #for checking possibility in 3-3 matrix
#     x0 = (row // 3)*3
#     y0 = (coloum // 3)*3
#     for i in range(0, 3):
#         for j in range(0, 3):
#             if grid[x0+i][y0+j] == number:
#                 return False

#     return True



# def solve():
#     global grid

#     for row in range(0, 9):
#         for coloum in range(0, 9):
#             if grid[row][coloum] == 0:
#                 for number in range(1, 10):
#                     if possible(row, coloum, number):
#                         grid[row][coloum] = number
#                         solve()
#                         grid[row][coloum] = 0
#                 return
#     print(np.matrix(grid))
#     input("press enter for more solution")

# solve()