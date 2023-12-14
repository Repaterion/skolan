import math
resistors = []
print("Beräkning av ersättningsresistans")

resistors = input('Vilka värden önskas? ')
split_resisitors = resistors.split(' ')

series_result = sum(resistors)
parallell_result = 3
print('resistors')

print(f'Totala ersättningsresistansen för seriella: {series_result}')

