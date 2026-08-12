# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:03:17Z
# Experiment: ai-leetcode-lab, round 1
"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""
class Node:
    def __init__(self, val, isLeaf, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val, self.isLeaf = val, isLeaf
        self.topLeft, self.topRight = topLeft, topRight
        self.bottomLeft, self.bottomRight = bottomLeft, bottomRight
from typing import List

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def build(row,col,size):
            value=grid[row][col]
            if all(grid[i][j]==value for i in range(row,row+size) for j in range(col,col+size)): return Node(bool(value),True,None,None,None,None)
            half=size//2
            return Node(True,False,build(row,col,half),build(row,col+half,half),build(row+half,col,half),build(row+half,col+half,half))
        return build(0,0,len(grid))
