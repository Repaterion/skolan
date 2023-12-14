import csv
M = 9 
def puzzle(a):
    for i in range(M):
        for j in range(M):
            print(a[i][j],end = " ")
        print()
def solve(grid, row, col, num):
    for x in range(9):
        if grid[row][x] == num:
            return False
             
    for x in range(9):
        if grid[x][col] == num:
            return False
 
 
    startRow = row - row % 3
    startCol = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[i + startRow][j + startCol] == num:
                return False
    return True

def Suduko(grid, row, col):
 
    if (row == M - 1 and col == M):
        return True
    if col == M:
        row += 1
        col = 0
    if grid[row][col] > 0:
        return Suduko(grid, row, col + 1)
    for num in range(1, M + 1, 1): 
     
        if solve(grid, row, col, num):
         
            grid[row][col] = num
            if Suduko(grid, row, col + 1):
                return True
        grid[row][col] = 0
    return False
 
'''0 means the cells where no value is assigned'''

grid =[]
with open('pussel_zero.csv', newline='') as pussel:
     reader = csv.reader(pussel, delimiter=',')
     for row in reader:
        for i in range(len(row)):
            row[i]=int(row[i])#omvandla till int
        grid.append(row)
            




'''with open('sudukopuzzle.csv', 'r') as file:
    pussel=file.read()'''


'''grid = [[0, 5, 9, 7, 3, 2, 8, 6, 1],
        [6, 0, 1, 0, 0, 0, 0, 0, 3],
    [0, 8, 0, 6, 9, 1, 0, 7, 5],
    [0, 9, 7, 0, 2, 8, 5, 3, 0],
    [0, 6, 0, 1, 7, 0, 0, 0, 4],
    [0, 2, 4, 0, 5, 6, 7, 1, 0],
    [2, 0, 8, 9, 0, 4, 6, 0, 7],
    [0, 0, 0, 5, 8, 3, 0, 9, 0],
    [0, 0, 0, 0, 6, 7, 3, 4, 8]]
'''
 
if (Suduko(grid, 0, 0)):
    puzzle(grid)
else:
    print("Solution does not exist:(")
