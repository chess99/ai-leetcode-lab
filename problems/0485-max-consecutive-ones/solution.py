# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T10:41:26Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        best = current = 0
        for value in nums:
            if value:
                current += 1
                best = max(best, current)
            else:
                current = 0
        return best
