"""MSIS 320 HW6_Q2 by Selena Chu 05.30.2022

An app stores and displays students' names and scores.
inputs: Student's name (str), score (int)
outputs: name (str), score (int)
"""

class Student:
    def __init__(self,name,score):
        self.name = name
        self.score = score

    def __str__(self):
        return f'|{"Name":^12s}|{"Score":^12s}|\n|{self.name:^12s}|{self.score:^12d}|'

    def display_line(self):
        return f'|{self.name:^12s}|{self.score:^12d}|'

students = []

def submit():
    global students
    name = input('Enter name >>')
    score = int(input('Enter score >>'))

    student = Student(name,score)
    students.append(student)

    print(student)

def load():
    pass

def summary():
    pass

def save():
    pass

def line():
    return '-' * 27

def display():
    global students
    print(line())
    print(f'|{"Name":^12s}|{"Score":^12s}|')
    print(line())
    for student in students:
        print(student.display_line())
    print(line())

def search():
    global students
    if not students:
        print('No Data...')
        return
    name = input('Enter name to search >>')
    for student in students:
        if name == student.name:
            print(student)
            return
    print('Not Found!')


def reset():
    global students
    students.clear()


#main
quit = False
while not quit:
   print('1.Submit 2.Load 3.Summary 4.Save 5.Display 6.Search 7. Reset 8. Exit')
   choice = int(input('Enter choice:  '))
   if choice == 1:
       submit()
   elif choice == 2:
       load()
   elif choice == 3:
       summary()
   elif choice == 4:
       save()
   elif choice == 5:
       display()
   elif choice == 6:
       search()
   elif choice == 7: 
       reset()    
       print('Data cleared. Ready for new series...')
   elif choice == 8:
       quit = True   
   else:
       print('Invalid Choice!')