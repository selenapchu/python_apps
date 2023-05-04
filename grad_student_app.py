"""MSIS 320 HW7 by Selena Chu 06.06.2022

An app stores and displays students' names, scores, and division (graduate or undergraduate).
inputs: Student's name (str), score (int), division (1 for Graduate or 0 for Undergraduate)
outputs: name (str), score (int), division (str), number of students (int), average score (float)
"""

class Student:

    total_score = 0
    count = 0

    def __init__(self,name,score,division):
        self.name = name
        self.score = score
        self.division = division

        #update class variables
        Student.total_score += self.score
        Student.count += 1

    def __str__(self):
        return f'|{"Name":^12s}|{"Score":^12s}|{"Division":^15s}|\n|{self.name:^12s}|{self.score:^12d}|{self.division:^15s}|'

    def display_line(self):
        return f'|{self.name:^12s}|{self.score:^12d}|{self.division:^15s}|'

    def save_line(self):
        return f'{self.name:s},{self.score:d},{self.division:s}'

    @classmethod
    def compute_avg_score(cls):
        avg_score = cls.total_score / cls.count if cls.count else None
        return avg_score

    @classmethod
    def summary_report(cls):
        output_str = ''
        avg_score = cls.compute_avg_score()
        total_count = cls.count

        if avg_score is None:
            output_str += f'Number of Students: {total_count:d}\nNot enough data to calculate average score with...'
        else:
            output_str += f'|{"Number of Students":^20s}|{"Average Score":>20s}|\n|{total_count:^20d}|{avg_score:>20.2f}|'
        return output_str

    @classmethod
    def reset(cls):
        cls.total_score = 0
        cls.count = 0
    
    @staticmethod
    def line():
        return '-' * 43

    @staticmethod
    def caption():
        return f'|{"Name":^12s}|{"Score":^12s}|{"Division":^15s}|'

students = []

def submit():
    global students
    name = input('Enter name >>')
    score = int(input('Enter score >>'))
    graduate = int(input('Enter 1 for Graduate or 0 for Undergraduate >>'))
    division = 'Graduate' if graduate == 1 else 'Undergraduate'
    
    student = Student(name,score,division)
    students.append(student)

    print(student)

def load():
    with open('students.txt','r') as loadfile:
        for line in loadfile:
            mylist = line.split(',')
            name = mylist[0]
            score = int(mylist[1])
            graduate = int(mylist[-1])
            division = 'Graduate' if graduate == 1 else 'Undergraduate'
            student = Student(name,score,division)
            students.append(student)

    print('Data loaded.')

def summary():
    summary = Student.summary_report()
    print(summary)

def save():
    with open('outputs.txt','w') as savefile:
        for student in students:
            out_line = student.save_line()
            savefile.write(out_line + '\n')
    print('Data saved...')

def display():
    global students
    print(Student.line())
    print(Student.caption())
    print(Student.line())
    for student in students:
        print(student.display_line())
    print(Student.line())

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
    Student.reset()


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