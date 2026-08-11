# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:49:32Z
# Experiment: ai-leetcode-lab, round 1
from collections import deque
from typing import List


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maximums = deque()
        minimums = deque()
        left = 0
        best = 0
        for right, value in enumerate(nums):
            while maximums and nums[maximums[-1]] < value:
                maximums.pop()
            while minimums and nums[minimums[-1]] > value:
                minimums.pop()
            maximums.append(right)
            minimums.append(right)
            while nums[maximums[0]] - nums[minimums[0]] > limit:
                if maximums[0] == left:
                    maximums.popleft()
                if minimums[0] == left:
                    minimums.popleft()
                left += 1
            best = max(best, right - left + 1)
        return best
