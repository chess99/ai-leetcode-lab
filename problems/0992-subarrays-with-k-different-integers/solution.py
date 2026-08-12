# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T06:20:06Z
# Experiment: ai-leetcode-lab, round 1
from collections import defaultdict
from typing import List


class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def at_most(limit):
            counts = defaultdict(int)
            left = answer = 0
            for right, value in enumerate(nums):
                if counts[value] == 0:
                    limit -= 1
                counts[value] += 1
                while limit < 0:
                    counts[nums[left]] -= 1
                    if counts[nums[left]] == 0:
                        limit += 1
                    left += 1
                answer += right - left + 1
            return answer

        return at_most(k) - at_most(k - 1)
