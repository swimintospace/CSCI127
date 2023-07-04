#Name: Eliyas Philip
#Email: eliyas.philip84@myhunter.cuny.edu
#Date: October 29, 2021 
#This program takes data from the ramen csv 

import matplotlib.pyplot as plt 
import pandas as pd 

inputFile = input("Enter name of input file: ")
outputFile = input("Enter name of output file: ")

s = pd.read_csv(inputFile)

state = s.groupby('state')
seconds = state['duration (seconds)'].mean()


groupedData.plot.bar("State","Seconds")
plt.xlabel("State")
plt.ylabel("Seconds")

graph = plt.gcf()
graph.savefig(outputFile)