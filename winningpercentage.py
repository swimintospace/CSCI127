#Name: Eliyas Philip
#Email: eliyas.philip84@myhunter.cuny.edu
#Date: November 1, 2021 

import matplotlib.pyplot as plt
import pandas as pd 


file = input("Name of input file: ")
output = input("Name of output file: ")

s = pd.read_csv(file)

s["Date"] = pd.to_datetime(s["Date"].apply(str))
s[" % Points"] = (s["Winner Pts"] / s["Loser Pts"] + s["Winner Pts"] * 100)

s.plot(x = "Date", y = " % Points")

fig = plt.gcf()
fig.savefig(output)