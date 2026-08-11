# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:59:17Z
# Experiment: ai-leetcode-lab, round 1
from collections import defaultdict
from math import gcd
from typing import List


class Solution:
    def numberOfSubsequences(self, nums: List[int]) -> int:
        n, answer = len(nums), 0
        right = defaultdict(int)
        for r in range(4, n - 1):
            for s in range(r + 2, n):
                g = gcd(nums[r], nums[s])
                right[(nums[s] // g, nums[r] // g)] += 1
        for q in range(2, n - 4):
            for p in range(q - 1):
                g = gcd(nums[p], nums[q])
                answer += right[(nums[p] // g, nums[q] // g)]
            r = q + 2
            for s in range(r + 2, n):
                g = gcd(nums[r], nums[s])
                right[(nums[s] // g, nums[r] // g)] -= 1
        return answer
