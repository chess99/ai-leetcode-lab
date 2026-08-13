# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:55:39Z
# Experiment: ai-leetcode-lab, round 1
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        pairs = 0
        distances = {}
        stack = [(root, False)]

        while stack:
            node, exiting = stack.pop()
            if not node:
                continue
            if not exiting:
                stack.append((node, True))
                stack.append((node.right, False))
                stack.append((node.left, False))
                continue

            if not node.left and not node.right:
                distances[node] = [1]
                continue

            left = distances.pop(node.left, [])
            right = distances.pop(node.right, [])
            pairs += sum(a + b <= distance for a in left for b in right)
            distances[node] = [
                steps + 1 for steps in left + right if steps + 1 < distance
            ]

        return pairs
