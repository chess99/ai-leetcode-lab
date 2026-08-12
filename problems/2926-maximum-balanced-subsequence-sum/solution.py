# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T15:15:48Z
# Experiment: ai-leetcode-lab, round 1
from bisect import bisect_left
from typing import List


class Solution:
    def maxBalancedSubsequenceSum(self, nums: List[int]) -> int:
        keys = sorted(set(value - index for index, value in enumerate(nums)))
        tree = [-(10 ** 30)] * (len(keys) + 1)
        answer = -(10 ** 30)
        for index, value in enumerate(nums):
            position = bisect_left(keys, value - index) + 1
            best = 0
            query = position
            while query:
                best = max(best, tree[query])
                query -= query & -query
            candidate = best + value
            answer = max(answer, candidate)
            update = position
            while update < len(tree):
                tree[update] = max(tree[update], candidate)
                update += update & -update
        return answer
