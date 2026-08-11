# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:14:12Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        words = set(dictionary)
        dp = [0] + [len(s)] * len(s)
        for end in range(1, len(s) + 1):
            dp[end] = dp[end - 1] + 1
            for start in range(end):
                if s[start:end] in words:
                    dp[end] = min(dp[end], dp[start])
        return dp[-1]
