# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:23:05Z
# Experiment: ai-leetcode-lab, round 1
from bisect import bisect_left
from typing import List
class Solution:
    def minAbsoluteDifference(self, nums: List[int], x: int) -> int:
        if x == 0: return 0
        values = sorted(set(nums)); bit = [0] * (len(values) + 1)
        def add(i):
            i += 1
            while i < len(bit): bit[i] += 1; i += i & -i
        def count(i):
            total = 0
            while i: total += bit[i]; i -= i & -i
            return total
        def kth(k):
            i = 0; step = 1 << (len(bit).bit_length() - 1)
            while step:
                if i + step < len(bit) and bit[i + step] < k: k -= bit[i + step]; i += step
                step >>= 1
            return i
        answer = float('inf')
        for i in range(x, len(nums)):
            add(bisect_left(values, nums[i - x])); p = bisect_left(values, nums[i]); before = count(p)
            if before: answer = min(answer, nums[i] - values[kth(before)])
            total = count(len(values))
            if before < total: answer = min(answer, values[kth(before + 1)] - nums[i])
        return answer
