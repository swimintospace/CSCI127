# Name: Eliyas Philip
# EmaiL: eliyas.philip84@myhunter.cuny.edu


import folium
import pandas as pd 

inputFile = input("Please enter the name of the input file: ")
outputFile = input("Please enter the name of the output file: ")
borough = input("Please enter the name of the borough: ")

wifiCSV = pd.read_csv(inputFile)

myMap = folium.Map(location=[40.768731, -73.964915], tiles="Stamen Watercolor")

for index, row in wifiCSV.iterrows():
    if row["City"] == borough:
        folium.Marker(location=[row["Latitude"], row["Longitude"]], popup=row["Location"]).add_to(myMap)

myMap.save(outfile=outputFile)