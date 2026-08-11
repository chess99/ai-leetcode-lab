# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:21:13Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        dp = [0] + [float("inf")] * len(books)
        for end in range(1, len(books) + 1):
            width = height = 0
            for start in range(end - 1, -1, -1):
                width += books[start][0]
                if width > shelfWidth:
                    break
                height = max(height, books[start][1])
                dp[end] = min(dp[end], dp[start] + height)
        return dp[-1]
