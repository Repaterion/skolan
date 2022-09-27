'''Skolprojekt - Sudokulösare. 
    Sudoku är ett pussle där man skall räkna var varje siffra skall sitta.
    varje rad får bara ha 1-9 // Varje kolumn får ha 1-9 // Varje ruta får ha 1-9
 '''
from functools import reduce #Används för att göra beräkningar.
from operator import add #Används till att göra andra beräkningar.
import csv
import sys

myArg = sys.argv


 #Listor för tal. Om 0 (nolla) matas in är detta en blank ruta.
rad1 = [1,2,3,4,5,6,7,8,9]
kolumn = [1,2,3,4,5,6,7,8,9]
crc = 45
crcAll = 405

problem = open("pussel.csv")

print(rad1 + kolumn)
#Varje rad checksum: Varje rad skall ha exkat summa av = talen 1-9 adderade.
checkLine = reduce(add,rad1)
checkKolumn = reduce(add, kolumn)
print(checkLine)
print(checkLine * 9)

#Får skapa en nästlad IF-sats.
if (checkLine == crc) == True:
    print('Rad 1 stämmer')
elif(checkKolumn == crc) == True:
    print('Kolumn sann')
else:
    print('Rad 1 stämmer inte!!!')

print (problem.readline())
#Summan av varje ruta.

#Summan av hela alla rutor.

problem.close() #Stänger filen pussel.csv