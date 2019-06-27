#-------------------------------------------------------------------------------
# Name:        bubble_sort
# Purpose:
#
# Author:      Ke Wang
#
# Created:     01/06/2019
# Copyright:   (c) Ke Wang 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#
# Worst time complexity: O(n^2)
# Optimal time complexity: O(n)
#

def bubble_sort(alist):
    """Bubble Sort unstable"""
    n = len(alist)
    for j in range(n-1):
        # Count exchange times
        count = 0
        for i in range(0, n-1-j):
            if alist[i] > alist[i+1]:
                alist[i],alist[i+1] = alist[i+1],alist[i]
                count += 1
        #No exchange, quit loop
        if count == 0:
            return

def main():
    list1 = [23,34,65,77,84,37,98,12,9,34]
    print list1
    bubble_sort(list1)
    print list1

if __name__ == '__main__':
    main()

