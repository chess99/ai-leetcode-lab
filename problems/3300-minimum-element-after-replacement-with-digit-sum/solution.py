# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:57:07Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def minElement(self, nums: List[int]) -> int:
        return min(sum(map(int, str(num))) for num in nums)
