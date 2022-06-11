import csv
from Class import Tax_Bracket

tax_array = []

with open('TaxBracket.csv', 'r') as file:
    reader = csv.reader(file, quoting=csv.QUOTE_NONNUMERIC)
    for row in reader:
        tax_array.append(Tax_Bracket(row[0], row[1]))

