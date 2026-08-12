# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T05:38:11Z
# Experiment: ai-leetcode-lab, round 1
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return '#'
        output = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node is None:
                output.append('#')
            else:
                output.append(str(node.val))
                stack.append(node.right)
                stack.append(node.left)
        return ','.join(output)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        values = data.split(',')
        if values[0] == '#':
            return None
        root = TreeNode(int(values[0]))
        stack = [(root, 0)]
        for value in values[1:]:
            child = None if value == '#' else TreeNode(int(value))
            parent, state = stack[-1]
            if state == 0:
                parent.left = child
                stack[-1] = (parent, 1)
            else:
                parent.right = child
                stack.pop()
            if child is not None:
                stack.append((child, 0))
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
