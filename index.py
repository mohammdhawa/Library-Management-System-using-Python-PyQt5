# from types import NoneType
from unicodedata import category
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
# from PyQt5.uic import loadUiType
import MySQLdb
import sys
import datetime
from xlsxwriter import *
from xlrd import *
from abc import ABC, abstractmethod
import smtplib
from random import randint
# from PyQt5 import QtGui, QtCore

from main import Ui_MainWindow as Main_Window

#################################### New Classes #########################################

class Author_2:
    __name = ''
    __location = ''
    
    def __init__(self):
        self.DB_Connect()
    
    def Show_Authors(self):
        self.cur.execute(''' 
                         SELECT name from author 
                         ''')
        authors = self.cur.fetchall()
        
        return authors
    
    def Add_Author(self, name, location):
        self.__name = name
        self.__location = location
        self.cur.execute(''' 
                         INSERT INTO author(name, location)
                         VALUES (%s, %s) 
                         ''', (self.__name, self.__location))
        
        ################## History
        global employee_id
        sql = ''' INSERT INTO history(employee_id, operation_date, history_table, history_action) 
        VALUES (%s, %s, %s, %s) '''
        self.cur.execute(sql, (employee_id, datetime.datetime.now(), table[5], action[3]))
        
        self.db.commit()
    
    ###################################### 
    def Show_Authors_Database(self):
        self.cur.execute(''' SELECT name, location FROM author ''')
        data = self.cur.fetchall()
        return data
    
    def Export_Authors_Database(self):
        sql = ''' SELECT name, location FROM author '''
        self.cur.execute(sql)
        data = self.cur.fetchall()
        
        excel_file = Workbook("author_database_report.xlsx")
        sheet1 = excel_file.add_worksheet()
        
        sheet1.write(0, 0, "Author Name")
        sheet1.write(0, 1, "Author Location")
        
        row_number = 1
        for row in data:
            col_number = 0
            for item in row:
                sheet1.write(row_number, col_number, str(item))
                col_number += 1
            row_number += 1
        
        excel_file.close()
    
    def DB_Connect(self):
        self.db = MySQLdb.connect(host='localhost', user='root', password='toor', db='my_library')
        self.cur = self.db.cursor()

class Publisher_2:
    __name = ''
    __location = ''
    
    def __init__(self):
        self.DB_Connect()
    
    def Show_Publishers(self):
        self.cur.execute(''' 
                         SELECT name from publisher 
                         ''')
        publishers = self.cur.fetchall()
        
        return publishers
    
    def Add_Publisher(self, name, location):
        self.__name = name
        self.__location = location
        self.cur.execute(''' 
                         INSERT INTO publisher(name, location)
                         VALUES (%s, %s) 
                         ''', (self.__name, self.__location))
        
        ################## History
        global employee_id
        sql = ''' INSERT INTO history(employee_id, operation_date, history_table, history_action) 
        VALUES (%s, %s, %s, %s) '''
        self.cur.execute(sql, (employee_id, datetime.datetime.now(), table[6], action[3]))
        
        self.db.commit()
    
    #######################################################
    def Show_Publishers_Database(self):
        self.cur.execute(''' SELECT name, location FROM publisher ''')
        data = self.cur.fetchall()
        return data
    
    def Export_Publishers_Database(self):
        sql = ''' SELECT name, location FROM publisher '''
        self.cur.execute(sql)
        data = self.cur.fetchall()
        
        excel_file = Workbook("publisher_database_report.xlsx")
        sheet1 = excel_file.add_worksheet()
        
        sheet1.write(0, 0, "publisher Name")
        sheet1.write(0, 1, "publisher Location")
        
        row_number = 1
        for row in data:
            col_number = 0
            for item in row:
                sheet1.write(row_number, col_number, str(item))
                col_number += 1
            row_number += 1
        
        excel_file.close()
    
    def DB_Connect(self):
        self.db = MySQLdb.connect(host='localhost', user='root', password='toor', db='my_library')
        self.cur = self.db.cursor()

class Category_2:
    __name = ''
    
    def __init__(self):
        self.DB_Connect()
    
    def Show_Categories(self):
        self.cur.execute(''' 
                         SELECT name FROM category 
                         ''')
        categories = self.cur.fetchall()
        
        return categories
    
    def Add_Cateogry(self, name):
        self.__name = name
        self.cur.execute(''' 
                         INSERT INTO category(name)
                         VALUES (%s) 
                         ''', [(self.__name)])
        
        ################## History
        global employee_id
        sql = ''' INSERT INTO history(employee_id, operation_date, history_table, history_action) 
        VALUES (%s, %s, %s, %s) '''
        self.cur.execute(sql, (employee_id, datetime.datetime.now(), table[4], action[3]))
        
        self.db.commit()
    
    def DB_Connect(self):
        self.db = MySQLdb.connect(host='localhost', user='root', password='toor', db='my_library')
        self.cur = self.db.cursor()

class Publications_2:
    _title = ''
    _description = ''
    _code = ''
    _price = 0.0
    
    def add(self, title, description, code, price):
        self._title = title
        self._description = description
        self._code = code
        self._price = price
    

class Books_2(Publications_2):
    __date = datetime.datetime.now()
    __category = ''
    __author = ''
    __publisher = ''
    
    ###### Coposition relation between Authors and Books
    authors = Author_2()
    ##### Composition relation between Publishers and Books
    publishers = Publisher_2()
    ##### Composition relation between Categories and Books
    categories = Category_2()
    
    def __init__(self):
        self.DB_Connect()

    def Show_Books(self):
        self.cur.execute(''' SELECT title, code, category_id, author_id, price FROM book ''')
        data = self.cur.fetchall()
        return data
    
    def Book_Search(self, code):
        self._code = code
        sql = ''' SELECT * FROM book WHERE  code=%s '''
        self.cur.execute(sql, [(self._code)])
        data = self.cur.fetchone()
        return data

    def Filter_Books(self, category_index, category):
        if category_index == 0:
            sql = ''' SELECT title, code, category_id, author_id, price FROM book '''
            self.cur.execute(sql)
        else:
            sql = ''' SELECT title, code, category_id, author_id, price FROM book WHERE category_id=%s '''
            self.cur.execute(sql, [(category)])
        
        data = self.cur.fetchall()
        return data
    
    def Add_Book(self, title, description, code, category, author, publisher, price, date):
        self._title = title
        self._description = description
        self._code = code
        self.__category = category
        self.__author = author
        self.__publisher = publisher
        self._price = price
        self.__data = date
        
        self.cur.execute('''
            INSERT INTO book(title, description, code, category_id, author_id, publisher_id, price, book_date)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        ''', (self._title, self._description, self._code, self.__category, 
              self.__author, self.__publisher, self._price, self.__date))
        
        ####### history
        global employee_id
        sql = ''' INSERT INTO history(employee_id, operation_date, history_table, history_action) 
        VALUES (%s, %s, %s, %s) '''
        self.cur.execute(sql, (employee_id, self.__date, table[1], action[3]))

        self.db.commit()
    
    def Edit_Book(self, title, description, code, category, author, publisher, price, date, prev_code):
        self._title = title
        self._description = description
        self._code = code
        self.__category = category
        self.__author = author
        self.__publisher = publisher
        self._price = price
        self.__date = date
        self.cur.execute(''' UPDATE book SET title=%s, description=%s, code=%s, category_id=%s, author_id=%s, publisher_id=%s, price=%s, book_date=%s WHERE code=%s 
                         ''', (self._title, self._description, self._code, self.__category, self.__author, self.__publisher, self._price, self.__date, prev_code))
        
        ################## History
        global employee_id
        sql = ''' INSERT INTO history(employee_id, operation_date, history_table, history_action) 
        VALUES (%s, %s, %s, %s) '''
        self.cur.execute(sql, (employee_id, self.__date, table[1], action[4]))
        
        self.db.commit()
    
    def Delete_Book(self, code):
        self.cur.execute(''' DELETE FROM book WHERE code=%s ''', [(code)])
        
        ################## History
        global employee_id
        sql = ''' INSERT INTO history(employee_id, operation_date, history_table, history_action) 
        VALUES (%s, %s, %s, %s) '''
        self.cur.execute(sql, (employee_id, self.__date, table[1], action[5]))
        
        self.db.commit()
    
    def Export_Books(self):
        sql = ''' SELECT code, title, category_id, author_id, publisher_id, price FROM book '''
        self.cur.execute(sql)
        data = self.cur.fetchall()
        
        excel_file = Workbook("books_report.xlsx")
        sheet1 = excel_file.add_worksheet()
        
        sheet1.write(0, 0, "Book Code")
        sheet1.write(0, 1, "Book Title")
        sheet1.write(0, 2, "Book Category")
        sheet1.write(0, 3, "Book Author")
        sheet1.write(0, 4, "Book Publisher")
        sheet1.write(0, 5, "Book Price")
        
        row_number = 1
        for row in data:
            col_number = 0
            for item in row:
                sheet1.write(row_number, col_number, str(item))
                col_number += 1
            row_number += 1
        
        excel_file.close()
    
    ################################
    def Show_Books_Database(self):
        self.cur.execute(''' SELECT title, code, category_id, author_id, publisher_id, price, book_date, description FROM book ''')
        data = self.cur.fetchall()
        return data
    
    def Export_Books_Database(self):
        sql = ''' SELECT title, code, category_id, author_id, publisher_id, price, book_date, description FROM book '''
        self.cur.execute(sql)
        data = self.cur.fetchall()
        
        excel_file = Workbook("books_database_report.xlsx")
        sheet1 = excel_file.add_worksheet()
        
        sheet1.write(0, 0, "Book Title")
        sheet1.write(0, 1, "Book Code")
        sheet1.write(0, 2, "Book Category")
        sheet1.write(0, 3, "Book Author")
        sheet1.write(0, 4, "Book Publisher")
        sheet1.write(0, 5, "Book Price")
        sheet1.write(0, 6, "Book Date")
        sheet1.write(0, 7, "Book Description")
        
        row_number = 1
        for row in data:
            col_number = 0
            for item in row:
                sheet1.write(row_number, col_number, str(item))
                col_number += 1
            row_number += 1
        
        excel_file.close()
    
    def DB_Connect(self):
        self.db = MySQLdb.connect(host='localhost', user='root', password='toor', db='my_library')
        self.cur = self.db.cursor()

class Researches_2(Publications_2):
    __subject = ''
    __authors = ''
    __language = ''
    __date = datetime.datetime.now()
    
    def __init__(self):
        self.DB_Connect()
    
    def Show_Researches(self):
        self.cur.execute(''' SELECT research_title, code, research_subject, research_author, research_language, price FROM research ''')
        data = self.cur.fetchall()
        return data
    
    def Research_Search(self, code):
        self._code = code
        self.cur.execute(''' SELECT * from research WHERE code=%s ''', [(self._code)])
        data = self.cur.fetchone()
        return data
    
    def Filter_Researchs(self, subject_idx, subject_name):
        if subject_idx == 0:
            self.cur.execute(''' SELECT research_title, code, research_subject, research_author, research_language, price FROM research ''')
        else:
            self.cur.execute(''' SELECT research_title, code, research_subject, research_author, research_language, price FROM research 
                            WHERE research_subject=%s ''', [(subject_name)])
        
        data = self.cur.fetchall()
        return data
    
    def Add_Research(self, title, description, code, subject, author, language, price, date):
        self._title = title
        self._code = code
        self._description = description
        self._price = price
        self.__authors = author
        self.__subject = subject
        self.__language = language
        self.__date = date
        
        self.cur.execute(''' INSERT INTO research(research_title, research_description, code, research_subject, 
                         research_author, research_language, price, date)
                         VALUES (%s, %s, %s, %s, %s, %s, %s, %s) ''', (self._title, self._description, 
                                                                       self._code, self.__subject, 
                                                                       self.__authors, self.__language, 
                                                                       self._price, self.__date))
        self.db.commit() 
    
    def Edit_Research(self, title, description, code, subject, author, language, price, date, prev_code):
        self._title = title
        self._code = code
        self._description = description
        self._price = price
        self.__authors = author
        self.__subject = subject
        self.__language = language
        self.__date = date
        
        self.cur.execute(''' UPDATE research SET research_title=%s, research_description=%s, code=%s, 
                         research_subject=%s, research_author=%s, research_language=%s, price=%s WHERE code=%s 
                         ''', (self._title, self._description, 
                               self._code, self.__subject, 
                               self.__authors, self.__language, 
                               self._price, prev_code))
        self.db.commit()
    
    def Delete_Research(self, code):
        self.cur.execute(''' DELETE FROM research WHERE code=%s ''', [(code)])
        self.db.commit()
    
    def Export_Research(self):
        sql = ''' SELECT research_title, code, research_subject, research_author, research_language, price, date FROM research '''
        self.cur.execute(sql)
        data = self.cur.fetchall()
        
        excel_file = Workbook("researches_report.xlsx")
        sheet1 = excel_file.add_worksheet()
        
        sheet1.write(0, 0, "Title")
        sheet1.write(0, 1, "Code")
        sheet1.write(0, 2, "Subject")
        sheet1.write(0, 3, "Author")
        sheet1.write(0, 4, "Language")
        sheet1.write(0, 5, "Price")
        sheet1.write(0, 6, "Date")
        
        row_number = 1
        for row in data:
            col_number = 0
            for item in row:
                sheet1.write(row_number, col_number, str(item))
                col_number += 1
            row_number += 1
        
        excel_file.close()  
    
    def DB_Connect(self):
        self.db = MySQLdb.connect(host='localhost', user='root', password='toor', db='my_library')
        self.cur = self.db.cursor()

class User_2:
    _name = ''
    _mail = ''
    _student_id = ''
    _phone = ''

class Students_2(User_2):
    __department = ''
    __date = datetime.datetime.now()
    
    def __init__(self):
        self.DB_Connect()
    
    def Show_Students(self):
        self.cur.execute(''' 
                         SELECT name, student_id, phone, mail, department FROM student 
                         ''')
        data = self.cur.fetchall()
        return data
    
    def Filter_Students(self, idx, src_data):
        if idx == 1:
            sql = ''' SELECT name, student_id, phone, department, date FROM student WHERE name=%s '''
            self.cur.execute(sql, [(src_data)])
        elif idx == 2:
            sql = ''' SELECT name, student_id, phone, department, date FROM student WHERE student_id=%s '''
            self.cur.execute(sql, [(src_data)])
        elif idx == 3:
            sql = ''' SELECT name, student_id, phone, department, date FROM student WHERE mail=%s '''
            self.cur.execute(sql, [(src_data)])
        elif idx == 4:
            sql = ''' SELECT name, student_id, phone, department, date FROM student WHERE phone=%s '''
            self.cur.execute(sql, [(src_data)])
        elif idx == 5:
            sql = ''' SELECT name, student_id, phone, department, date FROM student WHERE department=%s '''
            self.cur.execute(sql, [(src_data)])
        elif idx == 0:
            sql = ''' SELECT name, student_id, phone, department, date FROM student '''
            self.cur.execute(sql)
            
        
        data = self.cur.fetchall()
        return data
    
    def Sutdent_Search(self, idx, src_data):
        if idx == 0:
            sql = (''' SELECT * FROM student WHERE name=%s ''')
            self.cur.execute(sql, [(src_data)])
        elif idx == 1:
            sql = (''' SELECT * FROM student WHERE student_id=%s ''')
            self.cur.execute(sql, [(src_data)])
        elif idx == 2:
            sql = (''' SELECT * FROM student WHERE mail=%s ''')
            self.cur.execute(sql, [(src_data)])
        elif idx == 3:
            sql = (''' SELECT * FROM student WHERE phone=%s ''')
            self.cur.execute(sql, [(src_data)])
        
        data = self.cur.fetchone()
        return data
    
    def Add_Student(self, name, mail, student_id, phone, department, date):
        self._name = name
        self._mail = mail
        self._student_id = student_id
        self._phone = phone
        self.__department = department
        self.__date = date
        
        self.cur.execute(''' 
                         INSERT INTO student(name, student_id, mail, phone, department, date)
                         VALUES (%s, %s, %s, %s, %s, %s) 
                         ''', (self._name, self._student_id, self._mail, self._phone, self.__department, self.__date))
        
        ################## History
        sql = ''' INSERT INTO history(employee_id, operation_date, history_table, history_action) 
        VALUES (%s, %s, %s, %s) '''
        self.cur.execute(sql, (employee_id, self.__date, table[2], action[3]))
        
        self.db.commit()
    
    def Edit_Student(self, name, mail, student_id, phone, department, date, idx, src_data):
        self._name = name
        self._mail = mail
        self._student_id = student_id
        self._phone = phone
        self.__department = department
        self.__date = date
        if idx == 0:
            self.cur.execute(''' 
                         UPDATE student SET name=%s, student_id=%s, mail=%s, phone=%s, department=%s WHERE name=%s 
                         ''', (self._name, self._student_id, self._mail, self._phone, self.__department, src_data))
        elif idx == 1:
            self.cur.execute(''' 
                         UPDATE student SET name=%s, student_id=%s, mail=%s, phone=%s, department=%s WHERE student_id=%s 
                         ''', (self._name, self._student_id, self._mail, self._phone, self.__department, src_data))
        elif idx == 2:
            self.cur.execute(''' 
                         UPDATE student SET name=%s, student_id=%s, mail=%s, phone=%s, department=%s WHERE mail=%s 
                         ''', (self._name, self._student_id, self._mail, self._phone, self.__department, src_data))
        elif idx == 3:
            self.cur.execute(''' 
                         UPDATE student SET name=%s, student_id=%s, mail=%s, phone=%s, department=%s WHERE phone=%s 
                         ''', (self._name, self._student_id, self._mail, self._phone, self.__department, src_data))
        
        ################## History
        sql = ''' INSERT INTO history(employee_id, operation_date, history_table, history_action) 
        VALUES (%s, %s, %s, %s) '''
        self.cur.execute(sql, (employee_id, datetime.datetime.now(), table[2], action[4]))
        
        self.db.commit() 
    
    def Delete_Student(self, idx, src_data):
        if idx == 0:
            self.cur.execute(''' 
                         DELETE FROM student WHERE name=%s 
                         ''', [(src_data)])
        elif idx == 1:
            self.cur.execute(''' 
                          DELETE FROM student WHERE student_id=%s 
                         ''', [(src_data)])
        elif idx == 2:
            self.cur.execute(''' 
                          DELETE FROM student WHERE mail=%s 
                         ''', [(src_data)])
        elif idx == 3:
            self.cur.execute(''' 
                          DELETE FROM student WHERE phone=%s 
                         ''', [(src_data)])
        
        ################## History
        sql = ''' INSERT INTO history(employee_id, operation_date, history_table, history_action) 
        VALUES (%s, %s, %s, %s) '''
        self.cur.execute(sql, (employee_id, datetime.datetime.now(), table[2], action[5]))
        
        self.db.commit()
    
    def Export_Students(self):
        sql = ''' SELECT name, student_id, mail, phone, department FROM student '''
        self.cur.execute(sql)
        data = self.cur.fetchall()
        
        excel_file = Workbook("students_report.xlsx")
        sheet1 = excel_file.add_worksheet()
        
        sheet1.write(0, 0, "Student Name")
        sheet1.write(0, 1, "Student Id")
        sheet1.write(0, 2, "Student Mail")
        sheet1.write(0, 3, "Student Phone")
        sheet1.write(0, 4, "Student Department")
        
        row_number = 1
        for row in data:
            col_number = 0
            for item in row:
                sheet1.write(row_number, col_number, str(item))
                col_number += 1
            row_number += 1
        
        excel_file.close()
    
    ##############################################
    def Show_Students_Database(self):
        self.cur.execute(''' SELECT name, student_id, mail, phone, department, date FROM student ''')
        data = self.cur.fetchall()
        return data
    
    def Export_Students_Database(self):
        sql = ''' SELECT name, student_id, mail, phone, department, date FROM student '''
        self.cur.execute(sql)
        data = self.cur.fetchall()
        
        excel_file = Workbook("students_database_report.xlsx")
        sheet1 = excel_file.add_worksheet()
        
        sheet1.write(0, 0, "Student Name")
        sheet1.write(0, 1, "Student Id")
        sheet1.write(0, 2, "Student Mail")
        sheet1.write(0, 3, "Student Phone")
        sheet1.write(0, 4, "Student Department")
        sheet1.write(0, 5, "Sutdent Date")
        
        row_number = 1
        for row in data:
            col_number = 0
            for item in row:
                sheet1.write(row_number, col_number, str(item))
                col_number += 1
            row_number += 1
        
        excel_file.close()
    
    def DB_Connect(self):
        self.db = MySQLdb.connect(host='localhost', user='root', password='toor', db='my_library')
        self.cur = self.db.cursor()

class Sales_2:
    __title = ''
    __code = ''
    __sale_type = ''
    __sold_to = ''
    __price = 0.0
    __date = datetime.datetime.now()
    
    def __init__(self):
        self.DB_Connect()
    
    def Show_Sales(self):
        self.cur.execute(''' SELECT title, code, sales_type, sold_to, price, date FROM sales ''')
        data = self.cur.fetchall()
        return data
    
    def Filter_Sales(self, date_from, date_to):
        self.cur.execute(''' SELECT title, code, sales_type, sold_to, price, date FROM sales WHERE date BETWEEN %s AND %s ''', (date_from, date_to))
        data = self.cur.fetchall()
        return data
    
    def Add_Sale(self, title, code, sales_type, sold_to, price, date):
        self.__title = title
        self.__code = code
        self.__sale_type = sales_type
        self.__sold_to = sold_to
        self.__price = price
        self.__date = date
        
        self.cur.execute(''' INSERT INTO sales(title, code, sales_type, sold_to, price, date)
                         VALUES (%s, %s, %s, %s, %s, %s) 
                         ''', (self.__title, self.__code, self.__sale_type, self.__sold_to, self.__price, self.__date))
        self.db.commit()
    
    def DB_Connect(self):
        self.db = MySQLdb.connect(host='localhost', user='root', password='toor', db='my_library')
        self.cur = self.db.cursor()

class Librarian_2:
    __name = ''
    __mail = ''
    __national_id = ''
    __phone = ''
    __password = ''
    __date = datetime.datetime.now()
    
    def __init__(self):
        self.DB_Connect()
    
    def Show_Employee(self):
        self.cur.execute(''' 
                         SELECT name FROM employee 
                         ''')
        employees = self.cur.fetchall()
        return employees
    
    def Add_Employee(self, name, mail, national_id, phone, password, date, password2):
        self.__name = name
        self.__mail = mail
        self.__national_id = national_id
        self.__phone = phone
        self.__password = password
        self.__date = date
        x = 0
        if password == password2:
            self.cur.execute(''' 
                         INSERT INTO employee(name, mail, password, phone, date, national_id)
                         VALUES (%s, %s, %s, %s, %s, %s) 
                         ''', (self.__name, self.__mail, self.__password, self.__phone, self.__date, self.__national_id))
            ################## History
            sql = ''' INSERT INTO history(employee_id, operation_date, history_table, history_action) 
            VALUES (%s, %s, %s, %s) '''
            self.cur.execute(sql, (employee_id, self.__date, table[7], action[3]))
            
            self.db.commit()
            x = 1
        
        return x
    
    def Check_Employee(self):
        self.cur.execute(''' SELECT * FROM employee ''')
        data = self.cur.fetchall()
        return data
    
    def Edit_Employee(self, name, mail, national_id, phone, password, date):
        self.__name = name
        self.__mail = mail
        self.__national_id = national_id
        self.__phone = phone
        self.__password = password
        self.__date = date
        
        self.cur.execute(''' 
                UPDATE employee SET mail=%s, password=%s, phone=%s, date=%s, national_id=%s WHERE name=%s 
            ''', (self.__mail, self.__password, self.__phone, self.__date, int(self.__national_id), self.__name))
        
        ################## History
        sql = ''' INSERT INTO history(employee_id, operation_date, history_table, history_action) 
        VALUES (%s, %s, %s, %s) '''
        self.cur.execute(sql, (employee_id, self.__date, table[7], action[4]))
        
        self.db.commit()
    
    def Delete_Employee(self, name, password):
        self.__name = name
        self.__password = password
        sql = ''' DELETE FROM employee WHERE name=%s AND password=%s '''
        self.cur.execute(sql, (self.__name, self.__password))
        
        ################## History
        sql = ''' INSERT INTO history(employee_id, operation_date, history_table, history_action) 
        VALUES (%s, %s, %s, %s) '''
        self.cur.execute(sql, (employee_id, datetime.datetime.now(), table[7], action[5]))
        
        self.db.commit()
    
    def Add_Employee_Permission(self, name, *per):
        self.cur.execute(''' 
                         INSERT INTO employee_permissions(employee_name, book_tab, student_tab, 
                         history_tab, report_tab, setting_tab, database_tab, add_category, add_author, 
                         add_publisher, add_employee, edit_employee, delete_employee, add_book, edit_book, 
                         delete_book, export_book, add_student, edit_student, delete_student, export_student, 
                         set_as_admin, research_tab, sales) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
                         %s, %s, %s, %s, %s, %s, %s, %s) ''', (name, per[0], per[1], per[2], per[3], 
                                            per[4], per[5], per[6], per[7], per[8], 
                                            per[9], per[10], per[11], per[12], per[13], 
                                            per[14], per[15], per[16], per[17], per[18], 
                                            per[19], per[20], 1, 1))
        self.db.commit()
    
    def Show_Employee_Permissions(self, username):
        self.cur.execute(''' 
                                 SELECT * FROM employee_permissions WHERE employee_name=%s 
                                 ''', [(username)])
                
        user_permissions = self.cur.fetchone()
        return user_permissions
    
    def Show_Employees_Database(self):
        self.cur.execute(''' SELECT name, national_id, mail, phone, date FROM employee ''')
        data = self.cur.fetchall()
        return data

    def Export_Employees_Database(self):
        sql = ''' SELECT name, national_id, mail, phone, date FROM employee '''
        self.cur.execute(sql)
        data = self.cur.fetchall()
        
        excel_file = Workbook("employees_database_report.xlsx")
        sheet1 = excel_file.add_worksheet()
        
        sheet1.write(0, 0, "Employee Name")
        sheet1.write(0, 1, "Employee Id")
        sheet1.write(0, 2, "Employee Mail")
        sheet1.write(0, 3, "Employee Phone")
        sheet1.write(0, 4, "Employee Date")
        
        row_number = 1
        for row in data:
            col_number = 0
            for item in row:
                sheet1.write(row_number, col_number, str(item))
                col_number += 1
            row_number += 1
        
        excel_file.close()
    
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
    
    def DB_Connect(self):
        self.db = MySQLdb.connect(host='localhost', user='root', password='toor', db='my_library')
        self.cur = self.db.cursor()

class Reports_2:
    __date_from = datetime.datetime.now()
    __date_to = datetime.datetime.now()
    
    def __init__(self):
        self.DB_Connect()
    
    def Books_Report(self, date_from, date_to):
        self.cur.execute(''' SELECT code, title, category_id, author_id, book_date FROM book WHERE book_date BETWEEN %s AND %s ''', (date_from, date_to))
        data = self.cur.fetchall()
        return data
    
    def Students_Report(self, date_from, date_to):
        self.cur.execute(''' SELECT name, mail, phone, date FROM student WHERE date BETWEEN %s AND %s ''', (date_from, date_to))
        data = self.cur.fetchall()
        return data
    
    def DailyMovement_Report(self, date_from, date_to):
        self.cur.execute(''' SELECT book_id, student_id, book_from, book_to FROM daily_movement WHERE date BETWEEN %s AND %s ''', (date_from, date_to))
        data = self.cur.fetchall()
        return data
    
    def History_Report(self, date_from, date_to):
        self.cur.execute(''' SELECT employee_id, history_table, history_action, operation_date FROM history WHERE operation_date BETWEEN %s AND %s ''', (date_from, date_to))
        data = self.cur.fetchall()
        return data
    
    def DB_Connect(self):
        self.db = MySQLdb.connect(host='localhost', user='root', password='toor', db='my_library')
        self.cur = self.db.cursor()

class Database_2:
    ###### Composition Relation Between Reports and DataBase
    reports = Reports_2()
    books = Books_2()
    students = Students_2()
    employee = Librarian_2()
    
    # __books = Books()
    # __students = Students()
    # __employees = Employee()
    
    def Show_Books(self):
        return self.books.Show_Books_Database()
    
    def Export_Books(self):
        self.books.Export_Books_Database()
    
    def Show_Students(self):
        return self.students.Show_Students_Database()
    
    def Export_Students(self):
        self.students.Export_Students_Database()
    
    def Show_Employees(self):
        return self.employee.Show_Employees_Database()
    
    def Export_Employees(self):
        self.employee.Export_Employees_Database()
        
    ##################################################
    
    def Show_Authors(self):
        authors_2 = Author_2()
        return authors_2.Show_Authors_Database()
    
    def Export_Authors(self):
        authors = Author_2()
        authors.Export_Authors_Database()
    
    def Show_Publishers(self):
        publishers = Publisher_2()
        return publishers.Show_Publishers_Database()
    
    def Export_Publishers(self):
        publisher = Publisher_2()
        publisher.Export_Publishers_Database()
    
    ####################################################
    
    def Show_Books_Report(self, date_from, date_to):
        return self.reports.Books_Report(date_from, date_to)
    
    def Show_Students_Report(self, date_from, date_to):
        return self.reports.Students_Report(date_from, date_to)
    
    def Show_DailyMovement_Report(self, date_from, date_to):
        return self.reports.DailyMovement_Report(date_from, date_to)
    
    def Show_History_Report(self, date_from, date_to):
        return self.reports.History_Report(date_from, date_to)

class LibraryManagementSystem_2:
    __name = ''
    __password = ''
    database = Database_2()
    # __publication = Publications_2()
    # __users = User_2()
    librarian = Librarian_2()
    sales = Sales_2()
    
    ################################
    books = Books_2()
    students = Students_2()
    researches = Researches_2()
    
    def __init__(self):
        self.DB_Connect()
    
    def Login(self):
        self.cur.execute(''' SELECT national_id, name, password FROM employee ''')
        data = self.cur.fetchall()
        return data
    
    def Logout(self):
        ################## History
        sql = ''' INSERT INTO history(employee_id, operation_date, history_table, history_action) 
        VALUES (%s, %s, %s, %s) '''
        self.cur.execute(sql, (employee_id, datetime.datetime.now(), table[0], action[2]))
        self.db.commit()
    
    def Send_Mail_To_Reset_Password(self, mail, message):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login('librarymanagementsystem543@gmail.com', 'library#12345')
        server.sendmail('librarymanagementsystem543@gmail.com', mail, message)
    
    def DB_Connect(self):
        self.db = MySQLdb.connect(host='localhost', user='root', password='toor', db='my_library')
        self.cur = self.db.cursor()

###################################################################################

# MainUI,_ = loadUiType('main.ui')

class Main(QMainWindow, Main_Window):
    
    # lms = LibraryManagementSystem()
    # dbs = DataBase()
    lms_2 = LibraryManagementSystem_2()
    
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.UI_Changes()
        self.Set_Column_Width()
        self.Handle_Buttons()
        self.DB_Connect()
        
        ######################
        self.Show_All_Categories()
        self.Show_All_Authors()
        self.Show_All_Publishers()
        self.Show_All_Books()
        self.Show_All_Students()
        self.Show_Employee()
        self.Show_All_Daily_Works()
        self.Show_History()
        self.Show_All_Researches()
        self.Show_All_Sales()
        
        #################### DataBase 
        self.Show_Books_DataBase()
        self.Show_Students_DataBase()
        self.Show_Employees_DataBase()
        self.Show_Authors_DataBase()
        self.Show_Publishers_DataBase()
    
    #########################################################
    #### Connection between database and app
    def DB_Connect(self):
        try:
            self.db = MySQLdb.connect(host='localhost', user='root', password='toor', db='my_library')
            self.cur = self.db.cursor()
        except:
            print("There is an error in connection to database")
        else:
            print("Connection Accepted")
    #########################################################
    
    def UI_Changes(self):
        self.tabWidget.tabBar().setVisible(False)
        ##########
        self.pushButton_41.setVisible(False)
    
    def Set_Column_Width(self):
        self.tableWidget.setColumnWidth(0, 350)
        self.tableWidget.setColumnWidth(1, 110)
        self.tableWidget.setColumnWidth(2, 140)
        self.tableWidget.setColumnWidth(3, 170)
        
        self.tableWidget_6.setColumnWidth(0, 270)
        self.tableWidget_6.setColumnWidth(1, 120)
        self.tableWidget_6.setColumnWidth(2, 132)
        self.tableWidget_6.setColumnWidth(3, 135)
        self.tableWidget_6.setColumnWidth(4, 135)
        
        self.tableWidget_2.setColumnWidth(0, 180)
        self.tableWidget_2.setColumnWidth(1, 150)
        self.tableWidget_2.setColumnWidth(2, 150)
        self.tableWidget_2.setColumnWidth(3, 300)
        self.tableWidget_2.setColumnWidth(4, 215)
        
        self.tableWidget_3.setColumnWidth(0, 100)
        self.tableWidget_3.setColumnWidth(1, 270)
        self.tableWidget_3.setColumnWidth(2, 180)
        self.tableWidget_3.setColumnWidth(3, 180)
        self.tableWidget_3.setColumnWidth(4, 210)
        
        self.tableWidget_4.setColumnWidth(0, 240)
        self.tableWidget_4.setColumnWidth(1, 300)
        self.tableWidget_4.setColumnWidth(2, 160)
        self.tableWidget_4.setColumnWidth(3, 215)
        
        self.tableWidget_12.setColumnWidth(0, 270)
        self.tableWidget_12.setColumnWidth(1, 240)
        
        self.tableWidget_13.setColumnWidth(0, 240)
        self.tableWidget_13.setColumnWidth(1, 150)
        self.tableWidget_13.setColumnWidth(2, 150)
        self.tableWidget_13.setColumnWidth(3, 215)
        
        self.tableWidget_9.setColumnWidth(0, 240)
        self.tableWidget_9.setColumnWidth(1, 150)
        self.tableWidget_9.setColumnWidth(2, 300)
        self.tableWidget_9.setColumnWidth(3, 150)
        self.tableWidget_9.setColumnWidth(4, 215)
        
        self.tableWidget_10.setColumnWidth(0, 240)
        self.tableWidget_10.setColumnWidth(1, 500)
        
        self.tableWidget_11.setColumnWidth(0, 240)
        self.tableWidget_11.setColumnWidth(1, 500)
        
        self.tableWidget_8.setColumnWidth(0, 160)
        self.tableWidget_8.setColumnWidth(1, 120)
        self.tableWidget_8.setColumnWidth(2, 280)
        self.tableWidget_8.setColumnWidth(3, 140)
        self.tableWidget_8.setColumnWidth(4, 210)
        self.tableWidget_8.setColumnWidth(5, 200)
        
        self.tableWidget_5.setColumnWidth(0, 160)
        self.tableWidget_5.setColumnWidth(1, 140)
        self.tableWidget_5.setColumnWidth(2, 180)
        self.tableWidget_5.setColumnWidth(3, 210)
        
        self.tableWidget_15.setColumnWidth(0, 300)
        self.tableWidget_15.setColumnWidth(1, 100)
        self.tableWidget_15.setColumnWidth(2, 250)
        self.tableWidget_15.setColumnWidth(3, 250)
        self.tableWidget_15.setColumnWidth(4, 120)
        self.tableWidget_15.setColumnWidth(5, 100)
        
        self.tableWidget_14.setColumnWidth(0, 330)
        self.tableWidget_14.setColumnWidth(1, 100)
        self.tableWidget_14.setColumnWidth(2, 150)
        self.tableWidget_14.setColumnWidth(3, 150)
        self.tableWidget_14.setColumnWidth(4, 100)
        self.tableWidget_14.setColumnWidth(5, 200)
        
        self.dateEdit.setDate(datetime.date(2022, 1, 1))
        self.dateEdit_2.setDate(datetime.date.today())
        self.dateEdit_3.setDate(datetime.date(2022, 1, 1))
        self.dateEdit_4.setDate(datetime.date.today())
        self.dateEdit_6.setDate(datetime.date(2022, 1, 1))
        self.dateEdit_7.setDate(datetime.date.today())
        self.dateEdit_8.setDate(datetime.date(2022, 1, 1))
        self.dateEdit_9.setDate(datetime.date.today())
        self.dateEdit_5.setDate(datetime.date.today())
        self.dateEdit_11.setDate(datetime.date(2022, 1, 1))
        self.dateEdit_10.setDate(datetime.date.today())
    
    def Handle_Buttons(self):
        self.pushButton.clicked.connect(self.Open_Daily_Movement)
        self.pushButton_2.clicked.connect(self.Open_Books_Tab)
        self.pushButton_3.clicked.connect(self.Open_Students_Tab)
        self.pushButton_4.clicked.connect(self.Open_History_Tab)
        self.pushButton_5.clicked.connect(self.Open_Reports_Tab)
        self.pushButton_6.clicked.connect(self.Open_Settings_Tab)
        self.pushButton_7.clicked.connect(self.Open_Database_Tab)
        self.pushButton_46.clicked.connect(self.Open_Researches_Tab)
        
        ################# Settings
        self.pushButton_25.clicked.connect(self.Add_Category)
        self.pushButton_26.clicked.connect(self.Add_Author)
        self.pushButton_27.clicked.connect(self.Add_Publisher)
        self.pushButton_22.clicked.connect(self.Add_Employee)
        self.pushButton_20.clicked.connect(self.Check_Employee)
        self.pushButton_23.clicked.connect(self.Edit_Employee_Data)
        self.pushButton_24.clicked.connect(self.Delete_Employee)
        self.pushButton_29.clicked.connect(self.Add_Employee_Permission)
        
        ############# Books 
        self.pushButton_9.clicked.connect(self.Add_New_Book)
        self.pushButton_10.clicked.connect(self.Book_Search)
        self.pushButton_11.clicked.connect(self.Edit_Book)
        self.pushButton_12.clicked.connect(self.Delete_Book)
        self.pushButton_8.clicked.connect(self.All_Books_Filter)
        self.pushButton_37.clicked.connect(self.Export_Books)
        
        ############ Researches
        self.pushButton_49.clicked.connect(self.Add_New_Research)
        self.pushButton_47.clicked.connect(self.Filter_Researches)
        self.pushButton_50.clicked.connect(self.Research_Search)
        self.pushButton_51.clicked.connect(self.Edit_Research)
        self.pushButton_52.clicked.connect(self.Delete_Research)
        self.pushButton_48.clicked.connect(self.Export_Research)
        
        ########### Sales
        self.pushButton_43.clicked.connect(self.Open_Sales_Tab)
        self.pushButton_44.clicked.connect(self.Add_New_Sale)
        self.pushButton_45.clicked.connect(self.Show_Sales)
        
        ########### Students
        self.pushButton_14.clicked.connect(self.Add_New_Student)
        self.pushButton_15.clicked.connect(self.Search_Student)
        self.pushButton_16.clicked.connect(self.Edit_Student)
        self.pushButton_17.clicked.connect(self.Delete_Student)
        self.pushButton_13.clicked.connect(self.All_Students_Filter)
        self.pushButton_38.clicked.connect(self.Export_Students)
        
        ######### User Login
        self.pushButton_66.clicked.connect(self.User_Login_Permission)
        self.pushButton_41.clicked.connect(self.Hide_Password)
        self.pushButton_42.clicked.connect(self.Show_Password)
        ######## User Logout
        self.pushButton_67.clicked.connect(self.Handle_Logout)
        self.pushButton_68.clicked.connect(self.Handle_Reset_Password)
        self.pushButton_80.clicked.connect(self.Send_Email)
        self.pushButton_81.clicked.connect(self.Check_Verification_number)
        self.pushButton_79.clicked.connect(self.Set_New_Password)        
        
        self.pushButton_31.clicked.connect(self.Handle_Today_Work)
        
        ######## DataBase
        self.pushButton_36.clicked.connect(self.Export_Books_DataBase)
        self.pushButton_35.clicked.connect(self.Export_Students_DataBase)
        self.pushButton_34.clicked.connect(self.Export_Employees_DataBase)
        self.pushButton_33.clicked.connect(self.Export_Authors_DataBase)
        self.pushButton_32.clicked.connect(self.Export_Publishers_DataBase)
        
        self.pushButton_30.clicked.connect(self.Filter_History)
        
        ######## Reports
        self.pushButton_18.clicked.connect(self.Show_Books_Report)
        self.pushButton_19.clicked.connect(self.Show_Students_Report)
        self.pushButton_39.clicked.connect(self.Show_DailyMovement_Report)
        self.pushButton_40.clicked.connect(self.Show_History_Reports)
        
    
    #################################################################
    ##### User Login 
    def Handle_Login(self):
        pass
    
    
    def Handle_Logout(self):
        self.Open_Login_Tab()
        self.groupBox_11.setEnabled(False)
        self.pushButton_67.setEnabled(False)
        
        self.pushButton_2.setEnabled(False)
        self.pushButton_3.setEnabled(False)
        self.pushButton_4.setEnabled(False)
        self.pushButton_5.setEnabled(False)
        self.pushButton_6.setEnabled(False)
        self.pushButton_7.setEnabled(False)
        self.pushButton_37.setEnabled(False)
        self.pushButton_9.setEnabled(False)
        self.pushButton_11.setEnabled(False)
        self.pushButton_12.setEnabled(False)
        self.pushButton_38.setEnabled(False)
        self.pushButton_14.setEnabled(False)
        self.pushButton_16.setEnabled(False)
        self.pushButton_17.setEnabled(False)
        self.pushButton_22.setEnabled(False)
        self.pushButton_29.setEnabled(False)
        # self.User_Login_Permission()
        
        # self.lms.Logout()
        self.lms_2.Logout()
        self.Show_History()
    
    #################################################################################################################
    def Handle_Reset_Password(self):
        self.Open_Reset_Password_Tab()
    
    def Send_Email(self):
        username = self.lineEdit_92.text()
        
        self.cur.execute(''' SELECT mail FROM employee WHERE name=%s ''', [(username)])
        data = self.cur.fetchone()
        mail = data[0]
        
        n = randint(100001, 999999)
        global verification_number
        verification_number = n
        message = f"This message is sent for reset new passwor\nVerification number: {n}"
        
        try:
            # self.lms.Send_Mail_To_Reset_Password(mail, message)
            self.lms_2.Send_Mail_To_Reset_Password(mail, message)
        except:
            QMessageBox.about(self, "Error", "Something went wrong\n"
                              "Please make sure that your internet connection working")
        else:
            self.statusBar().showMessage("Email sent\nCheck your email to get verfication number")
    
    def Check_Verification_number(self):
        if self.lineEdit_77.text() == "":
            QMessageBox.about(self, "Error", "There is something wrong\n"
                              "make sure that you entered the name of employee that you want to reset its password")
        else:
            try:
                if verification_number == int(self.lineEdit_77.text()):
                    self.groupBox_22.setEnabled(True)
                else:
                    QMessageBox.about(self, "Error", "Entered verification number is not true\n"
                                    "please check your email and put the true verification number")
            except ValueError:
                QMessageBox.about(self, "Error", "verification number\n"
                                "you have to enter just numbers")
            except:
                QMessageBox.about(self, "Error", "something went wrong\n"
                                "make sure you press on button sent email")
    
    def Set_New_Password(self):
        username = self.lineEdit_92.text()
        new_password = self.lineEdit_91.text()
        
        sql = ''' UPDATE employee SET password=%s WHERE name=%s '''
        self.cur.execute(sql, (new_password, username))
        self.db.commit()
        
        self.statusBar().showMessage("New password has been set")
        
        self.Open_Login_Tab()
        
        self.lineEdit_92.clear()
        self.lineEdit_91.clear()
        self.lineEdit_77.clear()
    
    def Show_All_Daily_Works(self):
        self.tableWidget_6.setRowCount(0)
        self.tableWidget_6.insertRow(0)
        
        self.cur.execute(''' SELECT book_id, type, student_id, book_from, book_to FROM daily_movement ''')
        data = self.cur.fetchall()
        
        for row, form in enumerate(data):
            for col, item in enumerate(form):
                self.tableWidget_6.setItem(row, col, QTableWidgetItem(str(item)))
                col += 1
            
            row_position = self.tableWidget_6.rowCount()
            self.tableWidget_6.insertRow(row_position)
    
    
    def Handle_Today_Work(self):
        book_title = self.lineEdit_37.text()
        student_id = self.lineEdit_52.text()
        operation_type = self.comboBox_13.currentText()
        date_from = datetime.date.today()
        dt = self.dateEdit_5.text()
        date = datetime.datetime.now()
        global employee_id
        
        #### to change date format
        dt1 = dt.replace('/', '-')
        month = dt1[:dt1.find('-')]
        if len(month)==1:
            month = '0'+month
        day = dt1[dt1.find('-')+1:dt1.find('-', 3)]
        if len(day)==1:
            day = '0'+day
        year = dt1[dt1.find('-', 3)+1:]
        date_to = f'{year}-{month}-{day}'
        # print(date_from, date_to) 
        #############################
        
        sql = ''' INSERT INTO daily_movement(book_id, student_id, type, 
        date, book_from, book_to, employee_id) Values (%s, %s, %s, %s, 
        %s, %s, %s) '''
        self.cur.execute(sql, (book_title, student_id, operation_type, 
                               date, date_from, date_to, employee_id))
        
        ################## History
        if operation_type == "Rent":
            act = action[6]
        elif operation_type == "Retreive":
            act = action[7]
        else:
            act = action[8]
        sql = ''' INSERT INTO history(employee_id, operation_date, history_table, history_action) 
        VALUES (%s, %s, %s, %s) '''
        self.cur.execute(sql, (employee_id, datetime.datetime.now(), table[8], act))
        self.Show_History()
        
        self.db.commit()
        
        self.statusBar().showMessage("Operation Added")
        self.Show_All_Daily_Works()
        
        self.lineEdit_37.clear()
        self.lineEdit_52.clear()
        self.comboBox_13.setCurrentIndex(0)
    
    def Retreive_Today_Work(self):
        pass
    
    def User_Login_Permission(self):
        username = self.lineEdit_88.text()
        password = self.lineEdit_87.text()
        
        # data = self.lms.Login(username, password)
        data = self.lms_2.Login()
        
        for row in data:
            if row[1] == username and row[2]==password:
                global employee_id
                employee_id = row[0]
                
                ###### Load user permissions
                self.groupBox_11.setEnabled(True)
                self.pushButton_67.setEnabled(True)
                self.groupBox_24.setEnabled(False)
                
                # user_permissions = self.lms.staff.Show_Permissions(username)
                
                user_permissions = self.lms_2.librarian.Show_Employee_Permissions(username)
                
                if user_permissions[2] == 1:
                    self.pushButton_2.setEnabled(True)  # Book Tab
                if user_permissions[3] == 1:
                    self.pushButton_3.setEnabled(True)  # Student Tab
                if user_permissions[4] == 1:
                    self.pushButton_4.setEnabled(True)  # History Tab
                if user_permissions[5] == 1:
                    self.pushButton_5.setEnabled(True)  # Reports Tab
                if user_permissions[6] == 1:
                    self.pushButton_6.setEnabled(True)  # Settings Tab
                if user_permissions[7] == 1:
                    self.pushButton_7.setEnabled(True)  # Database Tab

                if user_permissions[8] == 1:
                    self.pushButton_25.setEnabled(True) # Add Category
                if user_permissions[9] == 1:
                    self.pushButton_26.setEnabled(True) # Add Author
                if user_permissions[10] == 1:
                    self.pushButton_27.setEnabled(True) # Add Publisher
                if user_permissions[11] == 1:
                    self.pushButton_22.setEnabled(True) # Add Employee
                if user_permissions[12] == 1:
                    self.pushButton_23.setEnabled(True) # Edit Employee
                if user_permissions[13] == 1:
                    self.pushButton_24.setEnabled(True) # Delete Employee
                
                if user_permissions[14] == 1:
                    self.pushButton_9.setEnabled(True)  # Add Book
                if user_permissions[15] == 1:
                    self.pushButton_11.setEnabled(True) # Edit Book
                if user_permissions[16] == 1:
                    self.pushButton_12.setEnabled(True) # Delete Book
                if user_permissions[17] == 1:
                    self.pushButton_37.setEnabled(True) # Export Book
                
                if user_permissions[18] == 1:
                    self.pushButton_14.setEnabled(True) # Add Student
                if user_permissions[19] == 1:
                    self.pushButton_16.setEnabled(True) # Edit Student
                if user_permissions[20] == 1:
                    self.pushButton_17.setEnabled(True) # Delete Student
                if user_permissions[21] == 1:
                    self.pushButton_38.setEnabled(True) # Export Student
                
                if user_permissions[22] == 1:
                    self.pushButton_29.setEnabled(True) # if Admin set Employee Permissions
                
                if user_permissions[23] == 1:
                    self.pushButton_46.setEnabled(True) # Scientific Researches
                
                if user_permissions[24] == 1:
                    self.pushButton_43.setEnabled(True) # Sale tab
                
                self.statusBar().showMessage("User Loged in")
                self.lineEdit_88.clear()
                self.lineEdit_87.clear()
                ################ History
                sql = ''' INSERT INTO history(employee_id, operation_date, history_table, history_action) 
                VALUES (%s, %s, %s, %s) '''
                self.cur.execute(sql, (employee_id, datetime.datetime.now(), table[0], action[1]))
                self.db.commit()
                self.Show_History()
            else:
                self.groupBox_24.setEnabled(True)
                self.lineEdit_88.clear()
                self.lineEdit_87.clear()
    
    def Show_Password(self):
        self.lineEdit_87.setEchoMode(QLineEdit.Normal)
        self.pushButton_41.setVisible(True)
        self.pushButton_42.setVisible(False)
        
    
    def Hide_Password(self):
        self.lineEdit_87.setEchoMode(QLineEdit.Password)
        self.pushButton_42.setVisible(True)
        self.pushButton_41.setVisible(False)
    
    ###############################################################
    ####### Books
    def Show_All_Books(self):
        self.tableWidget.setRowCount(0)
        self.tableWidget.insertRow(0)
        
        # data = self.lms.books.Show_Books()
        
        data = self.lms_2.books.Show_Books()
        
        for row, form in enumerate(data):
            for col, item in enumerate(form):
                self.tableWidget.setItem(row, col, QTableWidgetItem(str(item)))
                col += 1
            
            row_position = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row_position)
    
    def All_Books_Filter(self):
        category = self.comboBox.currentText()
        category_index = self.comboBox.currentIndex()
        
        # data = self.lms.books.Filter_Books(category_index, category)
        
        data = self.lms_2.books.Filter_Books(category_index,category)
        
        self.tableWidget.setRowCount(0)
        self.tableWidget.insertRow(0)
        
        for row, form, in enumerate(data):
            for col, item in enumerate(form):
                self.tableWidget.setItem(row, col, QTableWidgetItem(str(item)))
                col += 1
            
            row_position = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row_position)
    
    def Add_New_Book(self):
        title = self.lineEdit.text()
        description = self.textEdit.toPlainText()
        code = self.lineEdit_2.text()
        category = self.comboBox_2.currentText()
        author = self.comboBox_3.currentText()
        publisher = self.comboBox_4.currentText()
        price = self.lineEdit_3.text()
        date = datetime.datetime.now()
        
        # self.lms.books.Add_Book(title, description, code, category, author, publisher, price, date)
        
        self.lms_2.books.Add_Book(title, description, code, category, author, publisher, price, date)
        
        self.statusBar().showMessage("Book Added")
        self.Show_History()
        self.Show_All_Books()
        self.Show_Books_DataBase()
        
        self.lineEdit.clear()
        self.textEdit.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
        self.comboBox_2.setCurrentIndex(0)
        self.comboBox_3.setCurrentIndex(0)
        self.comboBox_4.setCurrentIndex(0)
    
    def Book_Search(self):
        code = self.lineEdit_4.text()
        
        # data = self.lms.books.Book_Search(code)
        
        data = self.lms_2.books.Book_Search(code)
        
        if data == None:
            QMessageBox.about(self, "Error", "There is no book has the code you entered")   
        else:
            self.lineEdit_5.setText(data[1])
            self.textEdit_2.setText(data[2])
            self.lineEdit_6.setText(str(data[3]))
            self.comboBox_5.setCurrentText(data[4])  
            self.comboBox_6.setCurrentText(data[5])
            self.comboBox_7.setCurrentText(data[6])
            self.lineEdit_7.setText(str(data[7]))
    
    def Edit_Book(self):
        title = self.lineEdit_5.text()
        description = self.textEdit_2.toPlainText()
        code = self.lineEdit_6.text()
        category = self.comboBox_5.currentText()
        author = self.comboBox_6.currentText()
        publisher = self.comboBox_7.currentText()
        price = self.lineEdit_7.text()
        prev_code = self.lineEdit_4.text()
        date = datetime.datetime.now()
        
        # self.lms.books.Edit_Book(title, description, code, category, author, publisher, price, date, prev_code)
        
        self.lms_2.books.Edit_Book(title, description, code, category, author, publisher, price, date, prev_code)
        
        self.statusBar().showMessage("Book Edited")
        self.Show_All_Books()
        self.Show_Books_DataBase()
        self.Show_History()
        
        self.lineEdit_5.clear()
        self.textEdit_2.clear()
        self.lineEdit_6.clear()
        self.comboBox_5.setCurrentIndex(0)
        self.comboBox_6.setCurrentIndex(0)
        self.comboBox_7.setCurrentIndex(0)
        self.lineEdit_7.clear()
        self.lineEdit_4.clear()
    
    def Delete_Book(self):
        code = self.lineEdit_4.text()
        
        # self.lms.books.Delete_Book(code)
        
        self.lms_2.books.Delete_Book(code)
        
        self.statusBar().showMessage("Book has been deleted")
        self.Show_All_Books()
        self.Show_Books_DataBase()
        self.Show_History()
        
        self.lineEdit_4.clear()
        self.lineEdit_5.clear()
        self.textEdit_2.clear()
        self.lineEdit_6.clear()
        self.comboBox_5.setCurrentIndex(0)
        self.comboBox_6.setCurrentIndex(0)
        self.comboBox_7.setCurrentIndex(0)
        self.lineEdit_7.clear()
    
    def Export_Books(self):
        
        # self.lms.books.Export_Books()
        
        self.lms_2.books.Export_Books()
        
        self.statusBar().showMessage("Book Report Exported Successfully")
    
    #########################################################
    #### Researches
    def Show_All_Researches(self):
        self.tableWidget_15.setRowCount(0)
        self.tableWidget_15.insertRow(0)
        
        data = self.lms_2.researches.Show_Researches()
        
        for row, form in enumerate(data):
            for col, item in enumerate(form):
                self.tableWidget_15.setItem(row, col, QTableWidgetItem(str(item)))
                col += 1
            
            row_position = self.tableWidget_15.rowCount()
            self.tableWidget_15.insertRow(row_position)
    
    def Filter_Researches(self):
        subject_idx = self.comboBox_14.currentIndex()
        subject_name = self.comboBox_14.currentText()
        
        data = self.lms_2.researches.Filter_Researchs(subject_idx, subject_name)
        
        self.tableWidget_15.setRowCount(0)
        self.tableWidget_15.insertRow(0)
        
        for row, form in enumerate(data):
            for col, item in enumerate(form):
                self.tableWidget_15.setItem(row, col, QTableWidgetItem(str(item)))
                col += 1
            
            row_position = self.tableWidget_15.rowCount()
            self.tableWidget_15.insertRow(row_position)
    
    def Add_New_Research(self):
        title = self.lineEdit_40.text()
        description = self.textEdit_3.toPlainText()
        code = self.lineEdit_41.text()
        subject = self.comboBox_17.currentText()
        author = self.lineEdit_47.text()
        language = self.comboBox_18.currentText()
        price = self.lineEdit_42.text()
        date = datetime.datetime.now()
        
        self.lms_2.researches.Add_Research(title, description, code, subject, author, language, price, date)
        
        self.statusBar().showMessage("Research Added Successfully")
        self.Show_All_Researches()
        
        self.lineEdit_40.clear()
        self.textEdit_3.clear()
        self.lineEdit_41.clear()
        self.comboBox_17.setCurrentIndex(0)
        self.lineEdit_47.clear()
        self.comboBox_18.setCurrentIndex(0)
        self.lineEdit_42.clear()
    
    def Research_Search(self):
        code = self.lineEdit_43.text()
        
        data = self.lms_2.researches.Research_Search(code)
        
        self.lineEdit_44.setText(data[1])
        self.textEdit_4.setText(data[2])
        self.lineEdit_46.setText(data[3])
        self.comboBox_19.setCurrentText(data[4])
        self.lineEdit_48.setText(data[5])
        self.comboBox_20.setCurrentText(data[6])
        self.lineEdit_45.setText(str(data[7]))
    
    def Edit_Research(self):
        prev_code = self.lineEdit_43.text()
        title = self.lineEdit_44.text()
        description = self.textEdit_4.toPlainText()
        code = self.lineEdit_46.text()
        subject = self.comboBox_19.currentText()
        author = self.lineEdit_48.text()
        language = self.comboBox_20.currentText()
        price = self.lineEdit_45.text()
        date = datetime.datetime.now()
        
        self.lms_2.researches.Edit_Research(title, description, code, subject, author, language, price, date, prev_code)
        
        self.statusBar().showMessage("Research Edited Successfully")
        self.Show_All_Researches()
        
        self.lineEdit_43.clear()
        self.lineEdit_44.clear()
        self.textEdit_4.clear()
        self.lineEdit_46.clear()
        self.comboBox_19.setCurrentIndex(0)
        self.lineEdit_48.clear()
        self.comboBox_20.setCurrentIndex(0)
        self.lineEdit_45.clear()
    
    def Delete_Research(self):
        code = self.lineEdit_43.text()
        
        self.lms_2.researches.Delete_Research(code)
        
        self.statusBar().showMessage("Research has been deleted")
        self.Show_All_Researches()
        
        self.lineEdit_43.clear()
        self.lineEdit_44.clear()
        self.textEdit_4.clear()
        self.lineEdit_46.clear()
        self.comboBox_19.setCurrentIndex(0)
        self.lineEdit_48.clear()
        self.comboBox_20.setCurrentIndex(0)
        self.lineEdit_45.clear()
    
    def Export_Research(self):
        
        self.lms_2.researches.Export_Research()
        
        self.statusBar().showMessage("Research has been Exported to Excel file")
    
    #########################################################
    #### Sales
    def Show_All_Sales(self):
        self.tableWidget_14.setRowCount(0)
        self.tableWidget_14.insertRow(0)
        
        data = self.lms_2.sales.Show_Sales()
        
        for row, form in enumerate(data):
            for col, item in enumerate(form):
                self.tableWidget_14.setItem(row, col, QTableWidgetItem(str(item)))
                col += 1
            
            row_position = self.tableWidget_14.rowCount()
            self.tableWidget_14.insertRow(row_position)
    def Show_Sales(self):
        dt = self.dateEdit_11.text()
        #### to change date format
        dt1 = dt.replace('/', '-')
        month = dt1[:dt1.find('-')]
        if len(month)==1:
            month = '0'+month
        day = dt1[dt1.find('-')+1:dt1.find('-', 3)]
        if len(day)==1:
            day = '0'+day
        year = dt1[dt1.find('-', 3)+1:]
        date_from = f'{year}-{month}-{day} 00:00:00'
        # print(date_from, date_to) 
        #############################
        dt2 = self.dateEdit_10.text()
        #### to change date format
        dt3 = dt2.replace('/', '-')
        month = dt3[:dt3.find('-')]
        if len(month)==1:
            month = '0'+month
        day = dt3[dt3.find('-')+1:dt3.find('-', 3)]
        if len(day)==1:
            day = '0'+day
        year = dt3[dt3.find('-', 3)+1:]
        date_to = f'{year}-{month}-{day} 00:00:00'
        # print(date_from, date_to) 
        #############################
        
        self.tableWidget_14.setRowCount(0)
        self.tableWidget_14.insertRow(0)
        
        data = self.lms_2.sales.Filter_Sales(date_from, date_to)
        
        for row, form in enumerate(data):
            for col, item in enumerate(form):
                self.tableWidget_14.setItem(row, col, QTableWidgetItem(str(item)))
                col += 1
            
            row_position = self.tableWidget_14.rowCount()
            self.tableWidget_14.insertRow(row_position)
    
    def Add_New_Sale(self):
        code = self.lineEdit_38.text()
        type_idx = self.comboBox_21.currentIndex()
        sales_type = ''
        sold_to = ''
        price = 0.0
        title = ''
        date = datetime.datetime.now()
        
        if type_idx == 0:
            sales_type = 'Book'
            self.cur.execute(''' SELECT title, price FROM book WHERE code=%s ''' ,[(code)])
        else:
            sales_type = 'Research'
            self.cur.execute(''' SELECT research_title, price FROM research WHERE code=%s ''', [(code)])
        
        data = self.cur.fetchone()
        title = data[0]
        price = data[1]
        
        if self.checkBox_22.isChecked() == True:
            sold_to = 'Student'
        else:
            sold_to = 'Client'
        
        self.lms_2.sales.Add_Sale(title, code, sales_type, sold_to, price, date)
        
        self.statusBar().showMessage("Sale Added")
        self.Show_All_Sales()
        
        self.lineEdit_38.clear()
        self.comboBox_21.setCurrentIndex(0)
        
        
    #########################################################
    #### Students
    def Show_All_Students(self):
        self.tableWidget_2.setRowCount(0)
        self.tableWidget_2.insertRow(0)
        
        # data = self.lms.students.Show_Students()
        
        data = self.lms_2.students.Show_Students()
        
        for row, form in enumerate(data):
            for col, item in enumerate(form):
                self.tableWidget_2.setItem(row, col, QTableWidgetItem(str(item)))
                col += 1
            
            row_position = self.tableWidget_2.rowCount()
            self.tableWidget_2.insertRow(row_position)
    
    def All_Students_Filter(self):
        src_data = self.lineEdit_8.text()
        idx = self.comboBox_8.currentIndex()
        
        # data = self.lms.students.Filter_Students(idx, src_data)
        
        data = self.lms_2.students.Filter_Students(idx, src_data)
        
        self.lineEdit_8.clear()
        
        self.tableWidget_2.setRowCount(0)
        self.tableWidget_2.insertRow(0)
        
        for row, form in enumerate(data):
            for col, item in enumerate(form):
                self.tableWidget_2.setItem(row, col, QTableWidgetItem(str(item)))
                col += 1
            
            row_position = self.tableWidget_2.rowCount()
            self.tableWidget_2.insertRow(row_position)
            
    
    def Add_New_Student(self):
        name = self.lineEdit_9.text()
        mail = self.lineEdit_10.text()
        id = self.lineEdit_11.text()
        phone = self.lineEdit_12.text()
        department = self.lineEdit_25.text()
        date = datetime.datetime.now()
        
        # self.lms.students.Add_Student(name, mail, id, phone, department, date)
        
        self.lms_2.students.Add_Student(name, mail, id, phone, department, date)
        
        self.statusBar().showMessage("Student Added")
        
        self.Show_All_Students()
        self.Show_Students_DataBase()
        self.Show_History()
        
        self.lineEdit_9.clear()
        self.lineEdit_10.clear()
        self.lineEdit_11.clear()
        self.lineEdit_12.clear()
        self.lineEdit_25.clear()
    
    def Search_Student(self):
        src_data = self.lineEdit_13.text()
        idx = self.comboBox_9.currentIndex()
        
        # data = self.lms.students.Sutdent_Search(idx, src_data)
        
        data = self.lms_2.students.Sutdent_Search(idx, src_data)
        
        self.lineEdit_14.setText(data[1])
        self.lineEdit_15.setText(data[3])
        self.lineEdit_16.setText(str(data[2]))
        self.lineEdit_17.setText(data[4])
        self.lineEdit_24.setText(data[5])
    
    def Edit_Student(self):
        src_data = self.lineEdit_13.text()
        idx = self.comboBox_9.currentIndex()
        
        name = self.lineEdit_14.text()
        mail = self.lineEdit_15.text()
        id = self.lineEdit_16.text()
        phone = self.lineEdit_17.text()
        department = self.lineEdit_24.text()
        date = datetime.datetime.now()
        
        # self.lms.students.Edit_Student(name, mail, id, phone, department, date, idx, src_data)
        
        self.lms_2.students.Edit_Student(name, mail, id, phone, department, date, idx, src_data)
        
        self.statusBar().showMessage("Student data has been Edited")
        self.Show_All_Students()
        self.Show_Students_DataBase()
        self.Show_History()
        
        self.lineEdit_13.clear()
        self.lineEdit_14.clear()
        self.lineEdit_15.clear()
        self.lineEdit_16.clear()
        self.lineEdit_17.clear()
        self.lineEdit_24.clear()
        self.comboBox_9.setCurrentIndex(0)
        
    
    def Delete_Student(self):
        src_data = self.lineEdit_13.text()
        idx = self.comboBox_9.currentIndex()
        
        # self.lms.students.Delete_Student(idx, src_data)
        
        self.lms_2.students.Delete_Student(idx, src_data)
        
        self.statusBar().showMessage("Student data has been Deleted")
        self.Show_All_Students()
        self.Show_Students_DataBase()
        self.Show_History()
        
        self.lineEdit_13.clear()
        self.lineEdit_14.clear()
        self.lineEdit_15.clear()
        self.lineEdit_16.clear()
        self.lineEdit_17.clear()
        self.lineEdit_24.clear()
        self.comboBox_9.setCurrentIndex(0)
    
    def Export_Students(self):
        
        # self.lms.students.Export_Students()
        
        self.lms_2.students.Export_Students()
        
        self.statusBar().showMessage("Students Report Exported Successfully")
    
    #########################################################
    #### Tabs
    def Open_Login_Tab(self):
        self.tabWidget.setCurrentIndex(0)
        print("Login Tab")
    
    def Open_Reset_Password_Tab(self):
        self.tabWidget.setCurrentIndex(1)
        print("Reset Password Tab")
    
    def Open_Daily_Movement(self):
        self.tabWidget.setCurrentIndex(2)
        print("Today Tab")
    
    def Open_Books_Tab(self):
        self.tabWidget.setCurrentIndex(3)
        self.tabWidget_2.setCurrentIndex(0)
        print("Books Tab")
    
    def Open_Sales_Tab(self):
        self.tabWidget.setCurrentIndex(9)
        self.tabWidget_7.setCurrentIndex(0)
        print("Sales Tab")
    
    def Open_Researches_Tab(self):
        self.tabWidget.setCurrentIndex(10)
        self.tabWidget_8.setCurrentIndex(0)
        print("Researches Tab")
    
    def Open_Students_Tab(self):
        self.tabWidget.setCurrentIndex(4)
        self.tabWidget_3.setCurrentIndex(0)
        print("Students Tab")
    
    def Open_History_Tab(self):
        self.tabWidget.setCurrentIndex(5)
        print("History Tab")
    
    def Open_Reports_Tab(self):
        self.tabWidget.setCurrentIndex(6)
        self.tabWidget_4.setCurrentIndex(0)
        print("Reports Tab")
    
    def Open_Settings_Tab(self):
        self.tabWidget.setCurrentIndex(7)
        self.tabWidget_5.setCurrentIndex(0)
        print("Settings Tab")
    
    def Open_Database_Tab(self):
        self.tabWidget.setCurrentIndex(8)
        self.tabWidget_6.setCurrentIndex(0)
        print("Database Tab")
    
    ########################################################
    ####### Settings
    def Add_Category(self):
        name = self.lineEdit_26.text()
        
        # self.lms.books.categories.Add_Cateogry(name)
        
        self.lms_2.books.categories.Add_Cateogry(name)
        
        self.statusBar().showMessage("Category Added")
        self.Show_All_Categories()
        self.Show_History()
        self.lineEdit_26.clear()
    
    def Add_Author(self):
        name = self.lineEdit_29.text()
        location = self.lineEdit_27.text()
        
        # self.lms.books.authors.Add_Author(name, location)
        
        self.lms_2.books.categories.Add_Cateogry(name, location)
        
        self.statusBar().showMessage("Author Added")
        self.Show_All_Authors()
        self.Show_Authors_DataBase()
        self.Show_History()
        self.lineEdit_29.clear()
        self.lineEdit_27.clear()
    
    def Add_Publisher(self):
        name = self.lineEdit_36.text()
        location = self.lineEdit_28.text()
        
        # self.lms.books.publishers.Add_Publisher(name, location)
        
        self.lms_2.books.publishers.Add_Publisher(name, location)
        
        self.statusBar().showMessage("Publisher Added")
        self.Show_All_Publishers()
        self.Show_Publishers_DataBase()
        self.Show_History()
        self.lineEdit_36.clear()
        self.lineEdit_28.clear()
    
    def Show_All_Categories(self):
        self.comboBox_10.clear()
        self.comboBox.clear()
        self.comboBox_2.clear()
        self.comboBox_5.clear()
        
        # categories = self.lms.books.categories.Show_Categories()
        
        categories = self.lms_2.books.categories.Show_Categories()
        
        self.comboBox.addItem("- - - - - - - - - ")
        for category in categories:
            self.comboBox_10.addItem(category[0])
            self.comboBox.addItem(category[0])
            self.comboBox_2.addItem(category[0])
            self.comboBox_5.addItem(category[0])
    
    def Show_All_Authors(self):
        self.comboBox_6.clear()
        self.comboBox_3.clear()
        
        # authors = self.lms.books.authors.Show_Authors()
        
        authors = self.lms_2.books.authors.Show_Authors()
        
        for author in authors:
            self.comboBox_6.addItem(author[0])
            self.comboBox_3.addItem(author[0])
    
    def Show_All_Publishers(self):
        self.comboBox_4.clear()
        self.comboBox_7.clear()
        
        # publishers = self.lms.books.publishers.Show_Publishers()
        
        publishers = self.lms_2.books.publishers.Show_Publishers()
        
        for publisher in publishers:
            self.comboBox_4.addItem(publisher[0])
            self.comboBox_7.addItem(publisher[0])
    
    #######################################################
    ###### Employee
    def Show_Employee(self):
        self.comboBox_16.clear()
        self.comboBox_11.clear()
        
        # employees = self.lms.staff.Show()
        
        employees = self.lms_2.librarian.Show_Employee()
        
        self.comboBox_16.addItem("- - - - - - - -")
        for employee in employees:
            self.comboBox_11.addItem(employee[0])
            self.comboBox_16.addItem(employee[0])
    
    def Add_Employee(self):
        name = self.lineEdit_18.text()
        mail = self.lineEdit_19.text()
        id = self.lineEdit_20.text()
        phone = self.lineEdit_21.text()
        password = self.lineEdit_22.text()
        password2 = self.lineEdit_23.text()
        date = datetime.datetime.now()
        
        # x = self.lms.staff.Add(name, mail, id, phone, password, date, password2)
        
        x = self.lms_2.librarian.Add_Employee(name, mail, id, phone, password, date, password2);
        
        if x == 1:
            self.statusBar().showMessage("Employee Added")
            self.Show_Employee()
            self.Show_Employees_DataBase()
            self.Show_History()
        else:
            self.statusBar().showMessage("Passwords do not match")
        
        self.lineEdit_18.clear()
        self.lineEdit_19.clear()
        self.lineEdit_20.clear()
        self.lineEdit_21.clear()
        self.lineEdit_22.clear()
        self.lineEdit_23.clear()
    
    def Check_Employee(self):
        name = self.lineEdit_30.text()
        password = self.lineEdit_34.text()
        
        # data = self.lms.staff.Check()
        
        data = self.lms_2.librarian.Check_Employee()
        
        for row in data:
            if row[1] == name and row[3] == password:
                self.groupBox_3.setEnabled(True)
                self.lineEdit_33.setText(row[4])
                self.lineEdit_32.setText(str(row[6]))
                self.lineEdit_31.setText(row[2])
                self.lineEdit_35.setText(row[3])
    
    def Edit_Employee_Data(self):
        name = self.lineEdit_30.text()
        mail = self.lineEdit_31.text()
        id = self.lineEdit_32.text()
        phone = self.lineEdit_33.text()
        password = self.lineEdit_35.text()
        date = datetime.datetime.now()
        
        # self.lms.staff.Edit(name, mail, id, phone, password, date)
        
        self.lms_2.librarian.Edit_Employee(name, mail, id, phone, password, date)
        
        self.Show_Employee()
        self.Show_Employees_DataBase()
        self.Show_History()
        self.statusBar().showMessage("Employee Edited")
        
        self.lineEdit_30.clear()
        self.lineEdit_31.clear()
        self.lineEdit_32.clear()
        self.lineEdit_33.clear()
        self.lineEdit_35.clear()
        self.lineEdit_34.clear()
    
    def Delete_Employee(self):
        name = self.lineEdit_30.text()
        password = self.lineEdit_34.text()
        
        # self.lms.staff.Delete(name, password)
        
        self.lms_2.librarian.Delete_Employee(name, password)
        
        self.statusBar().showMessage("Employee Deleted")
        self.Show_Employee()
        self.Show_Employees_DataBase()
        self.Show_History()
        
        self.lineEdit_30.clear()
        self.lineEdit_31.clear()
        self.lineEdit_32.clear()
        self.lineEdit_33.clear()
        self.lineEdit_35.clear()
        self.lineEdit_34.clear()
    
    def Add_Employee_Permission(self):
        employee_name = self.comboBox_11.currentText()
        books_tab = 0
        student_tab = 0
        history_tab = 0
        reports_tab = 0
        settings_tab = 0
        database_tab = 0
        
        add_category = 0
        add_author = 0
        add_publisher = 0
        add_employee = 0
        edit_employee = 0
        delete_employee = 0
        
        add_book = 0
        edit_book = 0
        delete_book = 0
        export_book = 0
        
        add_student = 0
        edit_student = 0
        delete_student = 0
        export_student = 0
        
        set_as_admin = 0
        
        if self.checkBox.isChecked() == True:
            books_tab = 1
        if self.checkBox_2.isChecked() == True:
            student_tab = 1
        if self.checkBox_3.isChecked() == True:
            history_tab = 1
        if self.checkBox_4.isChecked() == True:
            reports_tab = 1
        if self.checkBox_5.isChecked() == True:
            settings_tab = 1
        if self.checkBox_6.isChecked() == True:
            database_tab = 1
        
        if self.checkBox_15.isChecked() == True:
            add_category = 1
        if self.checkBox_16.isChecked() == True:
            add_author = 1
        if self.checkBox_17.isChecked() == True:
            add_publisher = 1
        if self.checkBox_18.isChecked() == True:
            add_employee = 1
        if self.checkBox_19.isChecked() == True:
            edit_employee = 1
        if self.checkBox_20.isChecked() == True:
            delete_employee = 1
        
        if self.checkBox_7.isChecked() == True:
            add_book = 1
        if self.checkBox_8.isChecked() == True:
            edit_book = 1
        if self.checkBox_9.isChecked() == True:
            delete_book = 1
        if self.checkBox_10.isChecked() == True:
            export_book = 1
        
        if self.checkBox_11.isChecked() == True:
            add_student = 1
        if self.checkBox_12.isChecked() == True:
            edit_student = 1
        if self.checkBox_13.isChecked() == True:
            delete_student = 1
        if self.checkBox_14.isChecked() == True:
            export_student = 1
        
        if self.checkBox_21.isChecked() == True:
            set_as_admin = 1
        
        librarian = Librarian()
        
        # librarian.Add_Employee_Permissions(employee_name, books_tab, student_tab, history_tab, reports_tab, 
        #                                     settings_tab, database_tab, add_category, add_author, add_publisher, 
        #                                     add_employee, edit_employee, delete_employee, add_book, edit_book, 
        #                                     delete_book, export_book, add_student, edit_student, delete_student, 
        #                                     export_student, set_as_admin)
        
        self.lms_2.librarian.Add_Employee_Permission(employee_name, books_tab, student_tab, history_tab, reports_tab, 
                                            settings_tab, database_tab, add_category, add_author, add_publisher, 
                                            add_employee, edit_employee, delete_employee, add_book, edit_book, 
                                            delete_book, export_book, add_student, edit_student, delete_student, 
                                            export_student, set_as_admin)
        
        self.statusBar().showMessage("Employee Permissions Added")
    
    ################################################################
    ###### History
    def Show_History(self):
        self.tableWidget_5.setRowCount(0)
        self.tableWidget_5.insertRow(0)
        
        self.cur.execute(''' SELECT employee_id, history_action, history_table, operation_date FROM history ''')
        data = self.cur.fetchall()
        
        for row, form in enumerate(data):
            for col, item in enumerate(form):
                if col == 0:
                    self.cur.execute(''' SELECT name FROM employee WHERE national_id=%s ''', [(item)])
                    employee_name = self.cur.fetchone()
                    # print(employee_name)
                    self.tableWidget_5.setItem(row, col, QTableWidgetItem(str(employee_name[0])))
                else:
                    self.tableWidget_5.setItem(row, col, QTableWidgetItem(str(item)))
                col += 1
            
            row_position = self.tableWidget_5.rowCount()
            self.tableWidget_5.insertRow(row_position)
    
    def Filter_History(self):
        employee_name = self.comboBox_16.currentText()
        action_text = self.comboBox_12.currentText()
        table_text = self.comboBox_15.currentText()
        employee_idx = self.comboBox_16.currentIndex()
        action_idx = self.comboBox_12.currentIndex()
        table_idx = self.comboBox_15.currentIndex()
        
        if action_idx == 0:
            action_text = '- - - - - - -'
        if table_idx == 0:
            table_text = '- - - - - - -'
        if table_idx == 0 and action_idx == 0 and employee_idx == 0:
            sql = ''' SELECT employee_id, history_action, history_table, operation_date FROM history '''
            self.cur.execute(sql)
            
            self.tableWidget_5.setRowCount(0)
            self.tableWidget_5.insertRow(0)
        
            data = self.cur.fetchall()
        
            for row, form in enumerate(data):
                for col, item in enumerate(form):
                    if col == 0:
                        self.cur.execute(''' SELECT name FROM employee WHERE national_id=%s ''', [(item)])
                        employee_name = self.cur.fetchone()
                        # print(employee_name)
                        self.tableWidget_5.setItem(row, col, QTableWidgetItem(str(employee_name[0])))
                    else:
                        self.tableWidget_5.setItem(row, col, QTableWidgetItem(str(item)))
                    col += 1
            
                row_position = self.tableWidget_5.rowCount()
                self.tableWidget_5.insertRow(row_position)
        
        if employee_idx == 0:
            
            if action_idx == 0 and table_idx == 0:
                sql = ''' SELECT employee_id, history_action, history_table, operation_date FROM history '''
                self.cur.execute(sql)
            
                self.tableWidget_5.setRowCount(0)
                self.tableWidget_5.insertRow(0)
        
                data = self.cur.fetchall()
        
                for row, form in enumerate(data):
                    for col, item in enumerate(form):
                        if col == 0:
                            self.cur.execute(''' SELECT name FROM employee WHERE national_id=%s ''', [(item)])
                            employee_name = self.cur.fetchone()
                            # print(employee_name)
                            self.tableWidget_5.setItem(row, col, QTableWidgetItem(str(employee_name[0])))
                        else:
                            self.tableWidget_5.setItem(row, col, QTableWidgetItem(str(item)))
                        col += 1

                    row_position = self.tableWidget_5.rowCount()
                    self.tableWidget_5.insertRow(row_position)
            elif action_idx == 0 and table_idx != 0:
                sql = ''' SELECT employee_id, history_action, history_table, operation_date FROM history 
                WHERE history_table=%s '''
                self.cur.execute(sql, [(table_text)])

                self.tableWidget_5.setRowCount(0)
                self.tableWidget_5.insertRow(0)

                data = self.cur.fetchall()

                for row, form in enumerate(data):
                    for col, item in enumerate(form):
                        if col == 0:
                            self.cur.execute(''' SELECT name FROM employee WHERE national_id=%s ''', [(item)])
                            employee_name = self.cur.fetchone()
                            # print(employee_name)
                            self.tableWidget_5.setItem(row, col, QTableWidgetItem(str(employee_name[0])))
                        else:
                            self.tableWidget_5.setItem(row, col, QTableWidgetItem(str(item)))
                        col += 1

                    row_position = self.tableWidget_5.rowCount()
                    self.tableWidget_5.insertRow(row_position)
            elif action_idx != 0 and table_idx == 0:
                sql = ''' SELECT employee_id, history_action, history_table, operation_date FROM history 
                WHERE history_action=%s '''
                self.cur.execute(sql, [(action_text)])

                self.tableWidget_5.setRowCount(0)
                self.tableWidget_5.insertRow(0)
        
                data = self.cur.fetchall()

                for row, form in enumerate(data):
                    for col, item in enumerate(form):
                        if col == 0:
                            self.cur.execute(''' SELECT name FROM employee WHERE national_id=%s ''', [(item)])
                            employee_name = self.cur.fetchone()
                            # print(employee_name)
                            self.tableWidget_5.setItem(row, col, QTableWidgetItem(str(employee_name[0])))
                        else:
                            self.tableWidget_5.setItem(row, col, QTableWidgetItem(str(item)))
                        col += 1
                    
                    row_position = self.tableWidget_5.rowCount()
                    self.tableWidget_5.insertRow(row_position)
            elif action_idx !=0 and table_idx != 0:
                sql = ''' SELECT employee_id, history_action, history_table, operation_date FROM history 
                WHERE history_action=%s AND history_table=%s '''
                self.cur.execute(sql, (action_text, table_text))

                self.tableWidget_5.setRowCount(0)
                self.tableWidget_5.insertRow(0)

                data = self.cur.fetchall()

                for row, form in enumerate(data):
                    for col, item in enumerate(form):
                        if col == 0:
                            self.cur.execute(''' SELECT name FROM employee WHERE national_id=%s ''', [(item)])
                            employee_name = self.cur.fetchone()
                            # print(employee_name)
                            self.tableWidget_5.setItem(row, col, QTableWidgetItem(str(employee_name[0])))
                        else:
                            self.tableWidget_5.setItem(row, col, QTableWidgetItem(str(item)))
                        col += 1

                    row_position = self.tableWidget_5.rowCount()
                    self.tableWidget_5.insertRow(row_position)
            #######################################################################################
        elif employee_idx != 0:
            
            self.cur.execute(''' SELECT national_id FROM employee WHERE name=%s ''', [(employee_name)])
            dta = self.cur.fetchone()
            employee_national_id = dta[0]
            
            if action_idx == 0 and table_idx == 0:
                sql = ''' SELECT employee_id, history_action, history_table, operation_date FROM history 
                WHERE employee_id=%s '''
                self.cur.execute(sql, [(employee_national_id)])
            
                self.tableWidget_5.setRowCount(0)
                self.tableWidget_5.insertRow(0)
        
                data = self.cur.fetchall()
        
                for row, form in enumerate(data):
                    for col, item in enumerate(form):
                        if col == 0:
                            self.cur.execute(''' SELECT name FROM employee WHERE national_id=%s ''', [(item)])
                            employee_name = self.cur.fetchone()
                            # print(employee_name)
                            self.tableWidget_5.setItem(row, col, QTableWidgetItem(str(employee_name[0])))
                        else:
                            self.tableWidget_5.setItem(row, col, QTableWidgetItem(str(item)))
                        col += 1

                    row_position = self.tableWidget_5.rowCount()
                    self.tableWidget_5.insertRow(row_position)
            elif action_idx == 0 and table_idx != 0:
                sql = ''' SELECT employee_id, history_action, history_table, operation_date FROM history 
                WHERE history_table=%s AND employee_id=%s '''
                self.cur.execute(sql, (table_text, employee_national_id))

                self.tableWidget_5.setRowCount(0)
                self.tableWidget_5.insertRow(0)

                data = self.cur.fetchall()

                for row, form in enumerate(data):
                    for col, item in enumerate(form):
                        if col == 0:
                            self.cur.execute(''' SELECT name FROM employee WHERE national_id=%s ''', [(item)])
                            employee_name = self.cur.fetchone()
                            # print(employee_name)
                            self.tableWidget_5.setItem(row, col, QTableWidgetItem(str(employee_name[0])))
                        else:
                            self.tableWidget_5.setItem(row, col, QTableWidgetItem(str(item)))
                        col += 1

                    row_position = self.tableWidget_5.rowCount()
                    self.tableWidget_5.insertRow(row_position)
            elif action_idx != 0 and table_idx == 0:
                sql = ''' SELECT employee_id, history_action, history_table, operation_date FROM history 
                WHERE history_action=%s AND employee_id=%s '''
                self.cur.execute(sql, (action_text, employee_national_id))

                self.tableWidget_5.setRowCount(0)
                self.tableWidget_5.insertRow(0)
        
                data = self.cur.fetchall()

                for row, form in enumerate(data):
                    for col, item in enumerate(form):
                        if col == 0:
                            self.cur.execute(''' SELECT name FROM employee WHERE national_id=%s ''', [(item)])
                            employee_name = self.cur.fetchone()
                            # print(employee_name)
                            self.tableWidget_5.setItem(row, col, QTableWidgetItem(str(employee_name[0])))
                        else:
                            self.tableWidget_5.setItem(row, col, QTableWidgetItem(str(item)))
                        col += 1
                    
                    row_position = self.tableWidget_5.rowCount()
                    self.tableWidget_5.insertRow(row_position)
            elif action_idx !=0 and table_idx != 0:
                sql = ''' SELECT employee_id, history_action, history_table, operation_date FROM history 
                WHERE history_action=%s AND history_table=%s AND employee_id=%s'''
                self.cur.execute(sql, (action_text, table_text, employee_national_id))

                self.tableWidget_5.setRowCount(0)
                self.tableWidget_5.insertRow(0)

                data = self.cur.fetchall()

                for row, form in enumerate(data):
                    for col, item in enumerate(form):
                        if col == 0:
                            self.cur.execute(''' SELECT name FROM employee WHERE national_id=%s ''', [(item)])
                            employee_name = self.cur.fetchone()
                            # print(employee_name)
                            self.tableWidget_5.setItem(row, col, QTableWidgetItem(str(employee_name[0])))
                        else:
                            self.tableWidget_5.setItem(row, col, QTableWidgetItem(str(item)))
                        col += 1

                    row_position = self.tableWidget_5.rowCount()
                    self.tableWidget_5.insertRow(row_position)
    
    ################################################################
    ###### Reports
    def Show_Books_Report(self):
        dt = self.dateEdit.text()
        #### to change date format
        dt1 = dt.replace('/', '-')
        month = dt1[:dt1.find('-')]
        if len(month)==1:
            month = '0'+month
        day = dt1[dt1.find('-')+1:dt1.find('-', 3)]
        if len(day)==1:
            day = '0'+day
        year = dt1[dt1.find('-', 3)+1:]
        date_from = f'{year}-{month}-{day} 00:00:00'
        # print(date_from, date_to) 
        #############################
        dt2 = self.dateEdit_2.text()
        #### to change date format
        dt3 = dt2.replace('/', '-')
        month = dt3[:dt3.find('-')]
        if len(month)==1:
            month = '0'+month
        day = dt3[dt3.find('-')+1:dt3.find('-', 3)]
        if len(day)==1:
            day = '0'+day
        year = dt3[dt3.find('-', 3)+1:]
        date_to = f'{year}-{month}-{day} 00:00:00'
        # print(date_from, date_to) 
        #############################
        self.tableWidget_3.setRowCount(0)
        self.tableWidget_3.insertRow(0)
        
        # data = self.dbs.Show_Books_Report(date_from, date_to)
        
        data = self.lms_2.database.Show_Books_Report(date_from, date_to)
        
        for row, form in enumerate(data):
            for col, item in enumerate(form):
                self.tableWidget_3.setItem(row, col, QTableWidgetItem(str(item)))
                col += 1
            
            row_position = self.tableWidget_3.rowCount()
            self.tableWidget_3.insertRow(row_position)
    
    def Show_Students_Report(self):
        dt = self.dateEdit_3.text()
        #### to change date format
        dt1 = dt.replace('/', '-')
        month = dt1[:dt1.find('-')]
        if len(month)==1:
            month = '0'+month
        day = dt1[dt1.find('-')+1:dt1.find('-', 3)]
        if len(day)==1:
            day = '0'+day
        year = dt1[dt1.find('-', 3)+1:]
        date_from = f'{year}-{month}-{day} 00:00:00'
        # print(date_from, date_to) 
        #############################
        dt2 = self.dateEdit_4.text()
        #### to change date format
        dt3 = dt2.replace('/', '-')
        month = dt3[:dt3.find('-')]
        if len(month)==1:
            month = '0'+month
        day = dt3[dt3.find('-')+1:dt3.find('-', 3)]
        if len(day)==1:
            day = '0'+day
        year = dt3[dt3.find('-', 3)+1:]
        date_to = f'{year}-{month}-{day} 00:00:00'
        # print(date_from, date_to) 
        #############################
        
        self.tableWidget_4.setRowCount(0)
        self.tableWidget_4.insertRow(0)
        
        # data = self.dbs.Show_Students_Report(date_from, date_to)
        
        data = self.lms_2.database.Show_Students_Report(date_from, date_to)
        
        for row, form in enumerate(data):
            for col, item in enumerate(form):
                self.tableWidget_4.setItem(row, col, QTableWidgetItem(str(item)))
                col += 1
            
            row_position = self.tableWidget_4.rowCount()
            self.tableWidget_4.insertRow(row_position)
    
    def Show_DailyMovement_Report(self):
        dt = self.dateEdit_6.text()
        #### to change date format
        dt1 = dt.replace('/', '-')
        month = dt1[:dt1.find('-')]
        if len(month)==1:
            month = '0'+month
        day = dt1[dt1.find('-')+1:dt1.find('-', 3)]
        if len(day)==1:
            day = '0'+day
        year = dt1[dt1.find('-', 3)+1:]
        date_from = f'{year}-{month}-{day} 00:00:00'
        # print(date_from, date_to) 
        #############################
        dt2 = self.dateEdit_7.text()
        #### to change date format
        dt3 = dt2.replace('/', '-')
        month = dt3[:dt3.find('-')]
        if len(month)==1:
            month = '0'+month
        day = dt3[dt3.find('-')+1:dt3.find('-', 3)]
        if len(day)==1:
            day = '0'+day
        year = dt3[dt3.find('-', 3)+1:]
        date_to = f'{year}-{month}-{day} 00:00:00'
        # print(date_from, date_to) 
        #############################
        
        self.tableWidget_12.setRowCount(0)
        self.tableWidget_12.insertRow(0)
        
        # data = self.dbs.Show_DailyMovement_Report(date_from, date_to)
        
        data = self.lms_2.database.Show_DailyMovement_Report(date_from, date_to)
        
        for row, form in enumerate(data):
            for col, item in enumerate(form):
                if col == 1:
                    self.cur.execute(''' SELECT name FROM student WHERE student_id=%s ''', [(item)])
                    student_name = self.cur.fetchone()
                    if student_name != None:
                        self.tableWidget_12.setItem(row, col, QTableWidgetItem(str(student_name[0])))
                else:
                    self.tableWidget_12.setItem(row, col, QTableWidgetItem(str(item)))
                col += 1
            
            row_position = self.tableWidget_12.rowCount()
            self.tableWidget_12.insertRow(row_position)
    
    def Show_History_Reports(self):
        dt = self.dateEdit_8.text()
        #### to change date format
        dt1 = dt.replace('/', '-')
        month = dt1[:dt1.find('-')]
        if len(month)==1:
            month = '0'+month
        day = dt1[dt1.find('-')+1:dt1.find('-', 3)]
        if len(day)==1:
            day = '0'+day
        year = dt1[dt1.find('-', 3)+1:]
        date_from = f'{year}-{month}-{day} 00:00:00'
        # print(date_from, date_to) 
        #############################
        dt2 = self.dateEdit_9.text()
        #### to change date format
        dt3 = dt2.replace('/', '-')
        month = dt3[:dt3.find('-')]
        if len(month)==1:
            month = '0'+month
        day = dt3[dt3.find('-')+1:dt3.find('-', 3)]
        if len(day)==1:
            day = '0'+day
        year = dt3[dt3.find('-', 3)+1:]
        date_to = f'{year}-{month}-{day} 00:00:00'
        # print(date_from, date_to) 
        #############################
        
        self.tableWidget_13.setRowCount(0)
        self.tableWidget_13.insertRow(0)
        
        # data = self.dbs.Show_History_Report(date_from, date_to)
        
        data = self.lms_2.database.Show_History_Report(date_from, date_to)
        
        for row, form in enumerate(data):
            for col, item in enumerate(form):
                if col == 0:
                    self.cur.execute(''' SELECT name FROM employee WHERE national_id=%s ''', [(item)])
                    employee_name = self.cur.fetchone()
                    self.tableWidget_13.setItem(row, col, QTableWidgetItem(str(employee_name[0])))
                else:
                    self.tableWidget_13.setItem(row, col, QTableWidgetItem(str(item)))
                col += 1
            
            row_position = self.tableWidget_13.rowCount()
            self.tableWidget_13.insertRow(row_position)
        
    ################################################################
    ###### DataBase
    def Show_Books_DataBase(self):
        self.tableWidget_7.setRowCount(0)
        self.tableWidget_7.insertRow(0)
        
        # books = Books()
        # data = self.dbs.Show_Books(books)
        data = self.lms_2.database.Show_Books()
        
        for row, form in enumerate(data):
            for col, item in enumerate(form):
                self.tableWidget_7.setItem(row, col, QTableWidgetItem(str(item)))
                col += 1
            
            row_position = self.tableWidget_7.rowCount()
            self.tableWidget_7.insertRow(row_position)
    
    def Export_Books_DataBase(self):
        
        # books = Books()
        # self.dbs.Export_Books(books)
        self.lms_2.database.Export_Books()
        
        self.statusBar().showMessage("Books In Database Exported Successfully")
    
    def Show_Students_DataBase(self):
        self.tableWidget_8.setRowCount(0)
        self.tableWidget_8.insertRow(0)
        
        # students = Students()
        # data = self.dbs.Show_Students(students)
        data = self.lms_2.database.Show_Students()
        
        for row, form in enumerate(data):
            for col, item in enumerate(form):
                self.tableWidget_8.setItem(row, col, QTableWidgetItem(str(item)))
                col += 1
            
            row_position = self.tableWidget_8.rowCount()
            self.tableWidget_8.insertRow(row_position)
    
    def Export_Students_DataBase(self):
        
        # students = Students()
        # self.dbs.Export_Students(students)
        self.lms_2.database.Export_Students()
        
        self.statusBar().showMessage("Students In Database Exported Successfully")
    
    def Show_Employees_DataBase(self):
        self.tableWidget_9.setRowCount(0)
        self.tableWidget_9.insertRow(0)
        
        # employees = Employee()
        # data = self.dbs.Show_Employees(employees)
        data = self.lms_2.database.Show_Employees()
        
        for row, form in enumerate(data):
            for col, item in enumerate(form):
                self.tableWidget_9.setItem(row, col, QTableWidgetItem(str(item)))
                col += 1
            
            row_position = self.tableWidget_9.rowCount()
            self.tableWidget_9.insertRow(row_position)
    
    def Export_Employees_DataBase(self):
        
        # employees = Employee()
        # self.dbs.Export_Employees(employees)
        self.lms_2.database.Export_Employees()
        
        self.statusBar().showMessage("Employees In Database Exported Successfully")
    
    def Show_Authors_DataBase(self):
        self.tableWidget_10.setRowCount(0)
        self.tableWidget_10.insertRow(0)
        
        # data = self.dbs.Show_Authors()
        data = self.lms_2.database.Show_Authors()
        
        
        for row, form in enumerate(data):
            for col, item in enumerate(form):
                self.tableWidget_10.setItem(row, col, QTableWidgetItem(str(item)))
                col += 1
            
            row_position = self.tableWidget_10.rowCount()
            self.tableWidget_10.insertRow(row_position)
    
    def Export_Authors_DataBase(self):
        
        # self.dbs.Export_Authors()
        self.lms_2.database.Export_Authors()
        
        self.statusBar().showMessage("Authors In Database Exported Successfully")
    
    def Show_Publishers_DataBase(self):
        self.tableWidget_11.setRowCount(0)
        self.tableWidget_11.insertRow(0)
        
        # data = self.dbs.Show_Publishers()
        data = self.lms_2.database.Show_Publishers()
        
        for row, form in enumerate(data):
            for col, item in enumerate(form):
                self.tableWidget_11.setItem(row, col, QTableWidgetItem(str(item)))
                col += 1
            
            row_position = self.tableWidget_11.rowCount()
            self.tableWidget_11.insertRow(row_position)
    
    def Export_Publishers_DataBase(self):
        
        # self.dbs.Export_Publishers()
        self.lms_2.database.Export_Publishers()
        
        self.statusBar().showMessage("Publisher In Database Exported Successfully")

######################################################################

global action
action = ['- - - - - - -', 'Login', 'Logout', 'Add', 'Edit', 'Delete', 'Add Rent', 'Add Retreive', 'Add Sale']
global table
table = ['- - - - - - -', 'Books', 'Students', 'History', 'Category', 'Author', 'Publisher', 'Employee', 'Daily Movement']

######################################################################

def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()
