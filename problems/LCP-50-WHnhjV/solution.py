# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:31:48Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def giveGem(self, gem: List[int], operations: List[List[int]]) -> int:
        for source, target in operations:
            amount = gem[source] // 2
            gem[source] -= amount
            gem[target] += amount
        return max(gem) - min(gem)
