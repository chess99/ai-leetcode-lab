# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:44:45Z
# Experiment: ai-leetcode-lab, round 1
from bisect import bisect_right
from collections import defaultdict
from typing import List


class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        positions = defaultdict(list)
        for index, character in enumerate(s):
            positions[character].append(index)

        def is_subsequence(word: str) -> bool:
            previous = -1
            for character in word:
                indices = positions[character]
                next_index = bisect_right(indices, previous)
                if next_index == len(indices):
                    return False
                previous = indices[next_index]
            return True

        return sum(is_subsequence(word) for word in words)
