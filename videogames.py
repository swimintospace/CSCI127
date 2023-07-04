#Name: Eliyas Philip
#Email: eliyas.philip84@myhunter.cuny.edu

from numpy import number
import pandas as pd 
import matplotlib.pyplot as plt

inFile = input("Enter file name: ")

games = pd.read_csv(inFile)

index = games.index 
rowNum = len(index)

print("There are ", rowNum, " total games")
print()

genres = games.pivot_table(index = ['Genre'], aggfunc = 'size')
print("The number of games in each genre is ")
print(genres)
print()

publishers = games.pivot_table(index = ['Publisher'], aggfunc = 'size')
topthree = publishers.nlargest(3)
print("The top 3 games publishers are ")
print(topthree)
