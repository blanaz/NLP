# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 21:08:07 2020

@author: blanka zana
"""

#Task 1: Adding machine

#Write a function that adds two numbers x,y and returns the output x + y. 
#Sample input might be x=-1, y=8 in which case the expected output is 7. 
#The expected output is either float or int.

def addictive_function(x,y):
    return x+y
    
#example
num1 = -1
num2 = 8

print ("The result is" , addictive_function(num1,num2))

#Task 2: Character count

#Write a function that takes two arguments
#- s an arbitrary string.
#- l a letter (i.e. any valid single character).

#The function should search the string for occurences of the letter and 
#return an integer indicating how many times the letter l occurs in the string s.

#Note: Your function should be case-insensitive, i.e. it shouldn't care if the letter is "H" or "h"
result = []

def char_cunt(s,l):
   return (s.lower().count(l.lower()))
  

f = "hellllLLllo you beautiful bastard"
k = "l"
    
char_cunt(f,k)


#Task 3: Function isEven

#Write a function which evaluates if a given integer number (given as a parameter for the function) is an even number. 
# The function should return a 
# Boolean value True if the number is even and False if the number is odd.

#Given a list (or array) of n integer numbers, write a program which uses the function isEven to determines the number of even 
# items in the list.

def isEven (a):
   return (a % 2 == 0)

x = isEven(7)
x

def isEvenList(a):
    count = 0
    for i in a:
        if isEven(i):
            count += 1
    return count

listy=[2,3,4,5,6,7,8]
isEvenList(listy)

#other way to do it (thanks to Mikkel)
def isEvenList(a):
    return len([i for i in a if isEven(i)])
listy=[2,3,4,5,6,7,8]

isEvenList(listy)
        
x = 4

[x for i in listy if isEven(i)]

#Task 4: Search in List
#ASK SOMEONE ABOUT THE FLOATS
#Given a list (or array) of n floating-point numbers, write a program 
# which searches and outputs the largest number in the list.



def maxi (a):
    result = max(a)
    return (result)                 #it could be just one line: return max(a)

dalist = [1.0,2.0,3.0,4.0,5.0]
type(maxi(dalist))



#Task 5: String and Loops

#Write a function which takes a string (word) as an argument. The function should print the complete word on the 
# first line and remove the last character on each successive line, ending with a single (the first) character.
#Example: Input word is Test
#Function output:
#Test
#Tes
#Te

def biter (x):
    while len (x) > 0:
        print (x)
        x = x[0:-1]                     #0 is optional
        
a = "hablabalbala"

biter (a)


#other way
def chopper (word):
    if word:
        print (word)
        word = word[0:-1]
        chopper(word)
        #else stuff

#Task 6: Get dict keys

#Write a function that takes as it's single input any dictionary
#The function should return the keys of the input dictionary, in a list.


def dic_return_keylist(x):
    return list(x.keys())

myDic = {"dog":"wau", "cat":"meow", "bee":"bzzz"}

dic_return_keylist(myDic)
