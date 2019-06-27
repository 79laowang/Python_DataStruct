# coding:utf-8
#-------------------------------------------------------------------------------
# Name:        binary_tree.py
# Purpose:    Binary tree implementation"
#
# Author:      Ke Wang
#
# Created:     04/06/201
# Copyright:   (c) Ke Wang 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from ppBT import PrintBT

class Node(object):
    """Binary tree node"""
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None

class BTree(object):
    """Binary tree"""
    def __init__(self):
        self._root = None

    def add(self, data):
        node = Node(data)
        if self._root is None:
            self._root = node
            return
        queue = [self._root]
        # Find a correct position to add node until queue is empty
        while queue:
            cur_node = queue.pop(0)
            if cur_node.lchild is None:
                cur_node.lchild = node
                return
            else:
                queue.append(cur_node.lchild)
            if cur_node.rchild is None:
                cur_node.rchild = node
                return
            else:
                queue.append(cur_node.rchild)

    def breadth_travel(self):
        """breadth travel binary tree"""
        if self._root is None:
            return
        queue = [self._root]
        while queue:
            cur_node = queue.pop(0)
            print cur_node.data,
            if cur_node.lchild is not None:
                queue.append(cur_node.lchild)
            if cur_node.rchild is not None:
                queue.append(cur_node.rchild)

    def preorder_travel(self, node):
        if node is None:
            return
        print node.data,
        self.preorder_travel(node.lchild)
        self.preorder_travel(node.rchild)

    def inorder_travel(self, node):
        if node is None:
            return
        self.inorder_travel(node.lchild)
        print node.data,
        self.inorder_travel(node.rchild)

    def postorder_travel(self, node):
        if node is None:
            return
        self.postorder_travel(node.lchild)
        self.postorder_travel(node.rchild)
        print node.data,

def main():
    btree = BTree()
    btree.add(1)
    btree.add(2)
    btree.add(3)
    btree.add(4)
    btree.add(5)
    btree.add(6)
    btree.add(7)
    btree.add(8)
    btree.add(9)
    PrintBT(btree)
    print("Breadth travel:")
    btree.breadth_travel()
    print("\nPreorder travel:")
    btree.preorder_travel(btree._root)
    print("\nInorder travel:")
    btree.inorder_travel(btree._root)
    print("\nPostorder travel:")
    btree.postorder_travel(btree._root)

if __name__ == '__main__':
    main()
