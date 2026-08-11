# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T16:08:29Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        triples = []
        for index, first in enumerate(nums):
            if index > 0 and first == nums[index - 1]:
                continue
            if first > 0:
                break
            left, right = index + 1, len(nums) - 1
            while left < right:
                total = first + nums[left] + nums[right]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    triples.append([first, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
        return triples
