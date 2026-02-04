#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'IsOneEdit' function below.
#
# The function is expected to return a BOOLEAN.
# The function accepts following parameters:
#  1. STRING str1
#  2. STRING str2
#

def IsOneEdit(str1, str2):
    # Write your code here
    # strip each string into separate lists
    list1 = list(str1.strip())
    list2 = list(str2.strip())

    # If length difference > 1, must not have any edits.
    if abs(len(list1) - len(list2)) > 1:
        return False

    # Allow 1 character replacement if they're the same length
    if len(list1) == len(list2):
        char = 0
        for a, b in zip(list1, list2):
            if a != b:
                char += 1
                if char > 1:
                    return False
        return True

    # For length difference of 1: check for one insertion/deletion
    # Ensure list1 is the shorter
    if len(list1) > len(list2):
        list1, list2 = list2, list1

    #This is more or less where we stopped. 
    # Here I'm looking for one insertion in list1 to make list2
    i = j = 0
    found_diff = False
    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
    # stepping through the list to see if words match
            i += 1
            j += 1
        else:
            if found_diff:
                return False
            found_diff = True
            j += 1
    return True


if __name__ == '__main__':
# I wrote out some extra test cases, as well as the ones provided during the test. 
# I'm embarrassed to say I forgot they don't have to be actual words for a minute there...
    tests = [
        ('Cute','Cut'),      # True
        ('Cat','Cut'),       # True
        ('Cat','At'),        # True
        ('Cat','Cute'),      # False
        ('Cut','Tuck'),      # False
        ('a',''),            # True
        ('','a'),            # True
        ('',''),             # True
        ('abc','ab'),        # True
        ('abc','a'),         # False
        ('abc','abcd'),      # True
        ('abc','abxcd'),     # False
        ('pale','ple'),      # True
        ('pales','pale'),    # True
        ('pale','bale'),     # True
        ('pale','bake'),     # False
    ]
    for a, b in tests:
        result = IsOneEdit(a.lower(), b.lower())
        print(f"Testing '{a}' and '{b}': {result}")


