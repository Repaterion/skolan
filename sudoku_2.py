'''
En Sudokulösare i python vilken skall läsa in en fil och tolka datan som en 
uppsättning för pusslet.
'''
import sys
from pprint import pprint
#import csv #ANVÄNDSINTE FÖR NÄRVARANDE

puzzleChart = ""
puzzleChartDone = []
intPuzzleChart = ""

#WITH GARANTERAR ATT FILEN STÄNGS.
with open("pussel_zero.csv", 'r') as puzzleChart:
    print(puzzleChart.readlines())

#puzzleChart = sys.argv #För att kunna skriva filen som skall öppnas direkt efter programnet
#puzzleChart = open("pussel_zero.csv")
#print_sudoku = puzzleChart[1]
#print(print_sudoku)
strPuzzleChart = str(puzzleChart)
print(strPuzzleChart)
#for line in puzzleChart:
 #   print (line)




#puzzleChartDone = strPuzzleChart.append([int(i) for i in intPuzzleChart.replace('\n','').split(',')])   #Appendar en städad lista till board.
#intPuzzleChart = [int(x) for x in puzzleChart]
#puzzleChartSTR = str(puzzleChart)

#with open(strPuzzleChart) as csv_file:
#    intPuzzleChart.append = csv.reader(csv_file, delimiter=',')




#DEFINETIONER
#Hitta nästa tomma rad eller kollumn 
def findNextEmpty(pussel):
    for r in range(9):
        for c in range(9):
            if pussel[r][c] == 0:  #Var tidigrae -1
                return r, c
    return None, None


def sudoku_solver(pussel):
    #Lösa Sodoku via "backtracking
    row, col = findNextEmpty(pussel)
    if row is None:
        return True

    for guess in range (1,10):
        #Steg 3 Kontrollerar om siffran är rätt.
        if is_valid (pussel, guess, row, col):
            #Om sann, placera denne inom rutan
            pussel[row][col] = guess

            if sudoku_solver(pussel):
                return True
        pussel[row][col] = 0
    return

# Räknar ut om oven gissning var korrekt eller ej, returnerar True eller False utifrån svaret.
def is_valid(pussel, row, col,):
    row_values = pussel[row]
    if guess in row_values:
        return False

    col_value = pussel[col]
    for i in range(9):
        col_value.append(pussel[i][col])
    #col_value = [pussel[i][col] for i in range(9)]
    if guess in col_value:
        return False

    # Leta var i 3X3 rutan vi befinner oss.
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3
    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start +3):
            if pussel [r][c] == guess:
                return False
    return True

#Här nedan skall resultatet skrivas ut direkt i terminalen och som en .csv fil.
if __name__ == '__main__':
    intPuzzleChart2 = [intPuzzleChart]
    print(sudoku_solver(intPuzzleChart))
    #pprint(intPuzzleChart)
    #SKRIVA UT TILL EN CSV-FIL

#STÄNGER FILEN 
puzzleChart.close()