# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T10:28:39Z
# Experiment: ai-leetcode-lab, round 1
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        result = []

        def dfs(node: TreeNode, path: str) -> None:
            path = f"{path}->{node.val}" if path else str(node.val)
            if not node.left and not node.right:
                result.append(path)
                return
            if node.left:
                dfs(node.left, path)
            if node.right:
                dfs(node.right, path)

        if root:
            dfs(root, "")
        return result
