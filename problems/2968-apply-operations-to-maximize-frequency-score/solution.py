# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T15:15:50Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def maxFrequencyScore(self, nums: List[int], k: int) -> int:
        nums.sort()
        prefix = [0]
        for value in nums:
            prefix.append(prefix[-1] + value)
        left = 0
        answer = 1
        for right in range(len(nums)):
            while left <= right:
                middle = (left + right) // 2
                cost = (
                    nums[middle] * (middle - left) - (prefix[middle] - prefix[left])
                    + (prefix[right + 1] - prefix[middle + 1])
                    - nums[middle] * (right - middle)
                )
                if cost <= k:
                    break
                left += 1
            answer = max(answer, right - left + 1)
        return answer
