class Library:
    def __init__(self):
        self.nbooks = 0
        self.books = []
     
    def addbooks(self, book):
        self.books.append(book)
        self.nbooks = len(self.books)

    def show(self):
        print(f"The total books in the library is : {self.nbooks}") 
        print("The name of the books are : ")
        for i in self.books:
            print(i)

l1 = Library()
l1.addbooks("Gulistan e Johar")
l1.addbooks("Salam Software in Bholari")
l1.addbooks("Ek Din Jeo k sath")
l1.show()

