# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T04:15:16Z
# Experiment: ai-leetcode-lab, round 1
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def closeLampInTree(self, root: 'TreeNode') -> int:
        infinity = 10 ** 9
        table = {}
        stack = [(root, False)]
        while stack:
            node, visited = stack.pop()
            if not node:
                continue
            if not visited:
                stack.append((node, True))
                stack.append((node.right, False))
                stack.append((node.left, False))
                continue
            current = [[infinity] * 2 for _ in range(2)]
            left = table.get(id(node.left), [[0, 0], [0, 0]])
            right = table.get(id(node.right), [[0, 0], [0, 0]])
            for subtree_flip in (0, 1):
                for parent_local_flip in (0, 1):
                    for switch1 in (0, 1):
                        for switch2 in (0, 1):
                            for switch3 in (0, 1):
                                state = (node.val ^ subtree_flip ^ parent_local_flip
                                         ^ switch1 ^ switch2 ^ switch3)
                                if state:
                                    continue
                                child_subtree = subtree_flip ^ switch2
                                cost = switch1 + switch2 + switch3
                                cost += left[child_subtree][switch3]
                                cost += right[child_subtree][switch3]
                                current[subtree_flip][parent_local_flip] = min(
                                    current[subtree_flip][parent_local_flip], cost
                                )
            table[id(node)] = current
        return table[id(root)][0][0]
