#Name: Eliyas Philip
#Email: eliyas.philip84@myhunter.cuny.edu
#Date: September 20, 2021
#This program takes a message from the user and shifts each character by 5 and displays the new character

mess = input('Enter a message: ')

for i in mess:
    newOrd = ord(i) + 5
    print(i, "shifted by 5 characters is ", chr(newOrd))
