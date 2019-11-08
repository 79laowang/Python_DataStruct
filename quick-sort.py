#!/usr/bin/env python
# -*- coding:utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        Quick Sorting
# Purpose:     快速排序 
#  稳定性：快排是一种不稳定排序，比如基准值的前后都存在与基准值相同的元素，那么相同值就会被放在一边，这样就打乱了之前的相对顺序
#  比较性：因为排序时元素之间需要比较，所以是比较排序
#  时间复杂度：快排的时间复杂度为O(nlogn)
#  空间复杂度：排序时需要另外申请空间，并且随着数列规模增大而增大，其复杂度为：O(nlogn)
#  缺点: 对于小规模的数据集性能不是很好。
#  Solution: 当分区的规模达到一定小时，便停止快速排序算法，而是改用插入排序，因为插入排序在对基本有序的数据集排序有着接近线性的复杂度
# Author:      kkewang
#
# Created:     01/06/2019
# Copyright:   (c) kkewang 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#demonstration:
#          --->                      <---
# Find the first element postion in list
#alist -> [23,34,65,77,84,37,98,12,9,34]
#           |                         |
#          low                       high
#sort_value = 23
#alist -> [ 9 ,34,65,77,84,37,98,12, ,34]
#           |                       |
#          low                  <--high
#sort_value = 23
#alist -> [ 9 ,34,65,77,84,37,98,12, ,34]
#              |                    |
#             low-->               high
#
#          if alist[high] < sort_value:
#              alist[low] = alist[high]
#              low += 1
#          elif alist[high] > sort_value:
#              high -= 1
#sort_value = 23
#alist -> [ 9 , ,65,77,84,37,98,12,34,34]
#              |                 |
#             low            <--high
#          if alist[low]  < sort_value:
#              low += 1
#          elif
#              alist[low] > sort_value:
#              alist[high] = alist[low]
#              high -= 1
#sort_value = 23
#alist -> [ 9,12, ,77,84,37,98,65,34,34]
#                |              |
#               low-->         high
#sort_value = 23
#alist -> [ 9,12,  ,77,84,37,98,65,34,34]
#                ||
#               low<--high
#Find the sort_value correct position:low = high
#
# Worst time complexity: O(n^2)
# Optimal time complexity: O(nlogn)
#

from __future__ import print_function

def quick_sort(alist, first, last):
    """Quick Sort unstable"""
    # quit recursion
    if first >= last:
        return

    sort_value = alist[first]
    low = first
    high = last
    while low < high:
        # move high index from right
        while high > low and alist[high] >= sort_value:
            high -= 1
        alist[low] = alist[high]

        # move low index from left
        while low < high and alist[low] < sort_value:
            low += 1
        alist[high] = alist[low]
    alist[low] = sort_value

    # quick sort left list
    quick_sort(alist, first, low-1)
    # quick sort right list
    quick_sort(alist,low + 1, last)

def quick_sort_pythonic(arr):
    """快速排序 pythonic"""
    n = len(arr)
    if n < 2:
        return arr

    mid = arr[n // 2]
    left, right = [], []
    arr.remove(mid)
    for item in arr:
        if item >= mid:
            right.append(item)
        else:
            left.append(item)
    return quick_sort_pythonic(left) + [mid] + quick_sort_pythonic(right)


def main():
    list1 = [23,34,65,77,84,37,98,12,9,34]
    print(list1)
    quick_sort(list1, 0, len(list1)-1)
    print(list1)
    print("Pythonic quick sorting ...")
    list1 = [23,34,65,77,84,37,98,12,9,34]
    print(quick_sort_pythonic(list1))

if __name__ == '__main__':
    main()
