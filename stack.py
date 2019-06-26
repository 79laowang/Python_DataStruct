#-------------------------------------------------------------------------------
# Name:        Stack operations
# Purpose:
#
# Author:      kkewang
#
# Created:     12/05/2019
# Copyright:   (c) kkewang 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class Stack(object):
    """ implment stack """
    def __init__(self):
        self.__list = []

    def push(self, item):
        """ push in stack  """
        self.__list.append(item)

    def pop(self):
        return self.__list.pop()

    def peek(self):
        if self.__list:
            return self.__list[-1]
        else:
            return None

    def is_empty(self):
        #return self.__list == []
        return not self.__list

    def size(self):
        return len(self.__list)

def main():
    s = Stack()
    for x in range(10):
        s.push(x)
    print('pop(): ' + str(s.pop()))
    print('pop(): ' + str(s.pop()))
    print('pop(): ' + str(s.pop()))

    if s.is_empty:
        print('peek(): ' + str(s.peek()))
    else:
        print("Empty list!")

if __name__ == '__main__':
    main()

