# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:23:52Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def sumOfGoodIntegers(self, n: int, k: int) -> int:
        return sum(x for x in range(max(1, n - k), n + k + 1) if n & x == 0)
