# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:59:17Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def beautifulSplits(self, nums: List[int]) -> int:
        n = len(nums)
        lcp = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, i, -1):
                if nums[i] == nums[j]:
                    lcp[i][j] = lcp[i + 1][j + 1] + 1
        answer = 0
        for i in range(1, n - 1):
            for j in range(i + 1, n):
                if (i <= j - i and lcp[0][i] >= i) or (j - i <= n - j and lcp[i][j] >= j - i):
                    answer += 1
        return answer
