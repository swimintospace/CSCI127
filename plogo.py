#Name: Eliyas Philip
#Email: eliyas.philip84@myhunter.cuny.edu
#Date: October 6, 2021 
#This program displays the P logo for Python 


import matplotlib.pyplot as plt 
import numpy as np

logoImg = np.zeros((30, 30, 3))
logoImg[:,:6,0::2] = 1
logoImg[:6,:,0::2] = 1
logoImg[:21,25:,0::2] = 1
logoImg[15:21,:,0::2] = 1

plt.imsave('logo.png', logoImg)
