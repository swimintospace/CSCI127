#Name: Eliyas Philip
#Email: eliyas.philip84@myhunter.cuny.edu
#Date: October 4, 2021 
#This program decides influencer tier based on user input

#Import the libraries for arrays and displaying images:
import numpy as np
import matplotlib.pyplot as plt

#Read in the data to an array, called elevations:
elevations = np.loadtxt('elevationsNYC.txt')
#Load the array into matplotlib.pyplot:
#plt.imshow(elevations)
#Display the plot:
#plt.show()

mapShape = elevations.shape + (3,)

floodMap = np.zeros(mapShape)

for row in range(mapShape[0]):
    for col in range(mapShape[1]):
        if elevations[row,col] <= 0:
            #Below sea level
           floodMap[row,col,0:2] = 1.0     #Set the blue channel to 100%
        elif elevations[row,col] <=5:
            #Below the storm surge of Hurricane Sandy (flooding likely)
           floodMap[row,col,0] = 1.0     #Set the red channel to 100%
        elif elevations[row, col] <= 20:
            floodMap[row, col, 0:3] = 0.5
        else:
            #Above the 6 foot storm surge and didn't flood
            floodMap[row,col,1] = 1.0   #Set the green channel to 100%
            

#plt.imshow(floodMap)
#plt.show()
        
plt.imsave('floodMap.png', floodMap)