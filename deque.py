#-------------------------------------------------------------------------------
# Name:        deque
# Purpose:
#
# Author:      kkewang
#
# Created:     21/05/2019
# Copyright:   (c) kkewang 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class Deque(object):
    """ Double-end queue implement """
    def __init__(self):
        self.__list = []

    def add_front(self, item):
        """add one in rear of the queue """
        self.__list.insert(0,item)

    def add_rear(self, item):
        """add one in rear of the queue """
        self.__list.append(item)

    def pop_front(self):
        """pop one from queue head"""
        return self.__list.pop(0)

    def pop_rear(self):
        """pop one from queue tail"""
        return self.__list.pop()

    def is_empty(self):
        """Check if the queue is empty"""
        return self.__list == []

    def size(self):
        """return the queue number size"""
        return len(self.__list)

def main():
    q = Deque()
    for x in range(10):
        q.add_front(x)

    for x in range(10):
        q.add_rear(x)

    print(q.pop_front())
    print(q.pop_rear())
    print(q.pop_front())
    print(q.pop_rear())

    if q.is_empty():
        print("empty queue!")
    else:
        print("Queue length:" + str(q.size()))

if __name__ == '__main__':
    main()

