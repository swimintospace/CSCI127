#Name: Eliyas Philip
#Email: eliyas.philip84@myhunter.cuny.edu
#Date: October 17, 2021 
#This program displays a square eye

import matplotlib.pyplot as plt
import numpy as np


firstImg = input("Enter first image file name: ")
secondImg = input("Enter second image file: ")
threshold = float(input("Enter threshold of white pixels: "))


ca = plt.imread(firstImg)   #Read in image
ca2 = plt.imread(secondImg)
countSnow = 0            #Number of pixels that are almost white
snowCount2 = 0

t = threshold             #Threshold for almost white-- can adjust between 0.0 and 1.0

#For every pixel:
for i in range(ca.shape[0]):
     for j in range(ca.shape[1]):
          #Check if red, green, and blue are > t:
          if (ca[i,j,0] > t) and (ca[i,j,1] > t) and (ca[i,j,2] > t):
               countSnow += 1


for i in range(ca2.shape[0]):
     for j in range(ca2.shape[1]):
          #Check if red, green, and blue are > t:
          if (ca2[i,j,0] > t) and (ca2[i,j,1] > t) and (ca2[i,j,2] > t):
               snowCount2 += 1

print("Snow count of first image: ", countSnow)
print("Snow count of second image: ", snowCount2)
print("Difference beween first and second image: ", countSnow - snowCount2)
