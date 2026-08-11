# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:33:17Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def longestWord(self, words: List[str]) -> str:
        buildable = {""}
        best = ""
        for word in sorted(words, key=lambda candidate: (len(candidate), candidate)):
            if word[:-1] in buildable:
                buildable.add(word)
                if len(word) > len(best) or (len(word) == len(best) and word < best):
                    best = word
        return best
