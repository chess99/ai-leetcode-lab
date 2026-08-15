# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-sol
# Reasoning effort: medium
# Profile: sol-medium
# Created: 2026-08-15
# Experiment: ai-leetcode-lab, round 1
from collections import Counter
from typing import List


class Solution:
    def oddString(self, words: List[str]) -> str:
        differences = [
            tuple(ord(right) - ord(left) for left, right in zip(word, word[1:]))
            for word in words
        ]
        frequencies = Counter(differences)

        for word, difference in zip(words, differences):
            if frequencies[difference] == 1:
                return word
