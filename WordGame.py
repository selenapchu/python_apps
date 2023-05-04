"""
An app stores and generate words based on game rule of a word's first letter must follow the last letter of the predecessor.
Inputs: A place's name (str)
Output: A new place's name (str) which does not repeat the ones before
"""


data = {}

used = {}
#computer doesnt know what has already been used

def store(entry):
    let = entry[0]
    if let in used.keys():   #does the key let exist in used? does the list exist?
        used[let].append(entry)
    else:
        used[let] = [entry]

def used_already(entry):
    let = entry[0]
    return let in used.keys() and entry in used[let] #true if entry is in used list

def retrieve(let):
    while True:
        if data[let]:
            response = data[let].pop(0)
            if not used_already(response):
                response = response.upper()
                store(response)
                return response #return first element, and deletes it
        else:
            return None

def load():
    with open('datafile.txt', 'r') as infile:
        lines = infile.readlines()

    for line in lines:
        inlist = line.split()
        data[inlist[0]] = inlist[1:]      #slice a list   numbers[1:4]

#main
load()
let = None
while True:
    entry = input('Enter a place name or 0 to quit: >>')
    if entry == '0':
        print('Bye!')
        break
    entry = entry.upper()

    if let and entry[0] != let: #let is not None
        print('Not match! Try again!')
        continue

    if used_already(entry):
        print('Used already! Try again!')
        continue

    let = entry[-1]

    store(entry)

    response = retrieve(let)

    if response is None:
        print('I CONCEDE!')
        break

    print(response, response[-1])
    let = response[-1]

