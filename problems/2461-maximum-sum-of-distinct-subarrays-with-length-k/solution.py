# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:37:20Z
# Experiment: ai-leetcode-lab, round 1

from collections import defaultdict
from typing import List


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        counts = defaultdict(int)
        window_sum = 0
        answer = 0

        for right, value in enumerate(nums):
            counts[value] += 1
            window_sum += value

            if right >= k:
                left_value = nums[right - k]
                counts[left_value] -= 1
                if counts[left_value] == 0:
                    del counts[left_value]
                window_sum -= left_value

            if right >= k - 1 and len(counts) == k:
                answer = max(answer, window_sum)

        return answer
