# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T06:20:10Z
# Experiment: ai-leetcode-lab, round 1
from collections import Counter
from typing import List


class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        frequencies = Counter()
        for word in words:
            mask = 0
            for char in set(word):
                mask |= 1 << (ord(char) - ord('a'))
            if mask.bit_count() <= 7:
                frequencies[mask] += 1

        answer = []
        for puzzle in puzzles:
            first = 1 << (ord(puzzle[0]) - ord('a'))
            optional = 0
            for char in puzzle[1:]:
                optional |= 1 << (ord(char) - ord('a'))
            total = 0
            subset = optional
            while True:
                total += frequencies[first | subset]
                if subset == 0:
                    break
                subset = (subset - 1) & optional
            answer.append(total)
        return answer
