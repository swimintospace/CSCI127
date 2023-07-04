#Name: Eliyas Philip
#Email: eliyas.philip84@myhunter.cuny.edu
#Date: September 22, 2021
#The purpose of this program is to take the user's input and manupilate it


mess = input("Enter a phrase: ")
reversed = mess[::-1]
print("Reversed phrase: ", reversed)
reversed = reversed.upper()
reversedlist = reversed.split()
finalresult = ""

for word in reversedlist:
    finalresult += word[len(word) - 1]

print("Last letters of reversed words: ", finalresult )