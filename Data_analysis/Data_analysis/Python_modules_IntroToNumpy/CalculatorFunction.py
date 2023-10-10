# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 11:00:18 2023

@author: KING
"""

def calculator(x,y):
    option = input('Enter "a" for addtion:  \n Enter "s" for substraction:  \n Enter "m" for multiplocation: \n Enter "d" for division: ')
    if option == 'a':
        add = x + y 
        return add 
    elif option == 's':
        sub = x - y 
        return sub
    elif option == 'm':
        mul = x*y 
        return mul
    elif option == 'd':
        div = x/y
        return div
    else:
        print('Please enter the right value: ')
    

