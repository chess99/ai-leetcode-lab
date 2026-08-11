# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T11:45:50Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        first, second = set(nums1), set(nums2)
        return [list(first - second), list(second - first)]
