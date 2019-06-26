# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# Name:        Print pretty Binary Tree
# Purpose:
#
# Author:      kkewang
#
# Created:     16/06/2019
# Copyright:   (c) kkewang 2019
# Licence:     <your licence>
# -------------------------------------------------------------------------------
class PrintBT:
    """
    Usage:
    from ppBT import PrintBT
    PrintBT(BTree)
    """
    def __init__(self, BSTree):
        # If the tree is empty, return
        if BSTree._root is None:
            return        
        self.display(BSTree._root)
    
    def display(self, node):
        lines, _, _, _ = self._display_aux(node)
        for line in lines:
            print(line)
    
    def _display_aux(self, node):
        """Returns list of strings, width, height, and horizontal coordinate of the root.
        line: output content of each lines for each height nodes 
        height :  The height of a binary tree
        width : The node output width of the binary tree
        middle: The horizontal coordinate of the root.
        """
        # No child.
        if node.rchild is None and node.lchild is None:
            line = '%s' % node.data
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle
    
        # Only left child.
        if node.rchild is None:
            lines, n, p, x = self._display_aux(node.lchild)
            s = '%s' % node.data
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2
    
        # Only right child.
        if node.lchild is None:
            lines, n, p, x = self._display_aux(node.rchild)
            s = '%s' % node.data
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2
    
        # Two children.
        left, n, p, x = self._display_aux(node.lchild)
        right, m, q, y = self._display_aux(node.rchild)
        s = '%s' % node.data
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y+3) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2
