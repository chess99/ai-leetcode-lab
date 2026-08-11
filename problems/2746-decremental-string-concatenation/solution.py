# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:14:13Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def minimizeConcatenatedLength(self, words: List[str]) -> int:
        infinity = float("inf")
        dp = [[infinity] * 26 for _ in range(26)]
        dp[ord(words[0][0]) - 97][ord(words[0][-1]) - 97] = len(words[0])
        for word in words[1:]:
            first, last = ord(word[0]) - 97, ord(word[-1]) - 97
            next_dp = [[infinity] * 26 for _ in range(26)]
            for start in range(26):
                for end in range(26):
                    length = dp[start][end]
                    if length == infinity:
                        continue
                    next_dp[start][last] = min(next_dp[start][last], length + len(word) - (end == first))
                    next_dp[first][end] = min(next_dp[first][end], length + len(word) - (last == start))
            dp = next_dp
        return min(map(min, dp))
