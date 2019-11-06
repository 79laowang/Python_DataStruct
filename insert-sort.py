#!/usr/bin/env python
# -*- coding:utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        Insert Sorting
# Purpose:
#
# Author:      kkewang
#
# Created:     01/06/2019
# Copyright:   (c) kkewang 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#demonstration:
#alist -> [23,34,65,77,84,37,98,12,9,34]
#rounds    [23,   34,65,77,84,37,98,12,9,34]
#          [23,34,   65,77,84,37,98,12,9,34]
#          [23,34,65,   77,84,37,98,12,9,34]
#          [23,34,65,77   ,84,37,98,12,9,34]
#          [23,34,65,77,84,   37,98,12,9,34]
#          [23,34,37,65,77,84,   98,12,9,34]
#          [23,34,37,65,77,84,98   ,12,9,34]
#          [12,23,34,37,65,77,84,98,   9,34]
#          [9,12,23,34,37,65,77,84,98,   34]
#          [9,12,23,34,34,37,65,77,84,98]
#
# Worst time complexity: O(n^2)
# Optimal time complexity: O(n)
#

from __future__ import print_function

def insert_sort(alist):
    """Insert Sort stable"""
    n = len(alist)
    # Variable j indicates selecting item times from right unsort list
    for j in range(1, n):
        i = j
        # Variable i indicates the left list sorting times
        while i > 0 and alist[i] < alist[i-1]:
            # Exchange the minmum from tail list to the front list
            alist[i],alist[i-1] = alist[i-1],alist[i]
            i -= 1
            # Selected item from right unsort list inserted the right postion
            # in left sorting list, quit while loop

def main():
    list1 = [23,34,65,77,84,37,98,12,9,34]
    print(list1)
    insert_sort(list1)
    print(list1)

if __name__ == '__main__':
    main()
