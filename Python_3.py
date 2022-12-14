#Öppna filen för läsning och rensning. pf = puzzle_file. 'r' = read.
pf = open("pussel_zero.csv", 'r')
#Avläsning och omvandling till sträng.
pf_read = str(pf.readlines())
#print (pf_read.split(','))
intPuzzleChart = [int(x) for x in pf_read]
puzzle_string = ""


#Pusslets rutnät skapas här.
def form_grid(puzzle_string):
    global grid
    print('The Sudoku Problem')
    for i in range(0, len(puzzle_string), 9):
        row = puzzle_string[i:i+9]
        temp = []
        for block in row:
            temp.append(int(block))
        grid.append(temp)    
    printGrid()

    #Funktion för att skriva ut Sudokurutnätet detta sker genom itteration.
def printGrid():
    global grid
    for row in grid:
        print(row)

#Function to check if a digit can be placed in the given block
def possible(row,col,digit):
    global grid
    for i in range(0,9):
        if grid[row][i] == digit:
            return False
    for i in range(0,9):
        if grid[i][col] == digit:
            return False
    square_row = (row//3)*3
    square_col = (col//3)*3
    for i in range(0,3):
        for j in range(0,3):
            if grid[square_row+i][square_col+j] == digit:
                return False    
    return True

def solve():
    global grid
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                for digit in range(1,10):
                    if possible(row,col,digit):
                        grid[row][col] = digit
                        solve()
                        grid[row][col] = 0  #Backtrack step
                return
    print('\nThe Solution')
    printGrid()


    puzzle_string = "004300209005009001070060043006002087190007400050083000600000105003508690042910300"
grid = []
form_grid(puzzle_string)
solve()
