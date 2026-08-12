# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T12:52:01Z
# Experiment: ai-leetcode-lab, round 1
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List, Optional
class Solution:
    def canMerge(self, trees: List[TreeNode]) -> Optional[TreeNode]:
        roots={tree.val:tree for tree in trees};children=set()
        for tree in trees:
            if tree.left:children.add(tree.left.val)
            if tree.right:children.add(tree.right.val)
        candidates=[tree for tree in trees if tree.val not in children]
        if len(candidates)!=1:return None
        root=candidates[0];used={root.val}
        def validate(node,low,high):
            if not node:return True
            if not low<node.val<high:return False
            if node.left is None and node.right is None and node.val in roots and node.val not in used:
                graft=roots[node.val];node.left,node.right=graft.left,graft.right;used.add(node.val)
            return validate(node.left,low,node.val) and validate(node.right,node.val,high)
        return root if validate(root,float('-inf'),float('inf')) and len(used)==len(trees) else None
