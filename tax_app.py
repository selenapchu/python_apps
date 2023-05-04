"""MSIS 320 HW6_Q1 by Selena Chu 05.30.2022

An app processes taxpayers.
inputs: taxpayer's name (str), income (float)
outputs: name (str), income (float), tax (float)
"""

taxpayers = {}
#insert: taxpayers[name] = income
#retrieve: income = taxpayers[name]

def submit():
    global taxpayers
    name = input('Enter name >>>')
    income = float(input('Enter income >>>'))
    tax_rate = compute_tax(income)
    tax = income * tax_rate
    taxpayers[name] = [income,tax]

    if name in taxpayers:
        print_taxpayer(name)
    else:
        print('No taxpayer found...')

def compute_tax(income):
    """Calculate tax rate.
    
    Parameters:
        Income (float)
    Returns:
        Tax rate (float)
    """
    global taxpayers
    tax_rate = 0.2 if income > 100000.0 else 0.1
    return tax_rate

def print_taxpayer(name):
    """Print taxpayer's name, income, and tax.
    
    Parameters:
        Name (str)
    Returns:
        Print name (str), income (float), tax (float)
    """
    global taxpayers
    value = taxpayers[name]
    income = value[0]
    tax = value[1]
    print(f'|{"Name":^12s}|{"Income":>10s}|{"Tax":>10s}|')
    print(f'|{name:^12s}|{income:>10.2f}|{tax:>10.2f}|')

def compute_average_tax():
    """Calculate average tax.
    
    Parameters:
        None
    Returns:
        Average tax (float if any, or None)
    """
    global taxpayers
    total_tax = 0.0
    count = 0
    for value in taxpayers.values():
        tax = value[1]
        total_tax += tax
        count += 1
    if count > 0:
        avg = total_tax / count
    else:
        avg = None
    return avg

def summary():
    global taxpayers
    avg = compute_average_tax()
    if avg is not None:
        print(f'The average tax is {avg:.2f}.')
    else:
        print('No data to compute average tax with!')

def reset():
    global taxpayers
    taxpayers.clear()

def line():
    return '-' * 36

def display():
    global taxpayers
    if taxpayers:
        for name in taxpayers:
            value = taxpayers[name]
            income = value[0]
            tax = value[1]
            print(line())
            print(f'|{"Name":^12s}|{"Income":>10s}|{"Tax":>10s}|')
            print(line())
            print(f'|{name:^12s}|{income:>10.2f}|{tax:>10.2f}|')
            print(line())
    else:
        print('No data to print!')

def search():
    global taxpayers
    if not taxpayers:
        print('No data to search!')
        return
    name = input('Enter name to search for >>>')
    if name in taxpayers:
        print_taxpayer(name)
    else:
        print('Not found!')

#main
quit = False
while not quit:
    print('1.Submit 2.Summary 3.Reset 4.Display 5.Search 6.Quit the app')
    choice = int(input('Enter 1, 2, 3, 4, 5 or 6>'))
    if choice == 1:
        submit()
    elif choice == 2:
        summary()
    elif choice == 3:
        reset()
    elif choice == 4:
        display()
    elif choice == 5:
        search()
    elif choice == 6:  
        quit = True
    else:
        print('Invalid choice! Choose 1, 2, 3, 4, 5 or 6')

print('Goodbye!')