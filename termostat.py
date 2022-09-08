#!/usr/bin/python3

#Importerar bilioteket för slumpmässiga tal
import random as rnd


nuTemp = rnd.randint(15, 30)

if (nuTemp < 25 ):
   print (f'Element aktivteras! {nuTemp}C')
elif (nuTemp > 24):
   print (f'Element deaktiverat! {nuTemp}C')
else:
   print (f'Ringhals brinner {nuTemp}C' )
