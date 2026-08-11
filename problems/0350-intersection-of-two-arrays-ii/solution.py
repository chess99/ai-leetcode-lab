# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T10:32:11Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counts = {}
        for value in nums1:
            counts[value] = counts.get(value, 0) + 1
        result = []
        for value in nums2:
            if counts.get(value, 0):
                result.append(value)
                counts[value] -= 1
        return result
