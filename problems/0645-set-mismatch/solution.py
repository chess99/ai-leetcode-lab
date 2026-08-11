# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T10:52:17Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        seen = set()
        duplicate = 0
        for value in nums:
            if value in seen:
                duplicate = value
            seen.add(value)
        missing = len(nums) * (len(nums) + 1) // 2 - sum(seen)
        return [duplicate, missing]
