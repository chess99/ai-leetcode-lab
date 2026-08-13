# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:22:36Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        seen = set(); result = 0
        for word in words:
            if word[::-1] in seen: result += 1
            seen.add(word)
        return result
