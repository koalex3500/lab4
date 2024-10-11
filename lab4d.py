#!/usr/bin/env python3

#this is the first_five function which will give the first 5 characters
def first_five(input_string):
 return input_string[:5]

#this is the last_seven function which will give the last 7 characters
def last_seven(input_string):
 return input_string[-7:]

#this is the middle_number function which will give us the mdiddle number of a numeric input
def middle_number(num):
 str_num = str(num)
 mid_index = len(str_num) // 2
#this part was added because it was not  handling floating point numbers correctly, it wasnt printing out .5 instead 1.5 or .
 if '.' in str_num:
  decimal_index = str_num.index('.')
  if decimal_index == mid_index:
   return '.' + str_num[mid_index+1]
  else:
   return str_num[mid_index] 
 else:
  if len(str_num) % 2 == 0:
   return str_num[mid_index - 1: mid_index +1]
  else:
   return str_num[mid_index]

#this is the function first_three_last_three , this will take the first three characters and and the last 3 of the second string.
def first_three_last_three(str1, str2):
 return str1[:3] + str2[-3:]




#This is to test on virtual machine for the functions to see if lab4d works correctly when its required to print according to the functions
#if __name__ == "__main__":
 #print(first_five("Hello World!!"))

 #print(last_seven("Hello World!!"))

 #print(middle_number(1500))
 #print(middle_number(1.50))

 #print(first_three_last_three("Hello", "World!!"))
 #print(first_three_last_three("Seneca", "College"))
