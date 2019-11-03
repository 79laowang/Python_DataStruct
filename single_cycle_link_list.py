#-------------------------------------------------------------------------------
# Name:        Single Cycle Link List
# Purpose:
#
# Author:      kkewang
#
# Created:     30/05/2019
# Copyright:   (c) kkewang 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class Node(object):
    def __init__(self ,item):
        self.item = item
        self.next = None

class SingleCycleLinkList(object):
    """single cycle link list"""

    def __init__(self, node=None):
        self.__head = node
        if node:
            node.next = node

    def is_empty(self):
        """check if Link list is empty"""
        return self.__head == None

    def length(self):
        """Count the Linklist length"""
        if self.is_empty():
            return  0
        cur = self.__head
        count = 1
        while cur.next != self.__head:
            count +=1
            cur = cur.next
        return count

    def travel(self):
        """travel the single cycle link list"""
        if self.is_empty():
            return
        cur = self.__head
        while cur.next != self.__head:
            print(cur.item,end=" ")
            cur = cur.next
        print(cur.item,end=" ")
        print

    def add(self, item):
        """Add node in head"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            # Quit look, cur point to tail node
            node.next = self.__head
            self.__head = node
            cur.next = self.__head

    def append(self, item):
        """Append node in tail"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            node.next = cur.next
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
        if self.is_empty():
            return
        cur = self.__head
        pre = None
        while cur.next != self.__head:
            if cur.item == item:
                # handle removing head node
                if cur == self.__head:
                    # head node
                    rear = self.__head
                    while rear.next != self.__head:
                        rear = rear.next
                    self.__head = cur.next
                    rear.next = self.__head
                else:
                    # middle node
                    pre.next = cur.next
                return
            else:
                pre = cur
                cur = cur.next
        # Quit the loop, handle the tail node
        if cur.item == item:
            if cur == self.__head:
                slef.__head = None
            else:
                pre.next = cur.next

    def search(self, item):
        """search the specified item"""
        if self.is_empty():
            return False
        cur = self.__head
        while cur.next != self.__head:
            if cur.item == item:
                return True
            else:
                cur = cur.next
        # Quit the loop, handle the current node
        if cur.item == item:
            return True
        return False

def main():
    single_ll = SingleCycleLinkList()
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
        print("find 22")
    if not single_ll.search(23):
        print("Not find 23")
    single_ll.remove(11)
    single_ll.travel()
    single_ll.remove(9)
    single_ll.travel()
    single_ll.remove(22)
    single_ll.travel()

if __name__ == '__main__':
    main()
