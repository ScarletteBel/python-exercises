# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 16:53:02 2021

@author: scarb
"""

# Few ways to getting factorial 

print (4*3*2*1)


from math import factorial 
factorial (4)



def factorial1 (n):
    producto = 1 
    i = 1
    while i <= n:
        producto *= i
        i += 1 
        
    return producto


def factorial2(n):
    producto = 1
    for i in range (1,n+1):
        producto = producto * i
        
    return producto


def factorial3(n):
    producto = 1
    for i in range (1,n+1):
        producto = producto * n
        n = n-1
        
    return producto


        
print(factorial(4))
print(factorial1(4))  
print(factorial2(4))    
print(factorial3(4))  
    
