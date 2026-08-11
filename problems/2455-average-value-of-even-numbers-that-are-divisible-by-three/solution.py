# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:03:27Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def averageValue(self, nums: List[int]) -> int:
        values = [value for value in nums if value % 6 == 0]
        return sum(values) // len(values) if values else 0
