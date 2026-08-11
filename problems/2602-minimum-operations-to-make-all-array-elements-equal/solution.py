# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:01:27Z
# Experiment: ai-leetcode-lab, round 1
from bisect import bisect_right
from typing import List


class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        prefix = [0]
        for value in nums:
            prefix.append(prefix[-1] + value)
        n = len(nums)
        answer = []
        for query in queries:
            split = bisect_right(nums, query)
            left = query * split - prefix[split]
            right = (prefix[n] - prefix[split]) - query * (n - split)
            answer.append(left + right)
        return answer
