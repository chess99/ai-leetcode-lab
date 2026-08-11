# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:07:33Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        common = set(nums1) & set(nums2)
        if common:
            return min(common)
        first, second = min(nums1), min(nums2)
        return min(10 * first + second, 10 * second + first)
