# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# Name:        Binary Sort Tree
# Purpose:
#
# Author:      kkewang
#
# Created:     16/06/2019
# Copyright:   (c) kkewang 2019
# Licence:     <your licence>
# -------------------------------------------------------------------------------
class BSTNode:
    """
    Define node of binary tree
    """

    def __init__(self, data, lchild=None, rchild=None):
        """        
        :param data: data of node
        :param lchild: left child of node
        :param rchild: right child of node
        """
        self.data = data
        self.lchild = lchild
        self.rchild = rchild


class BinarySortTree:
    """
    Binary sort tree with BSTnode class node
    """

    def __init__(self):
        self._root = None

    def is_empty(self):
        return self._root is None

    def search(self, key):
        """        
        :param key: Searching key of node
        :return: Return node or None
        """
        bt = self._root
        while bt:
            entry = bt.data
            if key < entry:
                bt = bt.lchild
            elif key > entry:
                bt = bt.rchild
            else:
                return entry
        return None

    def insert(self, key):
        """
        BST insert operation
        :param key: key of node
        :return: boolean
        """
        # Empty tree
        if self.is_empty():
            self._root = BSTNode(key)
            return
        # Non-empty tree
        bt = self._root
        while True:           
            if key < bt.data:
                if bt.lchild is None:
                    bt.lchild = BSTNode(key)
                    return
                bt = bt.lchild
            elif key > bt.data:
                if bt.rchild is None:
                    bt.rchild = BSTNode(key)
                    return
                bt = bt.rchild
            else:  # existed key, do nothing
                bt.data = key
                return

    def delete(self, key):
        """
        Every time deleted node,  need to adjust the remaining nodes to be sortable
        :param key: The deleted key of node
        :return: boolean
        """
        parent, node = None, self._root
        # find the node to be deleted
        while node and node.data != key:
            parent = node
            if key < node.data:
                node = node.lchild
            else:
                node = node.rchild
            if node is None:
                return
        # save the found node
        q = node
        # Find rear node of the deleted node in order traversal
        # There is four cases: 1. leaf node(no child) 2.only left child
        # 3. only right child 4. both left and rifht childs
        if q.lchild and q.rchild:
            parent = q            
            node = q.rchild
            while node.lchild:
                parent = node
                node = node.lchild
        # Get the final child in either case of deleted node
        # 1.child is None, 2. child is left child, 3. child is right child
        # 4.child is node's left subtree's far right child
        child = ( node.lchild if node.lchild else node.rchild)
        # Delete root node
        if parent is None:
            self._root = child
        else: 
            # Deleting node in either case, The final operation is 
            # to connect the child of the parent node that deleted the node 
            # to its rear node in order traversal 
            if parent.lchild is node:                
                parent.lchild = child
            else:
                parent.rchild = child
            # Only the case, node is q node's left subtree's far right child
            if node is not q:
                q.data = node.data
                
    def _pre_order(self, node=None):

        if node is None:
            node = self._root

        yield node.data

        if node.lchild is not None:
            for item in self._pre_order(node.lchild):
                yield item
        if node.rchild is not None:
            for item in self._pre_order(node.rchild):
                yield item

    def _in_order(self, node=None):
        if node is None:
            node = self._root

        if node.lchild is not None:
            for item in self._in_order(node.lchild):
                yield item

        yield node.data

        if node.rchild is not None:
            for item in self._in_order(node.rchild):
                yield item

    def _in_order1(self):
        """
        Implement the binary traversal algorithm of the binary tree,
        Show the binary sort tree we created
        Using Python's built-in list directly as a stack.
        :return: data
        """
        stack = []
        node = self._root
        while node or stack:
            while node:
                stack.append(node)
                node = node.lchild
            node = stack.pop()
            yield node.data
            node = node.rchild

    def _post_order(self, node=None):
        if node is None:
            node = self._root

        if node.lchild is not None:
            for item in self._post_order(node.lchild):
                yield item

        if node.rchild is not None:
            for item in self._post_order(node.rchild):
                yield item

        yield node.data

    def pre_order(self):
        return list(self._pre_order())

    def in_order(self):
        return list(self._in_order())  # return list(self._in_order1())

    def post_order(self):
        return list(self._post_order())

    def Print(self):
        resultArray = []
        if not self._root:
            return resultArray
        curLayerNodes = [self._root]
        isEvenLayer = True
        while curLayerNodes:
            curLayerValues = []
            nextLayerNodes = []
            isEvenLayer = not isEvenLayer
            for node in curLayerNodes:
                curLayerValues.append(node.data)
                if node.lchild:
                    nextLayerNodes.append(node.lchild)
                if node.rchild:
                    nextLayerNodes.append(node.rchild)
                    curLayerNodes = nextLayerNodes
                    resultArray.append(curLayerValues[::-1]) if isEvenLayer else resultArray.append(curLayerValues)
        return resultArray


"""Binary sorted tree
lis = [62, 55, 88, 47, 73, 99, 35, 51, 93, 37]
                            62
                55                    88
        47                   73                 99
35             51                        93
      37

lis = [62, 55, 88, 47, 73, 99, 35, 51, 93, 37, 58]
                            62
                55                      88
        47           58      73                 99
35             51                         93
      37

lis = [62, 55, 88, 47, 73, 99, 35, 51, 93, 37, 58, 57]
                                        62
                     55                                        88
        47                        58          73                         99
35            51         57                                     93
      37
"""
from ppBT import PrintBT
import random

if __name__ == '__main__': 
    # Created a BST
    bs_tree = BinarySortTree()
    print("Create a Binary sort tree from random list:")
    for _ in range(16):
        bs_tree.insert(random.randint(0, 100))             
    PrintBT(bs_tree)
    print "Pre order traverse:", bs_tree.pre_order()
    print "In order traverse:", bs_tree.in_order()
    print "Post order traverse:", bs_tree.post_order()    
    
    #Delete one key
    alist = [61, 62, 55, 88, 47, 73, 99, 35, 51, 93, 37, 58, 57, 59, 60, 63, 65]
    bs_tree1 = BinarySortTree()
    print "-" * 40
    print("Create a Binary sort tree from list %s:" % alist)
    for i in range(len(alist)):
        bs_tree1.insert(alist[i])
    PrintBT(bs_tree1)
    print "Pre order traverse :", bs_tree1.pre_order()
    print "In order traverse：", bs_tree1.in_order    ()

    key = 61
    print("Deleting one node with key: {}".format(key))
    bs_tree1.delete(key)
    
    PrintBT(bs_tree1)
    print "Pre order traverse :", bs_tree1.pre_order()
    print "In order traverse：", bs_tree1.in_order()

