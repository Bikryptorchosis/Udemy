import sys


def getint(prompt):
    while True:
        try:
            number = int(input(prompt))
            return number
        except ValueError:
            print("Niepoprawna liczba, TRAJ EGEN")
        except EOFError:
            sys.exit(1)


num1 = getint("Podej pierwszo liczba: ")
num2 = getint("Podej drugo liczba: ")

try:
    print("{} podzielone przez {} wynosi {}".format(num1, num2, num1/num2))
except ZeroDivisionError:
    print("Nie dziel przez 0, kurwo")
    sys.exit(2)
except (MemoryError, OverflowError):
    print("jakim kurwa cudem")
