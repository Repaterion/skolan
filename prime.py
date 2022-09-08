#!/urs/bin/python3
#Primtalsletare.

numberToTest = int(input('Hur många tal vill du testa? '))


#Yttre loop prova - testa allt upp till numbersToTest.
for y in range (1, numberToTest+1):
   #Inre loop - testar om talet är jämnt delbart med allt annat.
   #Är detta jämnt delbart med något annat så är det ej ett primtal.
   provenNotPrime = False
   for k in range(2, y):
      if y % k == 0:
         print(y)
         provenNotPrime = True
         break
   if provenNotPrime == False:
      print(f'****** {y} Är ett primtal =D *****')

