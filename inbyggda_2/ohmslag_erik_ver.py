import sys

def calcSerial(res_ser_Value): #Inom () är lokal variabel.
    returnValue = 0
    for s in res_ser_Value:
       returnValue += s
    return returnValue

def calcParallell(res_Para_Value):
    returnValue = 0
    for p in res_Para_Value:
        returnValue += 1/p
    return 1/returnValue

rawArg = sys.argv[1:]
#rawArg = input('Ange resistanser: ')       #sträng med rådata
#argList = rawArg.split()                   #Delad lista mellan varje mellanslag.
castadLista = [int(x) for x in rawArg]      #int konvertering utav string till integers.

#Insamling av data.
#for sum in argList:
#  castadLista.append(int(sum))

#print(sum(castadLista))
print(f'Parallellresistans: {calcParallell(castadLista)}')
print(f'Serieresistans: {calcSerial(castadLista)}')
