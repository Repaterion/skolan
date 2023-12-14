#!/usr/bin/python3

#Variabel för att lagra svar från husse.
svar = input('Är kattakräket hungrig? ')

#Skriva ut  mata kattet om den är hungrig!!! Vid felaktigt svar = Fräs!

#    .lower() gör om alla bokstäver till små.
if svar.lower() == 'ja':
   print ("Kurr kurr")
elif svar.lower() == 'nej':
   print ("Mjau")
else:
   print (" \n Blänger surt och dömmer dig tills döden skiljer er åt!!!")



print ("Katt gick och lade sig - program slut")

