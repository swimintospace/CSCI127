#Name:  Eliyas Philip
#Emai: eliyas.philip84@myhunter.cuny.edu
#Date:  September 29, 2021
#This program loads an image, displays it, and then creates, displays,
#    and saves a new image that has only the red and greeen channels displayed.

#Import the packages for images and arrays:
import matplotlib.pyplot as plt
import numpy as np

inpic = input("Enter name of the input file: ")
outpic = input("Enter name of the output file: ")
img = plt.imread(inpic)   #Read in image from csBridge.png


img2 = img.copy()        #make a copy of our image
img2[:,:,2] = 0          #Set the blue channel to 0

plt.imsave(outpic, img2)  #Save the image we created to the file: reds.png