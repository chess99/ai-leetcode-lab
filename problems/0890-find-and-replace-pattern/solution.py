# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:56:16Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def matches(word):
            forward = {}; backward = {}
            for left, right in zip(word, pattern):
                if forward.get(left, right) != right or backward.get(right, left) != left: return False
                forward[left] = right; backward[right] = left
            return True
        return [word for word in words if matches(word)]
