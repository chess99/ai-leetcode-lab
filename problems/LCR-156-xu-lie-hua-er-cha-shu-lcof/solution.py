# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T18:34:28Z
# Experiment: ai-leetcode-lab, round 1
# Definition for a binary tree node.

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string."""
        if root is None:
            return '#'
        output, queue = [], [root]
        for node in queue:
            if node is None:
                output.append('#')
            else:
                output.append(str(node.val))
                queue.extend((node.left, node.right))
        while output[-1] == '#':
            output.pop()
        return ','.join(output)

    def deserialize(self, data):
        """Decodes your encoded data to tree."""
        if data == '#':
            return None
        values = data.split(',')
        root = TreeNode(int(values[0]))
        queue = [root]
        index = 1
        for node in queue:
            if index < len(values):
                if values[index] != '#':
                    node.left = TreeNode(int(values[index]))
                    queue.append(node.left)
                index += 1
            if index < len(values):
                if values[index] != '#':
                    node.right = TreeNode(int(values[index]))
                    queue.append(node.right)
                index += 1
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
