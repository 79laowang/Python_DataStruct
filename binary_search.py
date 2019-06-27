#-------------------------------------------------------------------------------
# Name:        binary_search.py
# Purpose:    Binary Search
#
# Author:      Ke Wang
#
# Created:     03/06/2019
# Copyright:   (c) Ke Wang 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#
# Worst time complexity: O(logn)
# Optimal time complexity: O(1)
#

def binary_search(alist, item):
    """Binary search"""
    n = len(alist)
    if n > 0:
        mid = n/2
        if alist[mid] == item:
            return True
        elif item < alist[mid]:
            return binary_search(alist[:mid],item)
        else:
            return binary_search(alist[mid+1:],item)
    return False

def non_recursive_binary_search(alist, item):
    """Non-recursive binary search"""
    n = len(alist)
    first = 0
    last = n - 1
    while first <= last:
        mid = (first + last) / 2
        if alist[mid] == item:
            return True
        elif item < alist[mid]:
            last = mid - 1
        else:
            first = mid +1
    return False



def main():
    # The searching list should be sorted.
    list1 = [1, 9, 23, 45, 46, 48, 65, 77, 88, 99]
    print list1
    print(binary_search(list1, 45))
    print(binary_search(list1, 99))
    print(binary_search(list1, 100))
    print("non-recursive binary search:")
    print(non_recursive_binary_search(list1, 45))
    print(non_recursive_binary_search(list1, 99))
    print(non_recursive_binary_search(list1, 100))

if __name__ == '__main__':
    main()

