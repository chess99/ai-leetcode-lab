# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T05:38:17Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def sort(left, right):
            if right - left <= 1:
                return 0
            middle = (left + right) // 2
            answer = sort(left, middle) + sort(middle, right)
            second = middle
            for first in range(left, middle):
                while second < right and nums[first] > 2 * nums[second]:
                    second += 1
                answer += second - middle
            merged = []
            first, second = left, middle
            while first < middle or second < right:
                if second == right or (first < middle and nums[first] <= nums[second]):
                    merged.append(nums[first]); first += 1
                else:
                    merged.append(nums[second]); second += 1
            nums[left:right] = merged
            return answer
        return sort(0, len(nums))
