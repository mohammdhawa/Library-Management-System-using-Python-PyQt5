import datetime

class Author:
    __name = ''
    __location = ''
    
    def Show_Authors(self):
        pass
    
    def Add_Author(self, name, location):
        self.__name = name
        self.__location = location

class Publisher:
    __name = ''
    __location = ''
    
    def Show_Publisher(self):
        pass
    
    def Add_Publisher(self, name, location):
        self.__name = name
        self.__location = location

class Category:
    __name = ''
    
    def Show_Categories(self):
        pass
    
    def Add_Category(self, name):
        self.__name = name

class Publications:
    _title = ''
    _description = ''
    _code = ''
    _price = 0.0
    
class Books(Publications):
    __categories = Category()
    __authors = Author()
    __publishers = Publisher()
    
    def Show_Books(self):
        pass
    
    def Add_Book(self):
        pass
    
    def Edit_Book(self):
        pass
    
    def Delete_Book(self):
        pass
    
    def Filter_Book(self):
        pass
    
    def Export_Book(self):
        pass

class Researches(Publications):
    __subject = ''
    __authors = ''
    __language = ''
    
    def Show_Researches(self):
        pass
    
    def Add_Research(self):
        pass
    
    def Edit_Research(self):
        pass
    
    def Delete_Research(self):
        pass
    
    def Filter_Research(self):
        pass
    
    def Export_Research(self):
        pass

class User:
    _name = ''
    _mail = ''
    _national_id = ''
    _phone = ''
    
class Students(User):
    __department = ''
    
    def Show_Students(self):
        pass
    
    def Add_Student(self):
        pass
    
    def Edit_Student(self):
        pass
    
    def Delete_Student(self):
        pass
    
    def Filter_Student(self):
        pass
    
    def Export_Student(self):
        pass

class Sales:
    __title = ''
    __code = ''
    __sale_type = ''
    __sold_to = ''
    __price = 0.0
    
    def Show_Sales(self):
        pass
    
    def Add_Sale(self):
        pass

class Librarian:
    __name = ''
    __mail = ''
    __national_id = ''
    __phone = ''
    __password = ''
    __users = User()
    __books = Books()
    
    def Return_Book(self):
        pass
    
    def Collect_Fine(self, fine):
        pass
    
    def Search_Book(self):
        pass
    
    def Sell_Book(self):
        pass
    
    def Pay_Bills(self):
        pass
    
    def Order_Book(self):
        pass
    
    def Verify_Member(self):
        pass

class Database:
    
    def Show_All_Books(self):
        pass
    
    def Export_Books(self):
        pass
    
    def Show_All_Students(self):
        pass
    
    def Export_Students(self):
        pass
    
    def Show_All_Researches(self):
        pass
    
    def Export_Researchs(self):
        pass
    
    def Show_All_Employees(self):
        pass
    
    def Export_Employees(self):
        pass
    
    def Show_All_Authors(self):
        pass
    
    def Export_Authors(self):
        pass
    
    def Show_All_Publishers(self):
        pass
    
    def Export_Publishers(self):
        pass

class Reports:
    __date_from = datetime.datetime.now()
    __date_to = datetime.datetime.now()
    __database = Database()
    
    def Books_Report(self):
        pass
    
    def Researches_Report(self):
        pass
    
    def Students_Report(self):
        pass
    
    def Daily_Report(self):
        pass
    
    def History_Report(self):
        pass

class LibraryManagementSystem:
    __name = ''
    __password = ''
    __database = Database()
    __publication = Publications()
    __users = User()
    __librarian = Librarian()
    __sales = Sales()
    
    def Login(self):
        pass
    
    def Logout(self):
        pass
    
    def Send_Email_To_Reset_Password(self):
        pass