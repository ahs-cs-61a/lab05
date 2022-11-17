# lab01 WWPD?

import inspect

# preliminaries


def repeat():
    print("try again:")
    return input()


def intro():
    print("What Would Python Display?")
    print(
        "type the expected output, 'function' if you think the answer is a function object, 'infinite loop' if it loops forever, 'nothing' if nothing is displayed, or 'error' if it errors; use single quotes '' when needed\n"
    )


def outro():
    print("\nall questions for this question set complete")


# reference functions


def xk(c, d):
    if c == 4:
        return 6
    elif d >= 4:
        return 6 + 7 + c
    else:
        return 25


def how_big(x):
    if x > 10:
        print("huge")
    elif x > 5:
        print("big")
    elif x > 0:
        print("small")
    else:
        print("nothing")


def short_loop_1():
    n = 3
    while n >= 0:
        n -= 1
        print(n)


def short_loop_2():
    positive = 28
    while positive:
        print("positive")
        positive -= 3


def short_loop_3():
    positive = -9
    negative = -12
    while negative:
        if positive:
            print(negative)
        positive += 3
        negative += 3


def ab(c, d):
    if c > 5:
        print(c)
    elif c > 7:
        print(d)
    print("foo")


def bake(cake, make):
    if cake == 0:
        cake = cake + 1
        print(cake)
    if cake == 1:
        print(make)
    else:
        return cake
    return make


def special_case():
    x = 10
    if x > 0:
        x += 2
    elif x < 13:
        x += 3
    elif x % 2 == 1:
        x += 4
    return x


def just_in_case():
    x = 10
    if x > 0:
        x += 2
    if x < 13:
        x += 3
    if x % 2 == 1:
        x += 4
    return x


def case_in_point():
    x = 10
    if x > 0:
        return x + 2
    if x < 13:
        return x + 3
    if x % 2 == 1:
        return x + 4
    return x


def square(x):
    print("here!")
    return x * x


def so_slow(num):
    x = num
    while x > 0:
        x = x + 1
    return x / 0


# wwpd questions


def wwpd_control():  # wwpd_control
    intro()
    print(inspect.getsource(xk))  # xk

    print(">>> xk(10, 10)")
    x = input()
    while x != str(xk(10, 10)):
        x = repeat()

    print(">>> xk(10, 6)")
    x = input()
    while x != str(xk(10, 6)):
        x = repeat()

    print(">>> xk(4, 6)")
    x = input()
    while x != str(xk(4, 6)):
        x = repeat()

    print(">>> xk(0, 0)")
    x = input()
    while x != str(xk(0, 0)):
        x = repeat()

    print("\n", inspect.getsource(how_big))  # how_big

    print(">>> how_big(7)")
    x = input()
    while x != "big":
        x = repeat()

    print(">>> how_big(12)")
    x = input()
    while x != "huge":
        x = repeat()

    print(">>> how_big(1)")
    x = input()
    while x != "small":
        x = repeat()

    print(">>> how_big(-1)")
    x = input()
    while x != "nothing":
        x = repeat()

    print("\n", inspect.getsource(short_loop_1))  # short_loop_1

    print(">>> short_loop_1()")

    x = input()
    while x != "2":
        x = repeat()

    x = input()
    while x != "1":
        x = repeat()

    x = input()
    while x != "0":
        x = repeat()

    print("\n", inspect.getsource(short_loop_2))  # short_loop_2

    print(">>> short_loop_2()")
    x = input()
    while x != "infinite loop":
        x = repeat()

    print("\n", inspect.getsource(short_loop_3))  # short_loop_3

    print(">>> short_loop_3()")
    x = input()
    while x != "-12":
        x = repeat()

    x = input()
    while x != "-9":
        x = repeat()

    x = input()
    while x != "-6":
        x = repeat()

    outro()


def wwpd_booleans():  # wwpd_booleans
    intro()

    print(">>> True and 13")
    x = input()
    while x != str(True and 13):
        x = repeat()

    print(">>> False or 0")
    x = input()
    while x != str(False or 0):
        x = repeat()

    print(">>> not 10")
    x = input()
    while x != str(not 10):
        x = repeat()

    print(">>> not None")
    x = input()
    while x != str(not None):
        x = repeat()

    print(">>> True and 1 / 0 and False")
    x = input()
    while x != "error":
        x = repeat()

    print(">>> True or 1 / 0 or False")
    x = input()
    while x != str(True or 1 / 0 or False):
        x = repeat()

    print(">>> True or 0")
    x = input()
    while x != str(True or 0):
        x = repeat()

    print(">>> False or 1")
    x = input()
    while x != str(False or 1):
        x = repeat()

    print(">>> 1 and 3 and 6 and 10 and 15")
    x = input()
    while x != str(1 and 3 and 6 and 10 and 15):
        x = repeat()

    print(">>> -1 and 1 > 0")
    x = input()
    while x != str(-1 and 1 > 0):
        x = repeat()

    print(">>> 0 or False or 2 or 1 / 0")
    x = input()
    while x != str(0 or False or 2 or 1 / 0):
        x = repeat()

    print(">>> not 0")
    x = input()
    while x != str(not 0):
        x = repeat()

    print(">>> (1 + 1) and 1")
    x = input()
    while x != str((1 + 1) and 1):
        x = repeat()

    print(">>> 1/0 or True")
    x = input()
    while x != "error":
        x = repeat()

    print(">>> (True or False) and False")
    x = input()
    while x != str((True or False) and False):
        x = repeat()

    outro()


def wwpd_what_if():  # wwpd_what_if
    intro()
    print(inspect.getsource(ab))  # ab

    print(">>> ab(10, 20)")
    x = input()
    while x != "10":
        x = repeat()

    x = input()
    while x != "foo":
        x = repeat()

    print("\n", inspect.getsource(bake))  # bake

    print(">>> bake(0, 29)")
    x = input()
    while x != "1":
        x = repeat()

    x = input()
    while x != "29":
        x = repeat()

    x = input()
    while x != "29":
        x = repeat()

    print(">>> bake(1, 'mashed potatoes')")
    x = input()
    while x != "mashed potatoes":
        x = repeat()

    x = input()
    while x != "'mashed potatoes'":
        x = repeat()

    outro()


def wwpd_case_conundrum():  # wwpd_case_conundrum
    intro()
    print(inspect.getsource(special_case))  # special_case

    print(">>> special_case()")
    x = input()
    while x != str(special_case()):
        x = repeat()

    print("\n", inspect.getsource(just_in_case))  # just_in_case

    print(">>> just_in_case()")
    x = input()
    while x != str(just_in_case()):
        x = repeat()

    print("\n", inspect.getsource(case_in_point))  # case_in_point

    print(">>> case_in_point()")
    x = input()
    while x != str(case_in_point()):
        x = repeat()

    outro()


def wwpd_square_so_slow():  # wwpd_square_so_slow
    intro()
    print(inspect.getsource(square))
    print("\n", inspect.getsource(so_slow))

    print(">>> square(so_slow(5))")
    x = input()
    while x != "infinite loop":
        x = repeat()

    outro()
