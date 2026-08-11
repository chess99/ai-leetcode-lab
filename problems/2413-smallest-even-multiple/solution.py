# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T13:59:16Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        return n if n%2==0 else n*2
