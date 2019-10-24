#-------------------------------------------------------------------------------
# Name:        Quick Sorting
# Purpose:
#
# Author:      kkewang
#
# Created:     01/06/2019
# Copyright:   (c) kkewang 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

##demonstration:
##          --->                      <---
##alist -> [23,34,65,77,84,37,98,12,9,34]
##           |                         |
##          low                       high
##sort_value = 23
##alist -> [ 9 ,34,65,77,84,37,98,12, ,34]
##           |                       |
##          low                  <--high
##sort_value = 23
##alist -> [ 9 ,34,65,77,84,37,98,12, ,34]
##              |                    |
##             low-->               high
##
##          if alist[high] < sort_value:
##              alist[low] = alist[high]
##              low += 1
##          elif alist[high] > sort_value:
##              high -= 1
##sort_value = 23
##alist -> [ 9 , ,65,77,84,37,98,12,34,34]
##              |                 |
##             low            <--high
##          if alist[low]  < sort_value:
##              low += 1
##          elif
##              alist[low] > sort_value:
##              alist[high] = alist[low]
##              high -= 1
##sort_value = 23
##alist -> [ 9,12, ,77,84,37,98,65,34,34]
##                |              |
##               low-->         high
##sort_value = 23
##alist -> [ 9,12,  ,77,84,37,98,65,34,34]
##                ||
##               low<--high
##low = high = sort_value
#
# Worst time complexity: O(n^2)
# Optimal time complexity: O(nlogn)
#

def quick_sort(alist, first, last):
    """Quick Sort unstable"""
    # quit recursion
    if first >= last:
        return
    n = len(alist)
    sort_value = alist[first]
    low = first
    high = last
    while low < high:
        # move from right
        while high > low and alist[high] >= sort_value:
            high -= 1
        alist[low] = alist[high]

        # move from left
        while low < high and alist[low] < sort_value:
            low += 1
        alist[high] = alist[low]
    alist[low] = sort_value

    # quick sort left list
    quick_sort(alist, first, low-1)
    # quick sort right list
    quick_sort(alist,low + 1, last)

def main():
    list1 = [23,34,65,77,84,37,98,12,9,34]
    print list1
    quick_sort(list1, 0, len(list1)-1)
    print list1

if __name__ == '__main__':
    main()
