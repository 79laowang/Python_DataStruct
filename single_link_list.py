#-------------------------------------------------------------------------------
# Name:        SingleLinkList
# Purpose:
#
# Author:      kkewang
#
# Created:     30/05/2019
# Copyright:   (c) kkewang 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from __future__ import print_function

class Node(object):
    def __init__(self ,item):
        self.item = item
        self.next = None

class SingleLinkList(object):
    """single link list"""

    def __init__(self, node=None):
        self.__head = node

    def is_empty(self):
        """check if Link list is empty"""
        return self.__head == None

    def length(self):
        """Count the Linklist length"""
        cur = self.__head
        count = 0
        while cur != None:
            count +=1
            cur = cur.next
        return count

    def travel(self):
        """travel the linklist"""
        cur = self.__head
        while cur != None:
            print(cur.item,end=" ")
            cur = cur.next
        print("\n")


    def add(self, item):
        """Add node in head"""
        node = Node(item)
        node.next = self.__head
        self.__head = node

    def append(self, item):
        """Append node in tail"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next != None:
                cur = cur.next
            cur.next = node

    def insert(self, pos, item):
        """Insert node to specified position
        parameter pos from 0 start
        """
        if pos < 0:
            self.add(item)
        elif pos > (self.length() - 1):
            self.append(item)
        else:
            pre = self.__head
            index = 0
            while index < (pos - 1):
                index += 1
                pre = pre.next
            node = Node(item)
            node.next = pre.next
            pre.next = node

    def remove(self, item):
        """remove node from list"""
        cur = self.__head
        pre = None
        while cur != None:
            if cur.item == item:
                # handle removing head node
                if cur == self.__head:
                    self.__head = cur.next
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next

    def search(self, item):
        """search the specified item"""
        cur = self.__head
        while cur != None:
            if cur.item == item:
                return True
            else:
                cur = cur.next
        return False

def main():
    single_ll = SingleLinkList()
    print(single_ll.is_empty())
    print(single_ll.length())
    for x in range(10):
        single_ll.append(x)
    print(single_ll.length())
    single_ll.travel()
    single_ll.add(11)
    single_ll.travel()
    single_ll.insert(2,22)
    single_ll.travel()
    if single_ll.search(22):
        print("find")
    if not single_ll.search(23):
        print("Not find")
    single_ll.remove(11)
    single_ll.travel()
    single_ll.remove(9)
    single_ll.travel()
    single_ll.remove(22)
    single_ll.travel()

if __name__ == '__main__':
    main()
