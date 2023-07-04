#Name: Eliyas Philip
#Email: eliyas.philip84@myhunter.cuny.edu
#Date: September 29, 2021
#A program that takes user input to decide the turtle color and draws a square

print("Please enter tge conversion you want to do: ")
print("'a' for Light-Year to Parsec conversion ")
print("'b' for Parsec to Light-Year conversion")
selection = input("Your selection: ")

if selection == "a":
    lightyear = input("Please enter a number of Light-Years: ")
    lightyear = float(lightyear)
    parsecResult = (lightyear)/3.26156
    print(lightyear, "Light-Years is equal to ", parsecResult, "Parsecs.")

if selection == "b":
    parsec = input("Please enter a number of Parsecs: ")
    parsec = float(parsec)
    lightyearResult = parsec * 3.26156
    print(parsec, "Parsecs is equal to", lightyearResult, "Light-Years.")