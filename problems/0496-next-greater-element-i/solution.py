# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T10:38:25Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greater = {}
        stack = []
        for value in nums2:
            while stack and stack[-1] < value:
                next_greater[stack.pop()] = value
            stack.append(value)
        return [next_greater.get(value, -1) for value in nums1]
