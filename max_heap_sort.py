#!/usr/bin/env python
# -*- coding:utf-8 -*-
#-------------------------------------------------------------------------------
# File Name:   max_heap_sort.py
# Purpose:    
#
# Author:      Ke Wang
#
# Created:     2019-11-05
# Copyright:   (c) Ke Wang 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from __future__ import print_function                                                                                                                  
import numpy as np

def heapify(arr, n, i): 
    largest = i
    l = 2 * i + 1 # left = 2*i + 1 
    r = 2 * i + 2 # right = 2*i + 2 
    if l < n and arr[largest] < arr[l]: 
        largest = l 
    if r < n and arr[largest] < arr[r]: 
        largest = r 
    if largest != i: 
        arr[i],arr[largest] = arr[largest],arr[i] # 交换 
        heapify(arr, n, largest) 

def build_heap(arr):
    n = len(arr) # Build a maxheap. 
    for i in range(n, -1, -1): 
        heapify(arr, n, i) 

def heapSort(arr): 
    build_heap(arr)
    # 一个个交换元素 
    n = len(arr)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i] # 交换 
        heapify(arr, i, 0) 

def main():
    arr = np.random.randint(0, 20, size = 10)
    print("排序前:") 
    print(arr)
    heapSort(arr) 
    print("排序后:") 
    print(arr)

if __name__ == '__main__':
    main()
