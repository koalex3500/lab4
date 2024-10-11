#!/usr/bin/env python3

#this is the function for join_sets
def join_sets(set1, set2):
 return set1 | set2
#this is the function for match_sets
def match_sets(set1, set2):
 return set1 & set2
#this is the function for diff_sets
def diff_sets(set1, set2):
 return set1 ^ set2

#This is just to test if my three funcitons work correctly.
#if __name__ == "__main__":
 #set1 = {1, 2, 3, 4, 5}
 #set2 = {2, 1, 0, -1, -2,}

 #print("Join sets: ", join_sets(set1, set2))
 #print("Match sets: ", match_sets(set1, set2))
 #print("Diff sets: ", diff_sets(set1, set2))

