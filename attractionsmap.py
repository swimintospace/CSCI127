# NAME: Eliyas Philip      
# EMAIL: eliyas.philip84@myhunter.cuny.edu
# Starter code Program #40: Checkers

import folium 
import pandas as pd 

ny = folium.Map(location=[40.768731, -73.964915])

csv = input("Enter CSV file name: ")
out = input("Enter output file: ")

attractions = pd.read_csv(csv)
#print(ny["Attractions"])

for index,row in attractions.iterrows():
    lat = row["LATITUDE"]
    lon = row["LONGITUDE"]
    name = row["NAME"]
    newMarker = folium.Marker([lat, lon], popup=name)
    newMarker.add_to(ny)

ny.save(outfile=out)