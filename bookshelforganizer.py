#Name: Eliyas Philip
#Email: eliyas.philip84@myhunter.cuny.edu
#Date: September 28, 2021
#A program that displays a book's title and authors intials 
mess = input("Enter a list of books and their authors: ")

firstlist = mess.split("; ")


for item in firstlist:
    books = item.split(" - ")
    author = books[1].split(" ")
    print(books[0], "by", author[0][0]+ "." + author [1][0] + ".")
    print("Thank you for using my book organizer!")
