# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T15:15:49Z
# Experiment: ai-leetcode-lab, round 1
from collections import deque
from typing import List


class Solution:
    def findMaximumLength(self, nums: List[int]) -> int:
        size = len(nums)
        prefix = [0]
        for value in nums:
            prefix.append(prefix[-1] + value)
        dynamic = [0] * (size + 1)
        previous = [0] * (size + 1)
        candidates = deque([0])
        for index in range(1, size + 1):
            while len(candidates) > 1 and previous[candidates[1]] <= prefix[index]:
                candidates.popleft()
            best = candidates[0]
            dynamic[index] = dynamic[best] + 1
            previous[index] = 2 * prefix[index] - prefix[best]
            while candidates and previous[candidates[-1]] >= previous[index]:
                candidates.pop()
            candidates.append(index)
        return dynamic[size]
