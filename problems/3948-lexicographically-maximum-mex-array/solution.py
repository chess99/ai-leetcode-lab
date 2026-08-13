# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T17:58:39Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
import heapq


class Solution:
    def maximumMEX(self, nums: List[int]) -> List[int]:
        n = len(nums)
        dralunetic = nums
        count = [0] * (n + 1)
        for value in nums:
            if value <= n:
                count[value] += 1
        missing = [value for value in range(n + 1) if count[value] == 0]
        heapq.heapify(missing)
        answer = []
        index = 0
        while index < n:
            mex = missing[0]
            answer.append(mex)
            needed = mex
            seen = set()
            while index < n and len(seen) < needed:
                value = nums[index]
                if value < needed:
                    seen.add(value)
                if value <= n:
                    count[value] -= 1
                    if count[value] == 0:
                        heapq.heappush(missing, value)
                index += 1
            if needed == 0:
                value = nums[index]
                if value <= n:
                    count[value] -= 1
                    if count[value] == 0:
                        heapq.heappush(missing, value)
                index += 1
        return answer
