#-------------------------------------------------------------------------------
# Name:        Selection Sorting
# Purpose:
#
# Author:      kkewang
#
# Created:     01/06/2019
# Copyright:   (c) kkewang 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

##demonstration:
##alist -> [23,34,65,77,84,37,98,12,9,34]
##1st round of inter loop [23,34,65,77,84,37,98,12,9,34]
##   min - > 9
##          [9,  34,65,77,84,37,98,12,23,34]
##2rd round of inter loop [9,   |34,65,77,84,37,98,12,23,34]
##   min - > 12
##          [9,12,  65,77,84,37,98,34,23,34]
##3rd round of inter loop [9,12   |65,77,84,37,98,34,23,34]
##   min - > 23
##          [9,12,23,  77,84,37,98,34,65,34]
##...
#
# Worst time complexity: O(n^2)
# Optimal time complexity: O(n^2)
#
from __future__ import print_function
def select_sort(alist):
    """Select Sort unstable"""
    n = len(alist)
    for j in range(n-1):
        min_index = j
        for i in range(j+1, n):
            # Find the minmum
            if alist[min_index] > alist[i]:
                min_index = i
        # Exchange the minmum from tail list to the front list
        alist[j],alist[min_index] = alist[min_index],alist[j]

def main():
    list1 = [23,34,65,77,84,37,98,12,9,34]
    print(list1)
    select_sort(list1)
    print(list1)

if __name__ == '__main__':
    main()
