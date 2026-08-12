# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T08:09:57Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class TreeAncestor:

    def __init__(self, n: int, parent: List[int]):
        self.up=[parent]
        for _ in range(16):self.up.append([self.up[-1][x] if x>=0 else -1 for x in self.up[-1]])

    def getKthAncestor(self, node: int, k: int) -> int:
        for i in range(len(self.up)):
            if k>>i&1:
                node=self.up[i][node]
                if node<0:return -1
        return node


# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)
