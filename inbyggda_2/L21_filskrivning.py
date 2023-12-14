print("Halleloja!")

### Skapar en fil med namnet ###
f = open('minSkrivFil.txt', 'w') # PASS BY SEQUENCE, ANNARS SKRIV mode='skriv/läsetc'

minMtrix = [[1,2,3],[4,5,6],[7,8,9]]
print(minMtrix)

f.write("Testrad i filen =D ")
f.write("\nEn till rad\n")
f.write(str(minMtrix)) #Typecast till string

print(f)
# STÄNG FILEN.
f.close()

