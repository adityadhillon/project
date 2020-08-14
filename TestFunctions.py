# -*- coding: utf-8 -*-
from Book import Book
from Catalog import Catalog
from User import Member, Librarian
import sys 
#b1 = Book('Shoe Dog','Phil Knight', '2015',312)
#b1.addBookItem('123hg','H1B2')
#b1.addBookItem('124hg','H1B3')

#b1.printBook()
#-----------------------------------------------------------------------------------------#
def functionChoice(choice): 
    
    if (choice == 1):
        m1.issueBook(b,catalog,input('Enter your Book name:'))
    elif (choice == 2): 
        m1.returnBook(b,catalog,input('Enter your name:'))
    elif (choice == 3): 
        librarian.addBook(b,catalog,input('Enter Book Name:'), input('Enter Author Name:'), input('Enter Publish Date:'), input('Enter Total Pages:'))
    elif (choice == 4): 
        librarian.removeBook(b,catalog,input('Enter name of Book to be removed:'))
    elif (choice == 5): 
        librarian.removeBookItemFromCatalog(b,catalog,input("Enter name of Book whose item number to be removed:"),input("ISBN:"))
    elif (choice == 6): 
        catalog.searchByAuthor(input('Enter Author name:'))
    elif (choice == 7):
        catalog.displayAllBooks()
        print("Have a Good Day!")
        sys.exit()
    else:
        print("Wrong Input")
    return ""
    
catalog = Catalog()

b = catalog.addBook('Shoe Dog','Phil Knight', '2015',312)
catalog.addBookItem(b, '123hg','H1B2')
catalog.addBookItem(b, '124hg','H1B4')
catalog.addBookItem(b, '125hg','H1B5')

b = catalog.addBook('Moonwalking with Einstien','J Foer', '2017',318)
catalog.addBookItem(b, '463hg','K1B2')

catalog.displayAllBooks()

m1 = Member("Vish","Bangalore",23,'asljlkj22','std1233')
librarian = Librarian("Awantik","Bangalore",34,'asljlkj22','zeke101') 

print("-------------------------------------------------")
print("For Member -- Type Appropiate number for service:")
print("1. Issue Book")
print("2. Return Book")

print("For Librarian -- Type Appropiate number for service:")
print("3. Add Book")
print("4. Remove Book")
print("5. Remove Book Item from Catalog")
print("6. Search By Author")
print("7. Exit")
while True:
  try:
    choice=int(input('Enter Input:'))
    print (functionChoice(choice))
  except ValueError:
    print("Wrong Input")

#-----------------------------------------------------------------------------------------#

#print (m1)
#print (librarian)

#b = catalog.searchByName('Shoe Dog')
#print (b)


#catalog.removeBookItem('Shoe Dog','124hg')
#catalog.displayAllBooks()
#m1.issueBook
