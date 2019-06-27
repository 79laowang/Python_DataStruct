# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# Name:        avl_tree.py
# Purpose:    AVL tree: self-balancing Binary Search Tree
#
# Author:      Ke Wang
#
# Created:     16/06/2019
# Copyright:   (c) Ke Wang 2019
# Licence:     <your licence>
# -------------------------------------------------------------------------------

from ppBT import PrintBT


class AVLNode(object):
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None
        self.height = 0


class AVLTree(object):
    """ AVL tree: self-balancing Binary Search Tree
    """

    def __init__(self):
        self._root = None

    def find(self, data):
        if self._root is None:
            return None
        else:
            return self._find(data, self._root)

    def _find(self, data, node):
        if node is None:
            return None
        elif data < node.data:
            return self._find(data, self.lchild)
        elif data > node.data:
            return self._find(data, self.rchild)
        else:
            return node

    def findMin(self):
        if self._root is None:
            return None
        else:
            return self._findMin(self._root)

    def _findMin(self, node):
        if node.lchild:
            return self._findMin(node.lchild)
        else:
            return node

    def findMax(self):
        if self._root is None:
            return None
        else:
            return self._findMax(self._root)

    def _findMax(self, node):
        if node.rchild:
            return self._findMax(node.rchild)
        else:
            return node

    def height(self, node):
        # empty tree with height is -1
        return node.height if node else -1    

    def right_rotate(self, node):
        """
        Insert new on node's left child of left subtree 
                                node                                      node_left
                             /            \                               /                \
                  node_left           S3     =>                S1                node
                  /            \                                      /                /         \
              S1                S2                                New           S2         S3
              /
         New
        Node: right rotate node
        Return: rotated  node of AVL subtree as root
        """
        node_left = node.lchild
        node.lchild = node_left.rchild
        node_left.rchild = node
        node.height = max(self.height(node.rchild), self.height(node.lchild)) + 1
        node_left.height = max(self.height(node_left.lchild), node.height) + 1
        return node_left

    def left_rotate(self, node):
        """
        Insert new on node's right child of right subtree
                    node                                    node_right
                /            \                               /                \
               S1    node_right   =>            node              S3
                      /            \                    /         \              \
                   S2               S3              S1         S2            New
                                        \
                                       New
        Node: left rotate node
        Return: rotated  node of AVL subtree as root
        """        
        node_right = node.rchild
        node.rchild = node_right.lchild
        node_right.lchild = node
        node.height = max(self.height(node.rchild), self.height(node.lchild)) + 1
        node_right.height = max(self.height(node_right.rchild), node.height) + 1
        return node_right

    def right_left_rotate(self, node):
        """
        Insert new on node's left child of right subtree
        h -> Depth of leaf node
        bf -> balance factor = Depth of left subtree - Depth of right subtree
                    A(bf=1)                                    A(bf=2)                                    C(bf=1)
                 /              \                               /             \                             /                 \
            B(bf=-1)   Ar(h-1)        =>         B(bf=-2)     Ar(h-1)        =>    B(bf=0)         A(bf=0)    
            /        \                                       /        \                               /       \           /         \
        Bl(h-1)    C(bf=0)                       Bl(h-1)   C(bf=1)               Bl(h-1)   Cl(bf=1)  Cr(h-1)   Ar(h-1) 
                    /     \                                           /     \                             /         \
                Cl(h)   Cr(h)                                    Cl(h)   Cr(h)               New(h)   [new]
                                                                       /       \
                                                             New(h+1)    [new]
                                        After add new node, the B node bf =-2 which is
                                        the closest unbalanced parent node to the new node
                                        Take B as the axis, Rotate C to the right frist, after that,
                                        Take C as the axis, Rotate A to the left.
        A -> node
        B -> node.lchild
        C -> B.rchild
        """                   
        node.lchild = self.left_rotate(node.lchild)
        return self.right_rotate(node)        
    
    def left_right_rotate(self, node):
        """
        Insert new on node's right child of left subtree
        h -> Depth of leaf node
        bf -> balance factor = Depth of left subtree - Depth of right subtree
                    A(bf=1)                                    A(bf=-2)                                      C(bf=1)
                 /              \                               /             \                               /                     \
            Al(h-1)     B(bf=1)           =>     Al(h-1)      B(bf=2)        =>       A(bf=0)                B(bf=0)    
                         /             \                                   /        \                   /       \               /              \
                   C(bf=0)     Br(h-1)                      C(bf=1)     Br(h-1)      Al(h-1)   Cl(bf=1)  Cr(h-1)   Br(h-1) 
                    /      \                                           /     \                             /         \
                Cl(h)    Cr(h)                             Cl(bf=1)   Cr(h)               New(h)   [new]
                                                                    /           \
                                                             New(h+1)    [new]
                                        After add new node, the B node bf =2 which is
                                        the closest unbalanced parent node to the new node
                                        Take B as the axis, Rotate C to the left frist, after that,
                                        Take C as the axis, Rotate A to the right.
        A -> node
        B -> node.rchild
        C -> B.lchild        
        """          
        node.rchild = self.right_rotate(node.rchild)
        return self.left_rotate(node)        

    def insert(self, data):
        # If tree is empty, new node is root
        if self._root is None:
            self._root = AVLNode(data)
        else:
            self._root = self._insert(data, self._root)

    def _insert(self, data, node):
        """
        data: new node
        node: root of tree
        Inserting a new node operation is always at the leaf node of tree
        """
        # Recursive end condition
        if node is None:
            node = AVLNode(data)
        elif data < node.data:
            # Recursive insertion node
            node.lchild = self._insert(data, node.lchild)
            # If the tree lost balance, do re-balance operation
            if (self.height(node.lchild) - self.height(node.rchild)) == 2:
                # LL scenario(Insert new on node's left child of left subtree)
                if data < node.lchild.data:
                    # LR scenario(Insert new on node's left child of right subtree) 
                    node = self.right_rotate(node)
                else:
                    node = self.right_left_rotate(node)
        elif data > node.data:
            node.rchild = self._insert(data, node.rchild)
            if (self.height(node.rchild) - self.height(node.lchild)) == 2:
                # RR scenario (Insert new on node's right child of right subtree)
                if data < node.rchild.data:
                    # RL scenario(Insert new on node's right child of left subtree) 
                    node = self.left_right_rotate(node)
                else:
                    node = self.left_rotate(node)
        # Update height of the node
        node.height = max(self.height(node.rchild), self.height(node.lchild)) + 1
        return node

    def delete(self, data):
        self._root = self.remove(data, self._root)

    def remove(self, data, node):
        """        
        Scenario A: Deleted the leaf node
        Scenario B: Deleted node only left subtree or right subtree
        For A and B, how to: 
            1. Only replace node with it's left or right child(leaf node's child node is None)
            2. If the deleted node's parent node lost balance, do re-balance operation
        Scenario C: Deleted node with both left and right subtree
        How to:
            1.If the height of the left subtree is relatively high, 
            the node with the largest value of the left subtree is selected, 
            assign the value to the current node, and the node with the largest value is deleted; 
            2.If the height of the right subtree is relatively high,
            the lowest value of the middle subtree is selected, 
            assign the value to the current node and delete the node with the smallest value. 
            3.Finally dodo re-balance operation.
        
        h -> Depth of leaf node
        bf -> balance factor = Depth of left subtree - Depth of right subtree
        abs(bf) == 2, lost balance
        - Delete node Al of Node left subtree,  
        1. RR scenario: B.richild.height >= B.lchild.height, do left rotation on node A 
              A(bf=-1)                                A(bf=-2)                                  B(bf=1)    
            /             \                             (          \                                 /               \
        Al(h-1)    B(bf=0)             =>      \       B(bf=0)        =>     A(bf=-1)         Br(h)  
                    /         \                           V    /        \                           \
                  Bl(h)     Br(h)                       Bl(h)      Br(h)                         Bl(h+1)
        
        2. RL scenario:  B.richild.height < B.lchild.height, do right rotation on node Bl first, 
            do left rotation on node A.
              A(bf=-1)                            A(bf=-2)                     A(bf=-2)                   Bl(bf=0)         
            /             \                        ^             \                 /       \                        /             \       
        Al(h-1)    B(bf=0)         =>     |         B(bf=1)    =>   |   Bl(bf=-1)    =>     A(h)           B(h)      
                    /                                \    /                         V         \
                  Bl(h)                               Bl(h)                                    B 

        - Delete node Ar of Node right subtree, 
        1.LL scenario: B.richild.height >= B.lchild.height, do right rotation on node A 
               A(bf=1)                                A(bf=2)                          B(bf=-1)                
              /            \                           /               )                      /        \
            B(bf=0)    Ar(h-1)      =>      B(bf=0)      /       =>        Bl(h)      A(bf=-1) 
           /        \                               /        \     V                                  /
        Bl(h)     Br(h)                        Bl(h)     Br(h)                                  Br(h+1)
        
        2.LR scenario:  B.richild.height < B.lchild.height, do left rotation on node Br first, 
             do right rotation on node A.
        
                A(bf=1)                                A(bf=2)                          A(bf=2)                   Br(bf=0)        
              /            \                           /             ^                       /              )              /           \
            B(bf=0)    Ar(h-1)      =>      B(bf=-1)     \       =>       Br(bf=1)     /     =>   B(h)       A(h)
                   \                                          \         )                   /              V
                  Br(h)                                     Br(h)                     Br(h)
        """
        # Not found the deleted node
        if node is None:
            raise dataError, 'Error,data not in tree'
        elif data < node.data:
            node.lchild = self.remove(data, node.lchild)
            # The found node was deleted,  Recursively popping the top node from the stack and checking balance state
            # if current node's bf=2, do re-balance
            if (self.height(node.rchild) - self.height(node.lchild)) == 2:                
                if self.height(node.rchild.rchild) >= self.height(node.rchild.lchild):
                    # RR scenario
                    node = self.left_rotate(node)                
                else:
                    # RL scenario
                    node = self.left_right_rotate(node)
            node.height = max(self.height(node.lchild), self.height(node.rchild)) + 1
        elif data > node.data:
            node.rchild = self.remove(data, node.rchild)
            if (self.height(node.lchild) - self.height(node.rchild)) == 2:
                if self.height(node.lchild.lchild) >= self.height(node.lchild.rchild):
                    # LL scenario
                    node = self.right_rotate(node)
                else:
                     # LR scenario
                    node = self.right_left_rotate(node)
            node.height = max(self.height(node.lchild), self.height(node.rchild)) + 1
        # Found deleted node with left and right chiild
        elif node.lchild and node.rchild:
            # Right subtree is higher
            if node.lchild.height <= node.rchild.height:
                minAVLNode = self._findMin(node.rchild)
                node.data = minAVLNode.data
                node.rchild = self.remove(node.data, node.rchild)
            else:
                maxAVLNode = self._findMax(node.lchild)
                node.data = maxAVLNode.data
                node.lchild = self.remove(node.data, node.lchild)
            node.height = max(self.height(node.lchild), self.height(node.rchild)) + 1
        # Found deleted node only left or right child or no child
        else:
            if node.rchild:
                node = node.rchild
            else:
                node = node.lchild

        return node

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
        return list(self._in_order())

    def post_order(self):
        return list(self._post_order())


if __name__ == '__main__':
    #lis = [62, 55, 88, 47, 73, 99, 35, 51, 93, 37]
    #lis = [62, 55, 88, 47, 73, 99, 35, 51, 93, 37,58]
    #lis = [62, 55, 88, 47, 73, 99, 35, 51, 93, 37, 58, 57,100,1]
    lis = [6,1,3,5,10]
    avl_tree = AVLTree()
    print("Create a AVL tree from list %s:" % lis)
    for i in range(len(lis)):
        avl_tree.insert(lis[i])

    PrintBT(avl_tree)
    print "Pre order traverse:", avl_tree.pre_order()
    print "In order traverse:", avl_tree.in_order()
    print "Post order traverse:", avl_tree.post_order()
    print "-" * 40
    data = 1
    print "Deleting node only left child:%s"  % data
    avl_tree.delete(data)
    PrintBT(avl_tree)
    print "-" * 40
    data = 10
    print "Deleting node only right child:%s"  % data
    avl_tree.delete(data)
    PrintBT(avl_tree)    
    print "-" * 40
    data = 5
    print "Deleting node with left and right childs:%s"  % data
    avl_tree.delete(data)
    PrintBT(avl_tree)
