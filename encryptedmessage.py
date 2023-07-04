#Name: Eliyas Philip
#Email: eliyas.philip84@myhunter.cuny.edu
#Date: September 23, 2021
#This program shifts each letter by 13 characters and prints the output in uppercase

mess = input("Enter a word: ")
result = ""

for letter in mess: 
    offset = ord(letter) - ord("A") + 13
    wrap = offset % 26 
    newChar = chr(ord("A") + wrap)
    result += newChar

print("Your word in code is ", result.upper())