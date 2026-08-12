# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T05:38:12Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        def subsequence(nums, length):
            drop = len(nums) - length
            stack = []
            for digit in nums:
                while drop and stack and stack[-1] < digit:
                    stack.pop()
                    drop -= 1
                stack.append(digit)
            return stack[:length]

        def merge(left, right):
            result = []
            left_index = right_index = 0
            while left_index < len(left) or right_index < len(right):
                if left[left_index:] > right[right_index:]:
                    result.append(left[left_index])
                    left_index += 1
                else:
                    result.append(right[right_index])
                    right_index += 1
            return result

        answer = []
        for take1 in range(max(0, k - len(nums2)), min(k, len(nums1)) + 1):
            candidate = merge(subsequence(nums1, take1),
                              subsequence(nums2, k - take1))
            answer = max(answer, candidate)
        return answer
