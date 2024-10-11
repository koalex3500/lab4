#!/usr/bin/env python3

#This is for the function create_dictionary, this will help take two lists and return the dictionary with keys paired with corresponding value.
def create_dictionary(keys, values):
 return dict(zip(keys, values))
#This is the function split_dictionary, this will return two lists one of the list being keys and other containing values.
def split_dictionary(dictionary):
 keys = list(dictionary.keys())
 values = list(dictionary.values())
 return keys, values
#This is the function shared_values, this will take the two dictionaries and return set of the values common in both the dictionaries.
def shared_values(dict1, dict2):
 return set(dict1.values()) & set(dict2.values())

#This will be my test for local virtual machine to see how output looks like when i run python3 lab4c.
#if __name__ == "__main__":
 #keys = ['Address', 'City', 'Country', 'Postal Code', 'Province']
 #values = ['70 The Pond Rd', 'Toronto', 'Canada', 'M3J3M6', 'ON']

 #my_dict = create_dictionary(keys, values)
 #print("Created dictionary:", my_dict)
 
 #keys_out, values_out = split_dictionary(my_dict)
 #print("Keys:", keys_out)
 #print("Values", values_out)
 
 #dict1 = {'Address': '70 The Pond Rd', 'City': 'Toronto', 'Country': 'Canada', 'Postal Code': 'M3J3M6', 'Province': 'ON'}
 #dict2 = {'Address': '1750 Finch Ave E', 'City': 'Toronto', 'Country': 'Canada', 'Postal Code': 'M2J2X5', 'Province': 'ON'}

 #print("Shared values:", shared_values(dict1, dict2))
