mess = input("Enter a list of books and their authors: ")

firstlist = mess.split("; ")

for item in firstlist:
    secondlist = item.split("-")
    
print(secondlist)