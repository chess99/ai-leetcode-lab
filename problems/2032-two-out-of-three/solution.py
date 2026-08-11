# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T13:03:08Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        sets = (set(nums1), set(nums2), set(nums3))
        return [value for value in set().union(*sets) if sum(value in values for values in sets) >= 2]
