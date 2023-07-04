# NAME: Eliyas Philip      
# EMAIL: eliyas.philip84@myhunter.cuny.edu

import math 
def is_square(positive_int):
    if positive_int < 0:
        return False
    root = math.sqrt(positive_int)
    return positive_int == int(root + 0.5) ** 2

def perfectSquareChecker(num):
    if not (is_square(num)):
        print("Hey, this number isn't even! Try again next time.")
        return

    print("This number is a perfect square, it is the product of:", math.sqrt(num), "squared.")

def main():

    square = True

    while square:
        i1 = int(input('Enter a square integer: '))

        if is_square(i1):
            perfectSquareChecker(i1)
            square = False


if __name__ == "__main__":
    main()