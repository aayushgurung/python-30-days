import random
import pyperclip
from tkinter import *
from tkinter.ttk import *

def random_password():
    enter=int(input('Enter the strength of password from 1 to 3 : '))
    length=int(input('Enter the length of the password to generate  : '))
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    digits = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 !@#$%^&*()"
    password = ""
    if enter==1:
        for i in range(0,length):
            password= password + random.choice(lower)
        return password
    if enter==2:
        for i in range(0,length):
            password= password + random.choice(upper)
        return password
    if enter==3:
        for i in range(0,length):
            password= password + random.choice(digits)
        return password
    else:
        print('Please choose an option')
    
    
rand=random_password()
print(rand)

# def printf(x,y):
#     lower = "abcdefghijklmnopqrstuvwxyz"
#     upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
#     digits = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 !@#$%^&*()"
#     password = ""
#     if x==1:
#         for i in range(0,y):
#             password+=random.choice(lower)
#             print(password)
#         return password

# printf(1,5)
