# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T10:28:17Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ranges = []
        index = 0
        while index < len(nums):
            start = nums[index]
            while index + 1 < len(nums) and nums[index + 1] == nums[index] + 1:
                index += 1
            end = nums[index]
            ranges.append(str(start) if start == end else f"{start}->{end}")
            index += 1
        return ranges
