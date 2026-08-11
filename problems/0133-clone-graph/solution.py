# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T16:24:46Z
# Experiment: ai-leetcode-lab, round 1
from typing import Optional


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if not node:
            return None
        clones = {node: Node(node.val)}
        stack = [node]
        while stack:
            original = stack.pop()
            for neighbor in original.neighbors:
                if neighbor not in clones:
                    clones[neighbor] = Node(neighbor.val)
                    stack.append(neighbor)
                clones[original].neighbors.append(clones[neighbor])
        return clones[node]
