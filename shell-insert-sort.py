#-------------------------------------------------------------------------------
# Name:        Shell Sorting
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
##first round: gap = 5
##          23             37
##             34             98
##                65             12
##                   77             9
##                      84            34
#
# Worst time complexity: O(n^2)
# Optimal time complexity: O(n^1.3)
#

def shell_insert_sort(alist):
    """Shell Sort unstable"""
    n = len(alist)
    gap = n/2
    # gap change times
    while gap > 0:
        # The only difference from insert sort is gap value
        for j in range(gap,n):
            # j = [gap, gap+1, gap+2, gap+3 ... n-1]
            i = j
            while i > 0:
                if alist[i] < alist[i-gap]:
                    # Exchange the minmum to the front
                    alist[i],alist[i-gap] = alist[i-gap],alist[i]
                    i -= gap
                else:
                    break
        gap /= 2

def main():
    list1 = [23,34,65,77,84,37,98,12,9,34]
    print list1
    shell_insert_sort(list1)
    print list1

if __name__ == '__main__':
    main()
