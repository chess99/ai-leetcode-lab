# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T05:22:46Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def longestWord(self, words: List[str]) -> str:
        word_set = set(words)
        for word in sorted(words, key=lambda item: (-len(item), item)):
            word_set.remove(word)
            possible = [False] * (len(word) + 1)
            possible[0] = True
            for end in range(1, len(word) + 1):
                possible[end] = any(
                    possible[start] and word[start:end] in word_set
                    for start in range(end)
                )
            word_set.add(word)
            if possible[-1]:
                return word
        return ""
