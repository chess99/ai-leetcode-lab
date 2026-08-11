# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:23:06Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        chosen, value, total = set(), 1, 0
        while len(chosen) < n:
            if k - value not in chosen: chosen.add(value); total += value
            value += 1
        return total
