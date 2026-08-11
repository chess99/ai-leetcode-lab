# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:13:37Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        def is_subsequence(word: str) -> bool:
            position = 0
            for char in s:
                if position < len(word) and word[position] == char:
                    position += 1
            return position == len(word)

        best = ""
        for word in dictionary:
            if is_subsequence(word) and (
                len(word) > len(best) or (len(word) == len(best) and word < best)
            ):
                best = word
        return best
