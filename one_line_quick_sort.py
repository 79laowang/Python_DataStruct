#!/usr/bin/env python
# -*- coding:utf-8 -*-
#-------------------------------------------------------------------------------
# File Name:   one_line_quick_sort.py
# Purpose:     一行代码进行快速排序 
#
# Author:      Ke Wang
#
# Created:     2019-11-08
# Copyright:   (c) Ke Wang 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    # 排序数据个数小于等于一，直接返回;否则，返回一个list包含比list[0]数据小的子list+list[0]+比list[0]大的子list.
    quick_sort = lambda array: array if len(array) <= 1 else quick_sort([item for item in array[1:] if item <= array[0]]) + [array[0]] + quick_sort([item for item in array[1:] if item > array[0]])
    list1 = [23,34,65,77,84,37,98,12,9,34]
    print(list1)
    list2 = quick_sort(list1)
    print(list2)

if __name__ == '__main__':
    main()
