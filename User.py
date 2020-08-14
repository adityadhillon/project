# -*- coding: utf-8 -*-
from Catalog import Catalog

issue_book = []
detail_issueBook = []
class User:
    def __init__(self, name, location, age, aadhar_id):
        self.name = name
        self.location = location
        self.age = age
        self.aadhar_id = aadhar_id
        

class Member(User):
    
    def checkIssuedBook(self,name):
        for i in range(len(issue_book)):
            if (issue_book[i][0] == name):
                print("Book is already issued to we cannot issue more")
        return ""
    
    def __init__(self,name, location, age, aadhar_id,student_id):
        super().__init__(name, location, age, aadhar_id)
        self.student_id = student_id
        
    def __repr__(self):
        return self.name + ' ' + self.location + ' ' + self.student_id
    
    #assume name is unique
    def issueBook(self,b,catalog,name,days=10):
        userName  = input("Enter your name:")
        if(userName == self.name):
             b = catalog.searchByName(name)
             if (b):
                 if (len(issue_book) > 0):
                        self.checkIssuedBook(self.name)
                 else:
                        print("Issued Book with Item no. :")
                        print(str(b.book_item[0].book) + ", " + b.book_item[0].isbn + ", " + b.book_item[0].rack)
                        detail_issueBook.append(self.name)
                        detail_issueBook.append(b.book_item[0])
                        issue_book.append(detail_issueBook)
                        del b.book_item[0]
             else:
                  print("No such Book")
        else:
             print("Wrong member name!")
        
        return ""
    
    #assume name is unique
    def returnBook(self,b,catalog,name):
        if (len(issue_book) == 0):
            print("Not a single book issued from Library yet")
            
        for i in range(len(issue_book)):
            if (issue_book[i][0] == name):
                b = catalog.searchByName(input('Enter Book name:'))
                if (b):
                    b.book_item.append(issue_book[i][1])
                    del issue_book[i]
                    print("Book returned successfully!")
                else:
                    print("No such Book issued to you")
                                      
            else:
                 print("Wrong Name")
        
        return ""
        
        
class Librarian(User):
    def __init__(self,name, location, age, aadhar_id,emp_id):
        super().__init__(name, location, age, aadhar_id)
        self.emp_id = emp_id
        
    def __repr__(self):
        return self.name + self.location + self.emp_id
    
    def addBook(self,b,catalog,name,author,publish_date,pages):
        b = catalog.addBook(name,author,publish_date,pages)
        i = input('How many items to be added:')
        for j in range(int(i)):
                 catalog.addBookItem(b, input('Isbn:'),input('Rack:'))
        
    
    def removeBook(self,b,catalog,name):
        b = catalog.searchByName(name)
        if (b):
              for book in catalog.books:
                  if name == book.name:
                                 catalog.books.remove(book)
              print("Book removed!")                   
        else:
             print("No such book available")
    
    def removeBookItemFromCatalog(self,b,catalog,book,isbn):
        b = catalog.searchByName(book)
        
        if (b):
              if (b.searchBookItem(isbn)):
                                         catalog.removeBookItem(book,isbn)
                                         print("ISBN:" +isbn+ " of Book " +book+ " removed!")
              else:
                   print("No such ISBN")
                    
        else:
             print("No such book available")