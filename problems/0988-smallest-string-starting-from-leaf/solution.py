# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:06:56Z
# Experiment: ai-leetcode-lab, round 1
# Definition for a binary tree node.
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        best = "{"
        stack = [(root, "")]
        while stack:
            node, path = stack.pop()
            path += chr(node.val + ord("a"))
            if not node.left and not node.right:
                best = min(best, path[::-1])
                continue
            if node.left:
                stack.append((node.left, path))
            if node.right:
                stack.append((node.right, path))
        return best
