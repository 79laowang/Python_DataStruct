# coding:utf-8
#-------------------------------------------------------------------------------
# Name:        Merge Sorting
# Purpose:
#
# Author:      Ke Wang
#
# Created:     01/06/2019
# Copyright:   (c) Ke Wang 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

##demonstration:
## 将两个或两个以上的有序表组合成一个新的有序表的方法叫归并。
##假设初始序列含有n个记录，则可看成是n个有序的子序列，每个子序列的长度为1，
##然后两两归并，得到n/2个长度为2或1的有序子序列；再两两归并，如此重复。
##alist ->     [49,38  ,65,97,  76,13,  27]
##first merge     38,49   65,97      13,76   27
##second merge    38, 49 ,65, 97     13, 27, 76
##third merge     13, 27 ,38, 49     65, 76, 97
#
# Worst time complexity: O(nlogn)
# Optimal time complexity: O(nlogn)
#

from __future__ import print_function

def merge_sort(alist):
    """merge sort stable"""
    n = len(alist)
    if n <= 1:
        return alist
    mid = int(n/2)

    # return new sorted left list
    left_list = merge_sort(alist[:mid])
    # return new sorted right list
    right_list = merge_sort(alist[mid:])

    # Merge above sorted left and right lists into one new list named result
    left_p, right_p = 0, 0
    result = []

    while left_p < len(left_list) and right_p < len(right_list):
        if left_list[left_p] <= right_list[right_p]:
            result.append(left_list[left_p])
            left_p += 1
        else:
            result.append(right_list[right_p])
            right_p += 1
    # Add the remain one of left or right list if exists to result list
    result += left_list[left_p:]
    result += right_list[right_p:]
    return result

def main():
    list1 = [23,34,65,77,84,37,98,12,9,34]
    print(list1)
    sorted_list = merge_sort(list1)
    print(sorted_list)

if __name__ == '__main__':
    main()
