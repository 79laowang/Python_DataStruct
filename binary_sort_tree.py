# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        Binary Sort Tree
# Purpose:
#
# Author:      kkewang
#
# Created:     16/06/2019
# Copyright:   (c) kkewang 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

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
            entry = bt.data

            if key < entry:
                if bt.lchild is None:
                    bt.lchild = BSTNode(key)
                bt = bt.lchild
            elif key > entry:
                if bt.rchild is None:
                    bt.rchild = BSTNode(key)
                bt = bt.rchild
            else: # existed key, do nothing
                bt.data = key
                return

    def delete(self, key):
        """
        Every time deleted node,  need to adjust the remaining nodes to be sortable
        :param key: The deleted key of node
        :return: boolean
        """
        parent, node = None, self._root
        if not node:
            print("Empty tree!")
            return False
        # Searching for the node specified to be deleted
        while node and node.data != key:
            parent = node
            if key < node.data:
                node = node.lchild
            else:
                node = node.rchild
            if not node:
                return
        # Case: Delete node from left child
        if parent != None and parent.lchild == node:
            # Left leaf node, delete it directly
            if node.lchild is None and node.rchild is None:
                parent.lchild = None
                del node
            # Only left child of deleted node
            elif node.lchild != None and node.rchild is None:
                parent.lchild = node.lchild
                del node
            # Only right child of deleted node
            elif node.rchild != None and node.lchild is None:
                parent.lchild = node.rchild
                del node
            # Both left and right nodes
            elif node.rchild != None and node.lchild != None:
                r = node.lchild
                p = node
                # Get the maximum right child of node to be deleted  
                while r.rchild:
                    p = r
                    r = r.rchild
                # Replace the deleted node with found maximum right child
                r.lchild = node.lchild
                r.rchild = node.rchild
                parent.lchild = r
                p.rchild = None
                del node
        # Case: Delete node from right child
        elif parent != None and parent.rchild == node:
            # Right leaf node, delete it directly
            if node.lchild is None and node.rchild is None:
                parent.rchild = None
            # Only left child of deleted node
            elif node.lchild != None and node.rchild is None:
                parent.rchild = node.lchild
           # Only right child of deleted node 
            elif node.rchild != None and node.lchild is None:
                parent.rchild = node.rchild
            # Both left and right nodes
            elif node.rchild != None and node.lchild != None:
                # Get the maximum node from left subtree
                r = node.lchild
                p = node
                if r.rchild:
                    while r.rchild:
                        p = r
                        r = r.rchild
                    if r.lchild:
                        p.rchild = r.lchild
                    r.lchild = node.lchild
                r.rchild = node.rchild
                parent.rchild = r
                del node
        # Delete root node
        elif parent is None:
            # Get the maximum node from left subtree
            r = node.lchild
            p = node
            # left subtree of root node has right child
            if r.rchild:
                while r.rchild:
                    p = r
                    r = r.rchild
                # Maximun right node is not leaf node, has left node
                if r.lchild:
                    p.rchild = r.lchild
                r.lchild = node.lchild
            #left subtree without right child 
            r.rchild = node.rchild
            self._root = r
            del node

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

    def _mid_order(self, node=None):
        if node is None:
            node = self._root

        if node.lchild is not None:
            for item in self._mid_order(node.lchild):
                yield item

        yield node.data

        if node.rchild is not None:
            for item in self._mid_order(node.rchild):
                yield item

    def _mid_order1(self):
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

    def mid_order(self):
        return list(self._mid_order()) # return list(self._mid_order1())

    def post_order(self):
        return list(self._post_order())


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
if __name__ == '__main__':
    #lis = [62, 55, 88, 47, 73, 99, 35, 51, 93, 37]
    #lis = [62, 55, 88, 47, 73, 99, 35, 51, 93, 37,58]
    lis = [62, 55, 88, 47, 73, 99, 35, 51, 93, 37, 58, 57]
    bs_tree = BinarySortTree()
    print("Create a Binary sort tree from list %s:" % lis)
    for i in range(len(lis)):
        bs_tree.insert(lis[i])

    print "pre order:", bs_tree.pre_order()
    print "middle order:", bs_tree.mid_order()
    print "post order:", bs_tree.post_order()

    key = 62
    print("Deleting one node with key: {}".format(key))
    bs_tree.delete(key)
    print "pre order:", bs_tree.pre_order()
    print "middle order：", bs_tree.mid_order()
