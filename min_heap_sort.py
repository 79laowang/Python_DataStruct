#!/usr/bin/env python
# -*- coding:utf-8 -*-
#-------------------------------------------------------------------------------
# File Name:   min_heap_sort.pya
# Purpose:     小根堆排序 
#
# Author:      Ke Wang
#
# Created:     2019-11-05
# Copyright:   (c) Ke Wang 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#demonstration
# A small root heap 
#                  2
#               /      \
#              5         8       
#           /     \   /     \
#         16      30  15    20
#         /
#        40
#1. First, construct a small root heap of the array to be sorted
#2. Then, take out the top node (minimum value) of the small root heap and exchange
# it with the lowest layer and right-most element of the heap.
#3. Then, construct a small root heap of the remaining elements and repeat the
# second step until the length of the small root heap is 1, and the sorting is completed
#

from __future__ import print_function
import numpy as np

def MakeHeap(a):
    """Build a heap"""
    # All index > list.size/2 are leaf node
    n = len(a)
    for i in range(n // 2 - 1, -1, -1):#对非叶子节点的子节点进行调节，构建堆
        # i in seq [n/2 - 1, n/2 -2, ..., 0 ], a[0]保存最小元素
        AdjustHeap(a, i, n)

def AdjustHeap(a, low, high):
    """
    Adjust heap
    a: need to adjust list
    low: need to adjust heap node 
    high: node to adjust range
    """
    small = low * 2 +1        # small指向调整堆节点的左右子节点中关键字较小者
    x = a[low]                       #取得堆节点的数值
    while small < high:                    #循环对子节点及其子树进行调整
        if small + 1 < high and a[small+1] < a[small]:    #找到节点low子节点的最小值
            small += 1
        if x <= a[small]:      #若两个子节点均大于该堆节点，则不用调整
            break
        a[low], a[small] = a[small], a[low]             #将节点low的数值与其子节点中最小者的数值进行对调
        low = small                        #将low赋为改变的子节点的索引
        small = low * 2 + 1                   #将small赋为节点对应的左子节点

def HeapSort(a):
    MakeHeap(a)                 #构建小顶堆
    n = len(a)
    for i in range(n - 1, 0, -1):   # 对当前无序区a[0..n-1]的元素进行堆排序
        # 无序区 i in seq[n-1, n-2, n-3, .., 1]
        a[i], a[0] = a[0], a[i]           #将堆顶元素a[0]与堆中最后一个元素a[i]进行对调，因为小顶堆中堆顶元素永远最小，因此，输出即为最小元素
        # 有序区 [<-- .., a[n-2], a[n-1]], 调整完 a[0] 从大-->到小 a[n-1]
        AdjustHeap(a, 0, i)          #重新调整使剩下的元素仍为一个堆

def main():
      a = np.random.randint(0, 20, size = 10)
      print("Before sorting...")
      print("-"*50)
      print(a)
      print("-"*50)
      HeapSort(a)
      print("After sorting...")
      print("-"*50)
      print(a[::-1])                   #因为堆排序按大到小进行排列，采用a[::-1]对其按从小到大进行输出
      print("-"*50)

if __name__ == '__main__':
    main()
