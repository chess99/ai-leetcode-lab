# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T16:18:30Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def numTrees(self, n: int) -> int:
        counts = [0] * (n + 1)
        counts[0] = 1
        for nodes in range(1, n + 1):
            for left_nodes in range(nodes):
                counts[nodes] += counts[left_nodes] * counts[nodes - 1 - left_nodes]
        return counts[n]
