'''Skolprojekt - Sudokulösare. 
    Sudoku är ett pussle där man skall räkna var varje siffra skall sitta.
    varje rad får bara ha 1-9 // Varje kolumn får ha 1-9 // Varje ruta får ha 1-9
 '''
import math
from functools import reduce #Används för att göra beräkningar.
from operator import add #Används till att göra andra beräkningar.
 #Listor för tal. Om 0 (nolla) matas in är detta en blank ruta.
rad1 = [1,2,3,4,5,6,7,8,9]
kolumn = [1,2,3,4,5,6,7,8,9]
crc = 45
crcAll = 405

print(rad1 + kolumn)
#Varje rad checksum: Varje rad skall ha exkat summa av = talen 1-9 adderade.
checkLine = reduce(add,rad1)
checkKolumn = reduce(add, kolumn)
print(checkLine)
print(checkLine * 9)

if (checkLine == crc) == 1:
    print('Rad 1 stämmer')
else:
    print('Rad 1 stämmer inte!!!')

#Summan av varje ruta.

#Summan av hela alla rutor.