# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:46:08Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        def valid(word: str) -> bool:
            i = j = 0
            while i < len(s) and j < len(word):
                if s[i] != word[j]: return False
                start_i, start_j = i, j
                while i < len(s) and s[i] == s[start_i]: i += 1
                while j < len(word) and word[j] == word[start_j]: j += 1
                if (i - start_i < j - start_j) or (i - start_i != j - start_j and i - start_i < 3): return False
            return i == len(s) and j == len(word)
        return sum(valid(word) for word in words)
