# -*- coding:utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        Circle Queue
# Purpose:
#
# Author:      kkewang
#
# Created:     06/06/2019
# Copyright:   (c) kkewang 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class CircleQueue(object):
    """Circle Queue implement """
    def __init__(self, capacity):
        self.queue = [None] * capacity
        self.capacity = capacity
        self.front = 0
        self.rear = 0

    def enQueue(self, element):
        if self.full():
            print('Queue is full!')
            return
        self.queue[self.rear] = element
        self.rear  = (self.rear + 1) % self.capacity

    def deQueue(self):
        if self.empty():
            print('Queue is empty')
            return
        temp = self.queue[self.front]
        self.queue[self.front] = None
        self.front = (self.front + 1) % self.capacity
        return temp

    def full(self):
        return (self.rear + 1) % self.capacity == self.front

    def empty(self):
        return self.front == self.rear

    def printQueue(self):
        temp = self.front
        while temp != self.rear:
            print(self.queue[temp],end=" ")
            temp = (temp + 1) % self.capacity
        print

    def clear(self):
        temp = self.front
        while temp != self.rear:
            self.queue[temp] = None
            temp = (temp + 1) % self.capacity
        self.rear = self.front

    def getHead(self):
        if self.empty():
            print('Queue is empty!')
            return
        return self.queue[self.front]

    def length(self):
        return (self.rear - self.front + self.capacity) % self.capacity

def main():
    cir_queue = CircleQueue(10)

    # 0~9 enter in queue
    print("Enter Circle Queue:")
    for i in range(10):
        cir_queue.enQueue(i)
    cir_queue.printQueue()

    # delete 5 items from header：0~4
    print("Delete 5 items of Queue head:")
    for i in range(5):
        cir_queue.deQueue()
    cir_queue.printQueue()
    # add 8 items to Queue tail：0~7
    print("Add 8 items to Queue tail:")
    for i in range(8):
        if not cir_queue.full():
            cir_queue.enQueue(i)
    cir_queue.printQueue()

if __name__ == '__main__':
    main()
