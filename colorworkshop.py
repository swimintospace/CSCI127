# NAME: Eliyas Philip      
# EMAIL: eliyas.philip84@myhunter.cuny.edu

import matplotlib.pyplot as plt
import numpy as np

def validate(num):
    if 0 <= num <= 255:
        return num
    elif num < 0:
        return 0
    else:
        return 255


def main():
    print(
        """
------------------------------------------
Welcome to the Color Maker!
------------------------------------------
Please enter for each rbg color the value in which to increase/decrease them.
If all 3 values given are 0, the program will end and save the resulting image.
"""
    )


canvas = np.zeros((10, 10, 3))
red, green, blue = 0, 0, 0

y = input("Enter outfile name: ")
changeRed = int(input("How much do you want to change the red value by? \n"))
changeGreen = int(input("How much do you want to change the green value by? \n"))
changeBlue = int(input("How much do you want to change the blue value by? \n"))

red = validate(red + changeRed)
green = validate(green + changeGreen)
blue = validate(blue + changeBlue)

print("The current RGB values are: [", red / 255, ",", green / 255, ",", blue / 255,"]\n")

while changeRed + changeGreen + changeBlue != 0:

    changeRed = int(input("How much do you want to change the red value by? \n"))
    changeGreen = int(input("How much do you want to change the green value by? \n"))
    changeBlue = int(input("How much do you want to change the blue value by? \n"))

    red = validate(red + changeRed)
    green = validate(green + changeGreen)
    blue = validate(blue + changeBlue)

    print("The current RGB values are: [", red / 255, ",", green / 255, ",", blue / 255,"]\n")

canvas[:, :] = [red / 255, green / 255, blue / 255]
plt.imsave(y, canvas)

if __name__ == "__main__":
    main()