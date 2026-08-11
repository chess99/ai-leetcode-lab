# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T13:20:23Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def fillCups(self, amount: List[int]) -> int:
        return max(max(amount), (sum(amount)+1)//2)
