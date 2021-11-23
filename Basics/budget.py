

def calcBills():
    myBills = {'Electric': 140.00, 'Rent': 1400.00, 'Water_Sewer': 40.00,
               'Car Insurance': 75.00, 'Phone': 50.00}
    total = 0
    for i in myBills:
        total += myBills[i]
    due = 'The total due for bills this month is: ${}'.format(total)
    return due

calcBills()
