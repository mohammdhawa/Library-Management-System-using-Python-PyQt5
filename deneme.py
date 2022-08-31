import smtplib
from random import randint

server = smtplib.SMTP('smtp.gmail.com', 587)

server.starttls()
server.login('librarymanagementsystem543@gmail.com', 'library#12345')
server.sendmail('librarymanagementsystem543@gmail.com', "ismekbektop@gmail.com", "Hello fucking world")