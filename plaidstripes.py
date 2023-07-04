#Name: Eliyas Philip
#Email: eliyas.philip84@myhunter.cuny.edu
#Date: October 10, 2021 
#This program displays a plaid pattern 


import matplotlib.pyplot as plt 
import numpy as np

size = int(input("Enter the size: "))
img = input("Enter the output file: ")

stripesImg = np.ones((size, size, 3))
stripesImg[1::2,:,:] = .94,.90,.55
stripesImg[:,1::2,:] = .73,.56,.56 

plt.imsave(img, stripesImg)