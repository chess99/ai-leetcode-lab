# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T14:40:41Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        forbidden = set(forbidden)
        maximum_length = max(map(len, forbidden))
        left = 0
        answer = 0
        for right in range(len(word)):
            for start in range(right, max(left - 1, right - maximum_length), -1):
                if word[start:right + 1] in forbidden:
                    left = start + 1
                    break
            answer = max(answer, right - left + 1)
        return answer
