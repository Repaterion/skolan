## CSV är till för inläsning utav csv filen. 
## SYS är till för att anropa olika funktioner hos systemet (windows/linux),
##  i detta fall så används den till att läsa in pusselZero.csv som en "command-line (CL)" funktion.
import csv, sys
from time import sleep

## Efter inläsning via CL så lagras filens innehåll i variabeln filIn(fil In).
loaded_file = sys.argv[1]

## Nedan är enbart för det var roligt att skriva ut text i promtpen.
load = 'Loading system files....'
loaded = 'Files loaded: Starting calculations...'
finished = 'Calculations done: Results will be printed onto your terminal and as a file.'
cheers = 'Thank you for using this solver. =D'

m_len = len(load)
c_len = len(loaded)
f_len = len(finished)
h_len = len(cheers)


for m in range(m_len):
    print(load[m], end=' ', flush=True); sleep(0.1)
print('\n')
sleep(2)
for c in range(c_len):
    print(loaded[c], end=' ', flush=True); sleep(0.1)
print('\n')
sleep(0.5)
for f in range(f_len):
    print(finished[f], end=' ', flush=True); sleep(0.02)
print('\n')
sleep(0.5)

## Nedan är funktinonen från CSV biblioteket vilket förenklar inläsning av .csv filer.
##  innehållet lagras sedan i "board" vilket används för lösandet av pusslet.
board =[]
with open(loaded_file, newline='') as pussel:
     reader = csv.reader(pussel, delimiter=',')
     for row in reader:
        for i in range(len(row)):
            row[i]=int(row[i])  #omvandla till int
        board.append(row)

## Testutskrifter för att se om allt klaffar,
##  Dubbla nyradstecken för att skilja de olika delarna åt.
#print(board)
#print('\n\n')

##Funktionen för utskriften utav pussletslösning vilket sker via itteration genom två
##  for-loopar.
def printBoard(board):
    for i in range(0, 9):
        for j in range(0, 9):
            print(board[i][j], end=" ")        
        print()


##Här kontrolleras huruvida ett tal är True eller False och genom detta kan backtracking fungerar genom att
##  programmet testar sig fram genom siffrorna. Om det har kommit en bit genom programmet och det är fel en bit
##  upp så raderas alla tal upptill det felaktiga och ett nytt tal provas. Det är en form av "Brut Force".
def isPossible(board, row, col, val):
    for j in range(0, 9):
        if board[row][j] == val:
            return False

    for i in range(0, 9):
        if board[i][col] == val:
            return False

    startRow = (row // 3) * 3
    startCol = (col // 3) * 3
    for i in range(0, 3):
        for j in range(0, 3):
            if board[startRow+i][startCol+j] == val:
                return False
    return True


## solve - Lösningen här börjar den slutgiltiga kontrollen och lösniongen vilken sammarbetar med 
##  isPossible efter vilka tal som fungerar. När allt itterationen nåt "10" så vet den att nu är 
##  pusslet slut och backar skriver ut svaret både som fil och i promtpen.
##
def solve():
    for i in range(0, 9):
        for j in range(0, 9):
            if board[i][j] == 0:
                for val in range(1, 10):
                    if isPossible(board, i, j, val):
                        board[i][j] = val
                        solve()

                        # Vid felaktigt val, radera och gör om.
                        board[i][j] = 0
                return
    # Om lösning funnen? skriver ut detta, annars inget.           
    printBoard(board)
    sulotion = open('sudoku_solution.txt', 'w')
    sulotion.writelines(str(board))

solve()


print('\n')
for h in range(h_len):
    print(cheers[h], end=' ', flush=True); sleep(0.1)
print('\n')
sleep(0.5)