# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T16:26:41Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        longest = max(map(len, words))
        possible = [False] * (len(s) + 1)
        possible[0] = True
        for end in range(1, len(s) + 1):
            for start in range(max(0, end - longest), end):
                if possible[start] and s[start:end] in words:
                    possible[end] = True
                    break
        return possible[-1]
