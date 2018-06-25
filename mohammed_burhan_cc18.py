# -*- coding: utf-8 -*-
"""
Created on Thu May 17 11:06:22 2018

@author: Lenovo
"""


from string import ascii_lowercase as asc_lower 
def check(s):
    return set(asc_lower) - set(s.lower()) == set([])
strng=input("Enter string: ")




if(check(strng)==True):
      print("PANGRAM")
else:
      print("NOT PANGRAM")
      

    