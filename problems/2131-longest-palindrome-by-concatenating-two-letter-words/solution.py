# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:05:27Z
# Experiment: ai-leetcode-lab, round 1

from collections import defaultdict
from typing import List


class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        unmatched = defaultdict(int)
        length = 0

        for word in words:
            reverse = word[::-1]
            if unmatched[reverse]:
                unmatched[reverse] -= 1
                length += 4
            else:
                unmatched[word] += 1

        for word, count in unmatched.items():
            if count and word[0] == word[1]:
                return length + 2
        return length
