# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T18:34:25Z
# Experiment: ai-leetcode-lab, round 1
# Definition for a binary tree node.

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string."""
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
        """Decodes your encoded data to tree."""
        values = iter(data.split(','))
        first = next(values)
        if first == '#':
            return None
        root = TreeNode(int(first))
        stack = [(root, 0)]
        for value in values:
            node, state = stack[-1]
            child = None if value == '#' else TreeNode(int(value))
            if state == 0:
                node.left = child
                stack[-1] = (node, 1)
            else:
                node.right = child
                stack.pop()
            if child is not None:
                stack.append((child, 0))
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
