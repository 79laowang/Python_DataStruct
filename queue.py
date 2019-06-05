# coding:utf-8
#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      kkewang
#
# Created:     13/05/2019
# Copyright:   (c) kkewang 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class MyQueue(object):
    """ Queue implement """
    def __init__(self):
        self.__list = []

    def enqueue(self, item):
        """add one in rear of the queue """
        self.__list.append(item)

    def dequeue(self):
        """delete one from head of queue"""
        return self.__list.pop(0)

    def is_empty(self):
        """Check if the queue is empty"""
        return self.__list == []

    def size(self):
        """return the queue number size"""
        return len(self.__list)

def main():
    q = MyQueue()
    for x in range(10):
        q.enqueue(x)

    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())

    if q.is_empty():
        print("empty queue!")
    else:
        print("Queue length:" + str(q.size()))

if __name__ == '__main__':
    main()

