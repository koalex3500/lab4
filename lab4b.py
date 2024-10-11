#!/usr/bin/env python3

#This is the function join_lists this will return list of unique elements from the lists
def join_lists(list1, list2):
 return list(set(list1) | set(list2))
#This is the function match_lists this will return list of common elements from the lists
def match_lists(list1, list2):
 return list(set(list1) & set(list2))
#This is the function diff_lists this will return list of different elements that are not both present in both lists
def diff_lists(list1, list2):
 return list(set(list1) ^ set(list2))

#This is for to test locally on my machine to see if script for lab4b is correct.
#if __name__ == "__main__":
# list1 = [1, 2, 3, 4, 5]
# list2 = [2, 1, 0, -1, -2]

 #print("Join lists: ", join_lists(list1, list2))
 #print("Match lists: ", match_lists(list1, list2))
 #print("Diff lists: ", diff_lists(list1, list2))
