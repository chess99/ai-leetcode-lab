# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:31:19Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        first,second=set(nums1),set(nums2);return [sum(value in second for value in first),sum(value in first for value in second)]
