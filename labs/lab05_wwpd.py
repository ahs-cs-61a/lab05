# lab05 WWPD?


# IMPORTS

import inspect
import tests.wwpd_storage as s

st = s.wwpd_storage 


# COLORED PRINTS - custom text type to terminal: https://stackoverflow.com/questions/287871/how-do-i-print-colored-text-to-the-terminal, ANSI colors: http://www.lihaoyi.com/post/BuildyourownCommandLinewithANSIescapecodes.html

class bcolors:
    HIGH_MAGENTA = '\u001b[45m'
    HIGH_GREEN = '\u001b[42m'
    HIGH_YELLOW = '\u001b[43;1m'
    HIGH_RED = '\u001b[41m'
    HIGH_BLUE = '\u001b[44m'
    MAGENTA = ' \u001b[35m'
    GREEN = '\u001b[32m'
    YELLOW = '\u001b[33;1m'
    RED = '\u001b[31m'
    BLUE = '\u001b[34m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    RESET = '\u001b[0m'


# INCORRECT ANSWER LOOP, INSTRUCTIONS, COMPLETE, OPTIONS

def repeat():
    print("Try again:")
    return input()

def intro(name):
    print("\nWhat Would Python Display?: " + name)
    print("Type the expected output, 'function' if you think the answer is a function object, 'infinite loop' if it loops forever, 'nothing' if nothing is displayed, or 'error' if it errors; use single quotes '' when needed.\n")

def complete():
    print(bcolors.HIGH_GREEN + bcolors.BOLD + "\nSUCCESS: All questions for this question set complete." + bcolors.ENDC)

def options():
    print(bcolors.HIGH_MAGENTA + bcolors.BOLD + "\nMESSAGE: All questions for this question set complete. Restart question set?" + bcolors.ENDC)
    guess = input("Y/N?\n")
    guess = guess.lower()
    while guess != "y" and guess != "n":
        print(bcolors.HIGH_YELLOW + bcolors.BOLD + "\nUnknown input, please try again." + bcolors.ENDC)
        guess = input()
    if guess == "y":
        return "restart"
    return False


# WWPD? ALGORITHM 

def wwpd(name, question_set, stored_list):

    intro(name)

    match_elems1 = [[question_set[i][0], question_set[i][2]] for i in range(len(question_set))]
    match_elems2 = [[stored_list[i][0], stored_list[i][1]] for i in range(len(stored_list))]

    restart = str(match_elems1)[1:-1] in str(match_elems2) and options() == "restart"

    done = False
    for i in question_set:
        group = [i[0], i[2], i[3], True]
        if group not in stored_list or restart:
            done = True 
            if i[1]:
                print(i[1])
            if i[2]:
                print(i[2])
            guess = input()
            while guess != i[3]:
                guess = repeat()
            if str(match_elems1)[1:] not in str(match_elems2):
                op = open("tests/wwpd_storage.py", "w")
                if not stored_list:
                    stored_list = [group]
                else:
                    for j in range(len(stored_list)):
                        if group[0] < stored_list[j][0]:
                            stored_list.insert(j, group)
                            break
                    stored_list.append(group)
                op.write("wwpd_storage = " + str(stored_list))
                op.close()
    if done:
        complete()


# REFERENCE CLASSES & METHODS

# https://inst.eecs.berkeley.edu/~cs61a/su22/disc/disc05/

class Student:

    extension_days = 3 # this is a class variable

    def __init__(self, name, staff):
        self.name = name # this is an instance variable
        self.understanding = 0
        staff.add_student(self)
        print("Added", self.name)

    def visit_office_hours(self, staff):
        staff.assist(self)
        print("Thanks, " + staff.name)

class Professor:

    def __init__(self, name):
        self.name = name
        self.students = {}

    def add_student(self, student):
        self.students[student.name] = student

    def assist(self, student):
        student.understanding += 1

    def grant_more_extension_days(self, student, days):
        student.extension_days = days


# https://inst.eecs.berkeley.edu/~cs61a/su22/lab/lab04/

class Car:
    num_wheels = 4
    gas = 30
    headlights = 2
    size = 'Tiny'

    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.color = 'No color yet. You need to paint me.'
        self.wheels = Car.num_wheels
        self.gas = Car.gas

    def paint(self, color):
        self.color = color
        return self.make + ' ' + self.model + ' is now ' + color

    def drive(self):
        if self.wheels < Car.num_wheels or self.gas <= 0:
            return 'Cannot drive!'
        self.gas -= 10
        return self.make + ' ' + self.model + ' goes vroom!'

    def pop_tire(self):
        if self.wheels > 0:
            self.wheels -= 1

    def fill_gas(self):
        self.gas += 20
        return 'Gas level: ' + str(self.gas)


# QUESTION SET - ELEMENT FORMAT: [<INITIAL PRINTS> (usually empty), <QUESTION>, <ANSWER>]
# INSPECT MODULE - convert function body into String: https://docs.python.org/3/library/inspect.html 

student_oop_qs = [
    ['>>> callahan = Professor("Callahan")', '>>> elle = Student("Elle", callahan)', "Added Elle"],
    ["", ">>> elle.visit_office_hours(callahan)", "Thanks, Callahan"],
    ["", '>>> elle.visit_office_hours(Professor("Paulette"))', "Thanks, Paulette"],
    ["", ">>> elle.understanding", "2"],
    ["", ">>> [name for name in callahan.students]", "['Elle']"],
    ["", 'x = Student("Vivian", Professor("Stromwell")).name', "Added Vivian"],
    ["", ">>> x", "'Vivian'"],
    ["", ">>> elle.extension_days", "3"],
    [">>> callahan.grant_more_extension_days(elle, 7)", ">>> elle.extension_days", "7"],
    ["", ">>> Student.extension_days", "3"]
    ]
student_oop_qs = [[i + 1] + student_oop_qs[i] + [False] for i in range(len(student_oop_qs))]


classy_cars_qs = [
    [inspect.getsource(Car) + "\n\n>>> deneros_car = Car('Tesla', 'Model S')", ">>> deneros_car.model", "'Model S'"],
    [">>> deneros_car.gas = 10", ">>> deneros_car.drive()", "'Tesla Model S goes vroom!'"],
    ["", ">>> deneros_car.drive()", "'Cannot drive!'"],
    ["", ">>> deneros_car.fill_gas()", "'Gas level: 20'"],
    ["", ">>> Car.gas", "30"],
    [">>> deneros_car = Car('Tesla', 'Model S')\n>>> deneros_car.wheels = 2", ">>> deneros_car.wheels", "2"],
    ["", ">>> Car.num_wheels", "4"],
    ["", ">>> deneros_car.drive()", "'Cannot drive!'"],
    ["", ">>> Car.drive()", "error"],
    ["", ">>> Car.drive(deneros_car)", "'Cannot drive!'"]
]
classy_cars_qs = [[i + 1] + classy_cars_qs[i] + [False] for i in range(len(classy_cars_qs))]


# WWPD? QUESTIONS

def wwpd_student_oop():
    wwpd("Student OOP", student_oop_qs, st)

def wwpd_classy_cars():
    wwpd("Classy Cars", classy_cars_qs, st)
