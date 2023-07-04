#Name: Eliyas Philip
#Email: eliyas.philip84@myhunter.cuny.edu
#Date: October 23, 2021 
#This program takes data from the ramen csv 

import pandas as pd 

name = input("Enter file name: ")

df = pd.read_csv(name)
df["Stars"] = pd.to_numeric(df["Stars"], downcast="float")

print("The average stars per serving style: ")
ramenData = df.groupby("Style")
print(ramenData["Stars"].mean())

Singaporedata = df.groupby("Country").get_group('Singapore')
print("KOKA has the lowest rating in Singapore with", Singaporedata["Stars"].min(), "stars")